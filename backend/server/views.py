from django.db.models import Count
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.response import Response

from .models import Server
from .schema import server_list_docs
from .serializers import ServerSerializer


class ServerListViewSet(viewsets.ViewSet):
    """
    A ViewSet for listing Server instances.

    This viewset handles the listing of servers with various filtering and annotation options.
    It supports filtering by category, user, server ID, and inclusion of member count.

    Attributes:
        queryset (QuerySet): The default queryset for listing Server instances.
    """

    queryset = Server.objects.all()

    @server_list_docs
    def list(self, request):
        """
        List all servers with optional filtering and pagination.

        Filters servers based on query parameters:
        - `category`: Filter servers by category name.
        - `qty`: Limit the number of results returned.
        - `by_user`: Filter servers by the authenticated user's ID.
        - `by_serverid`: Filter server by its ID.
        - `with_num_members`: Annotate servers with the number of members.

        **Args:**

        request (Request): The request object containing query parameters and user information.

        **Returns:**

        Response: A response containing the serialized list of servers.

        **Raises:**

        AuthenticationFailed: If filtering by user or server ID requires authentication and the user
            is not authenticated.

        ValidationError: If an invalid server ID is provided or no server is found for a given ID.

        **Examples:**

        List servers filtered by category:

        **Request:**
        GET /servers/?category=Gaming

        **Response:**
        ```json
        [
            {
                "id": 1,
                "name": "Epic Gaming Server",
                "category": "Gaming",
                "num_members": 150,
                "channel_server": [
                    {
                        "id": 5,
                        "name": "General Chat"
                    },
                    {
                        "id": 6,
                        "name": "Game Strategies"
                    }
                ]
            }
        ]
        ```

        List servers with pagination and member count:

        **Request:**
        GET /servers/?qty=5&with_num_members=true

        **Response:**
        ```json
        [
            {
                "id": 1,
                "name": "Epic Gaming Server",
                "num_members": 150,
                "channel_server": [
                    {
                        "id": 5,
                        "name": "General Chat"
                    }
                ]
            }
        ]
        ```

        List servers filtered by authenticated user:

        **Request:**
        GET /servers/?by_user=true
        Authorization: Bearer <valid-token>

        **Response:**
        ```json
        [
            {
                "id": 1,
                "name": "Epic Gaming Server",
                "num_members": 150,
                "channel_server": [
                    {
                        "id": 5,
                        "name": "General Chat"
                    }
                ]
            }
        ]
        ```

        Request filtered by server ID with no match:

        **Request:**
        GET /servers/?by_serverid=999

        **Response:**
        ```json
        {
            "detail": "Server with id 999 not found"
        }
        ```

        Request with invalid server ID format:

        **Request:**
        GET /servers/?by_serverid=abc

        **Response:**
        ```json
        {
            "detail": "Server value error"
        }
        ```
        """

        # Retrieve query parameters from the request
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == "true"
        by_serverid = request.query_params.get("by_serverid")
        with_num_members = request.query_params.get("with_num_members") == "true"

        # Filter the queryset by category if specified
        if category:
            self.queryset = self.queryset.filter(category__name=category)

        # Filter the queryset by the user's ID if "by_user" is set to true
        if by_user:
            if request.user.is_authenticated:
                user_id = request.user.id
                self.queryset = self.queryset.filter(member=user_id)
            else:
                raise AuthenticationFailed()

        # Annotate the queryset with the number of members if specified
        if with_num_members:
            self.queryset = self.queryset.annotate(num_members=Count("member"))

        # Limit the number of results returned if "qty" is specified
        if qty:
            self.queryset = self.queryset[: int(qty)]

        # Filter the queryset by server ID if "by_serverid" is specified
        if by_serverid:
            if not request.user.is_authenticated:
                raise AuthenticationFailed()

            try:
                self.queryset = self.queryset.filter(id=by_serverid)
                # Raise ValidationError if no server with the given ID exists
                if not self.queryset.exists():
                    raise ValidationError(detail=f"Server with id {by_serverid} not found")
            except ValueError:
                # Handle invalid server ID format
                raise ValidationError(detail="Server value error")

        # Serialize the queryset and return the response
        serializer = ServerSerializer(self.queryset, many=True, context={"num_members": with_num_members})
        return Response(serializer.data)
