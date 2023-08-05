from rest_framework import viewsets
from rest_framework.response import Response

from apps.chat.models import ChatMessage
from apps.chat.serializers import ChatMessageSerializer
from apps.chat.services import index


class ChatBotViewSet(viewsets.ViewSet):
    def create(self, request):
        # Get the user's query from the request data
        user_input = request.data.get('user_input')

        # Call the VectorstoreIndexCreator's query method with the user's query
        bot_response = index.query(user_input)

        # Save the chat history to the database
        chat_message = ChatMessage.objects.create(user_input=user_input, bot_response=bot_response)

        # Serialize the chat message for the response
        serializer = ChatMessageSerializer(chat_message)

        # Return the response as a JSON object
        return Response(serializer.data)
