from rest_framework.response import Response
from rest_framework.views import APIView
from typing import Dict, List, Union
from rest_framework import status

from .models import TransactionSummary
from .selectors import (
    get_daily_transactions,
    get_weekly_transactions,
    get_monthly_transactions,
)


class TransactionReportView(APIView):
    def get(self, request):
        t_type = request.query_params.get('type', 'amount')  # count | amount
        mode = request.query_params.get('mode', 'daily')  # daily | weekly | monthly
        merchant_id = request.query_params.get('merchantId')  # user merchant or none

        result: List[Dict[str, Union[str, int]]]
        if mode == 'daily':
            result = get_daily_transactions(type=t_type, merchant_id=merchant_id)
        elif mode == 'weekly':
            result = get_weekly_transactions(type=t_type, merchant_id=merchant_id)
        elif mode == 'monthly':
            result = get_monthly_transactions(type=t_type, merchant_id=merchant_id)

        return Response(result, status=status.HTTP_200_OK)


class CachedTransactionHistory(APIView):
    def get(self, request):
        mode = request.query_params.get('mode', 'daily')  # daily | weekly | monthly

        result = TransactionSummary.objects(mode=mode)

        res_data = []

        for i in result:
            res_data.append(i.summary)

        return Response(*res_data)
