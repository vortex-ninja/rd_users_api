from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='users'),
    path('users/me/', views.LoggedInUserView.as_view(), name='logged_in_user'),
    path('login/', obtain_jwt_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
