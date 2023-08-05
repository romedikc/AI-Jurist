from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ChatBotViewSet

router = DefaultRouter()
router.register(r'chatbot', ChatBotViewSet, basename='ChatMessage')

urlpatterns = [
    path('', include(router.urls)),
]
