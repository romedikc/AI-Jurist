from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView

from apps.users.views import (
    RegisterUserView,
    LoginUserView,
)

app_name = "users"


urlpatterns = [

    # rest framework
    path("rest-login/", include("rest_framework.urls")),

    # simple jwt
    path("token/refresh/",
         TokenRefreshView.as_view(), name="token_refresh"),

    # app endpoints
    path("registration-user/",
         RegisterUserView.as_view(), name="create_user"),
    path("login-user/",
         LoginUserView.as_view(), name="login_user"),
]
