from rest_framework import viewsets
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

        if category:
            self.queryset = self.queryset.filter(category__name=category)

        serializer = ServerSerializer(self.queryset, many=True)
        return Response(serializer.data)
