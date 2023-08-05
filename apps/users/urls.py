from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenRefreshView

from apps.users.views import (
    UserView,
    LoginUserView,
)

app_name = "users"

router = DefaultRouter()
router.register('users', UserView)

urlpatterns = [
    # viewsets
    path('', include(router.urls)),

    # rest framework
    path("rest-login/", include("rest_framework.urls")),

    # simple jwt
    path("token/refresh/",
         TokenRefreshView.as_view(), name="token_refresh"),

    # app endpoints
    path("login-user/",
         LoginUserView.as_view(), name="login_user"),
]
