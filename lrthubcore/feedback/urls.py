# Created by Joshua de Guzman on 07/07/2018
# @email code@jmdg.io

from django.urls import path
from . import views
from .api import views

urlpatterns = [
    path('', views.FeedbackConversationList.as_view(), name='api_feedback_list'),
    path('<int:pk>/', views.FeedbackConversationDetail.as_view(), name='api_feedback_detail'),
]