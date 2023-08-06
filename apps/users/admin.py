from django.contrib import admin

from apps.users.models import User
from apps.chat.models import ChatMessage


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id", "username", "phone", "email",
        "user_type", "is_staff", "is_superuser",
        "is_active"
    )


@admin.register(ChatMessage)
class ChatMessage(admin.ModelAdmin):
    list_display = (
        'id', 'user_input',
        'bot_response',
        'timestamp'
    )
