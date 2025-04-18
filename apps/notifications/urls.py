from django.urls import path
from .views import NotifierView, NotificationLogListView

urlpatterns = [
    path('send/', NotifierView.as_view()),
    path('logs/', NotificationLogListView.as_view()),
]