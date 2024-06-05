
from django.contrib import admin
from django.urls import path
from users.api import UserAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    # users
    path('users/', UserAPI.as_view()),
]
