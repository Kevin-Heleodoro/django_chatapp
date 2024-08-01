from rest_framework import serializers

from .models import Category, Channel, Server


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.

    This serializer includes all fields of the Category model.
    """

    class Meta:
        model = Category
        fields = "__all__"


class ChannelSerializer(serializers.ModelSerializer):
    """
    Serializer for the Channel model.

    This serializer includes all fields of the Channel model.
    """

    class Meta:
        model = Channel
        fields = "__all__"


class ServerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Server model.

    This serializer includes all fields of the Server model except for the 'member' field.
    It also includes:
    - A custom field 'num_members' to represent the number of members.
    - A nested serializer 'channel_server' to include related Channel objects.

    Methods:
    - get_num_members: Returns the number of members for the server instance.
    - to_representation: Customizes the serialized data to conditionally include or exclude the 'num_members' field.
    """

    num_members = serializers.SerializerMethodField()
    channel_server = ChannelSerializer(many=True)

    class Meta:
        model = Server
        exclude = ("member",)

    def get_num_members(self, obj):
        """
        Returns the number of members for the server instance.

        Args:
            obj (Server): The server instance being serialized.

        Returns:
            int or None: The number of members if available, otherwise None.
        """
        if hasattr(obj, "num_members"):
            return obj.num_members
        return None

    def to_representation(self, instance):
        """
        Customize the serialized representation of the server instance.

        Args:
            instance (Server): The server instance being serialized.

        Returns:
            dict: The serialized data, with 'num_members' field conditionally included or excluded.
        """
        data = super().to_representation(instance)
        num_members = self.context.get("num_members")

        if not num_members:
            data.pop("num_members", None)

        return data
