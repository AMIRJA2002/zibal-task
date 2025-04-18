from django.urls import path
from .views import NotifierView

urlpatterns = [
    path('test/', NotifierView.as_view())
]