from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import *

from .serializers import *
from .models import *
from .service import *


class UserView(APIView):
    def get(self, request):
        if request.user:
            user = User.objects.filter(username=request.user).first()
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response('Response 401 Current User Users Current Get')


class PrivateUserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ShortUsersSerializer
    pagination_class = PaginationUsers
    permission_classes = (UserIsAdmin,)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ShortUsersSerializer(page, many=True)
            meta = PrivateShortUsersSerializer(page, many=True)
            data = serializer.data + meta.data
            res = self.get_paginated_response(data)
            return res

        serializer = self.get_serializer(queryset, many=True)
        meta = PrivateShortUsersSerializer(queryset, many=True)
        data = serializer.data + meta.data
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserSerializer(instance)
        return Response(serializer.data)


class AllUsersListView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ShortUsersSerializer
    pagination_class = PaginationUsers
    permission_classes = (AuthorAllStaffAllButEditOrReadOnly,)
