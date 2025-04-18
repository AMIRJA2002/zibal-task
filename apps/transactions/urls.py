from django.urls import path
from .views import TransactionReportView, CachedTransactionHistory

urlpatterns = [
    path('report/', TransactionReportView.as_view()),
    path('cache-report/', CachedTransactionHistory.as_view()),
]
