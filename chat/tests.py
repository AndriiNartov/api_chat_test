from collections import OrderedDict
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Message
from .serializers import MessageSerializer, MessageCreateSerializer
from .views import MessageListAPIView


class MessageAPITestCase(APITestCase):

    def setUp(self):
        self.message = Message.objects.create(author_email='john@doe.com', content_text='First message')

    def test_message_create(self):

        self.assertEqual(1, Message.objects.all().count())

        url = 'http://127.0.0.1:8000/api/chat/messages/create/'
        request_body = {'author_email': 'john@doe.com', 'content_text': 'Some message'}
        response = self.client.post(url, request_body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(2, Message.objects.all().count())

        request_body = {}
        response = self.client.post(url, request_body)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_get_massage_detail(self):

        url = f'http://127.0.0.1:8000/api/chat/messages/single/{self.message.pk}/'
        response = self.client.get(url)
        expected_data = MessageSerializer(self.message).data
        self.assertEqual(expected_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        url = 'http://127.0.0.1:8000/api/chat/messages/single/10/'
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_get_paginated_message_list(self):
        url = 'http://127.0.0.1:8000/api/chat/messages/list/0/'
        Message.objects.create(author_email='john@doe.com', content_text='Second message')
        paginate_by = MessageListAPIView.paginate_by
        queryset = Message.objects.all()[:paginate_by]
        expected_data = MessageSerializer(queryset, many=True).data
        response = self.client.get(url)
        self.assertEqual(expected_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        MessageListAPIView.paginate_by = 1
        paginate_by = MessageListAPIView.paginate_by
        queryset = Message.objects.all()[:paginate_by]
        expected_data = MessageSerializer(queryset, many=True).data
        response = self.client.get(url)
        self.assertEqual(expected_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        url = 'http://127.0.0.1:8000/api/chat/messages/list/1/'
        queryset = Message.objects.all()[paginate_by:]
        expected_data = MessageSerializer(queryset, many=True).data
        response = self.client.get(url)
        self.assertEqual(expected_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)


class MessageSerializerTestCase(TestCase):

    def setUp(self):
        self.message_1 = Message.objects.create(author_email='john@doe.com', content_text='First message')
        self.message_2 = Message.objects.create(author_email='john@doe.com', content_text='Second message')
        self.date_format = '%Y-%m-%dT%H:%M:%S.%f'

    def test_create_serializer(self):
        message_creation_data = {'author_email': 'john@doe.com', 'content_text': 'Some message'}

        data = MessageCreateSerializer(message_creation_data).data
        expected_data = {'author_email': 'john@doe.com', 'content_text': 'Some message'}

        self.assertEqual(expected_data, data)

        some_invalid_field_name = 'invalid'
        some_invalid_data = {
            f'{some_invalid_field_name}': 'Hi, it is the test post here!',
        }
        with self.assertRaises(KeyError):
            print(MessageCreateSerializer(some_invalid_data).data)

    def test_get_single_message_serializer(self):
        data = MessageSerializer(self.message_1).data
        expected_data = {
            'id': self.message_1.id,
            'author_email': self.message_1.author_email,
            'content_text': self.message_1.content_text,
            'created_at': self.message_1.created_at.strftime(format=self.date_format),
            'updated_at': self.message_1.updated_at.strftime(format=self.date_format)
        }
        self.assertEqual(expected_data, data)

    def test_get_message_list_serializer(self):

        queryset = Message.objects.all()
        data = MessageSerializer(queryset, many=True).data
        expected_data = [
            OrderedDict(
                [
                    ('id', self.message_2.id),
                    ('author_email', self.message_2.author_email),
                    ('content_text', self.message_2.content_text),
                    ('created_at', self.message_2.created_at.strftime(format=self.date_format)),
                    ('updated_at', self.message_2.updated_at.strftime(format=self.date_format))
                ]
            ),
            OrderedDict(
                [
                    ('id', self.message_1.id),
                    ('author_email', self.message_1.author_email),
                    ('content_text', self.message_1.content_text),
                    ('created_at', self.message_1.created_at.strftime(format=self.date_format)),
                    ('updated_at', self.message_1.updated_at.strftime(format=self.date_format))
                ]
            )
        ]
        self.assertEqual(expected_data, data)
