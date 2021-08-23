from django.urls import path

from .views import MessageCreateAPIView, MessageDetailAPIView, MessageListAPIView

urlpatterns = [
    path('messages/create/', MessageCreateAPIView.as_view()),
    path('messages/list/<int:page_num>/', MessageListAPIView.as_view()),
    path('messages/single/<int:pk>/', MessageDetailAPIView.as_view()),
]
