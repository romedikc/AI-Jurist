from django.db import models


class ChatMessage(models.Model):
    user_input = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp} - User: {self.user_input}, Bot: {self.bot_response}"

