from django.urls import path
from .views import NotifierView, NotificationLogListView

urlpatterns = [
    path('test/', NotifierView.as_view()),
    path('logs/', NotificationLogListView.as_view()),
]