from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Transaction
from rest_framework import serializers


class TestMongo(APIView):
    class TransactionSerializer(serializers.Serializer):
        id = serializers.CharField(source='pk')
        merchantId = serializers.CharField()
        amount = serializers.IntegerField()
        createdAt = serializers.DateTimeField()


    def get(self, request):
        transactions = Transaction.objects.order_by('created_at')[:5]
        # data = [
        #     {
        #         "id": str(tx.id),
        #         "merchant_id": str(tx.merchantId),
        #         "amount": tx.amount,
        #         "created_at": tx.createdAt.isoformat(),
        #     }
        #     for tx in transactions
        # ]
        data = self.TransactionSerializer(instance=transactions, many=True)

        return Response(data.data)
