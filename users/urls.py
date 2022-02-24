from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('users', AllUsersListView, basename='users')
router.register('private/users', PrivateUserView, basename='private_users')

urlpatterns = [
    path('', include('rest_framework.urls')),
    path('users/current/', UserView.as_view()),
]
urlpatterns += router.urls
