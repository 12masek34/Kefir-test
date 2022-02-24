from rest_framework.permissions import  IsAuthenticated
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
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = ShortUsersSerializer(page, many=True)
                meta = PrivateShortUsersSerializer(page, many=True)
                data = set_data_and_meta(serializer, meta)
                res = self.get_paginated_response(data)
                return res

            serializer = self.get_serializer(queryset, many=True)
            meta = PrivateShortUsersSerializer(queryset, many=True)
            data = serializer.data + meta.data
            return Response(data)
        except AttributeError:
            return Response('User Unauthorized')

    def retrieve(self, request, *args, **kwargs):
        self.permission_classes = (UserIsAdmin,)
        try:
            if request.user.is_admin:
                instance = self.get_object()
                serializer = UserSerializer(instance)
                return Response(serializer.data)
        except AttributeError:
            return Response('User Unauthorized')
        return Response('Response 403 Private Get User Private Users  Pk  Get')


class AllUsersListView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ShortUsersSerializer
    pagination_class = PaginationUsers
    permission_classes = (AuthorAllStaffAllButEditOrReadOnly,)
