from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.response import Response

from .models import Server
from .serializers import ServerSerializer

# Using class-based view -> viewsets
# classes come pre-configured with some basic CRUD logic
# https://www.django-rest-framework.org/api-guide/viewsets/


class ServerListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()

    def list(self, request):
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == "true"
        by_serverid = request.query_params.get("by_serverid")

        if by_user or by_serverid and not request.user.is_authenticated:
            # Throw 403
            raise AuthenticationFailed()

        if category:
            self.queryset = self.queryset.filter(category__name=category)

        if by_user:
            user_id = request.user.id
            self.queryset = self.queryset.filter(member=user_id)

        if qty:
            self.queryset = self.queryset[: int(qty)]

        if by_serverid:
            try:
                self.queryset = self.queryset.filter(id=by_serverid)
                if not self.queryset.exists():
                    raise ValidationError(detail=f"Server with id {by_serverid} not found")
            except ValueError:
                raise ValidationError(detail="Server value error")

        serializer = ServerSerializer(self.queryset, many=True)
        return Response(serializer.data)
