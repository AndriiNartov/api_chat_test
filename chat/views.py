from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Message
from .serializers import MessageCreateSerializer, MessageSerializer
from .services import make_custom_paginated_queryset


class MessageCreateAPIView(CreateAPIView):
    '''Create a message. Body must contain author email end message text.'''

    serializer_class = MessageCreateSerializer


class MessageDetailAPIView(RetrieveAPIView):
    '''Return details of single message by unique identificator from db.'''

    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class MessageListAPIView(APIView):
    '''Return paginated list of messages from db. Pages count starts with 0(according to the test task).'''

    paginate_by = 10

    def get(self, *args, **kwargs):
        queryset = make_custom_paginated_queryset(kwargs['page_num'], self.paginate_by)
        serializer = MessageSerializer(queryset, many=True)
        return Response(data=serializer.data)
