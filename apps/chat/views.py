from rest_framework import viewsets
from rest_framework.response import Response

from apps.chat.models import ChatMessage
from apps.chat.serializers import ChatMessageSerializer
from apps.chat.services import index


class ChatBotViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

    def create(self, request, *args, **kwargs):
        user_input = request.data.get('user_input')
        bot_response = index.query(user_input)
        chat_message = ChatMessage.objects.create(user_input=user_input, bot_response=bot_response)
        serializer = ChatMessageSerializer(chat_message)
        return Response(serializer.data)
