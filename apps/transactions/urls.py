from django.urls import path
from .views import TestMongo, TransactionReportView


urlpatterns = [
    path('', TestMongo.as_view()),
    path('report/', TransactionReportView.as_view()),
]