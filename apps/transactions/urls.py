from django.urls import path
from .views import TransactionReportView, CachedTransactionHistory

urlpatterns = [
    path('report/', TransactionReportView.as_view()),
    path('cache/', CachedTransactionHistory.as_view()),
]
