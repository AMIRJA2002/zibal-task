from django.urls import path
from .views import TestMongo


urlpatterns = [
    path('', TestMongo.as_view())
]