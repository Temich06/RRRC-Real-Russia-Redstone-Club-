from knox import views as know_views
from django.urls import path
from .views import RegisterAPI, LoginAPI, LogoutAPI

urlpatterns = [
    path('reg/', RegisterAPI.as_view(), name='register'),
    path('log/', LoginAPI.as_view(), name='login'),
    path('logout/', LogoutAPI.as_view(), name='logout'),
    path('logoutall/', know_views.LogoutAllView.as_view(), name='logoutall'),
]