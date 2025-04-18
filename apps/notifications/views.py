from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .sevices import send_notification
from .models import NotificationLog


class NotifierView(APIView):
    class NotificationRequestSerializer(serializers.Serializer):
        mediums = serializers.ListField(
            child=serializers.ChoiceField(choices=['email', 'sms', 'telegram']),
            required=True
        )
        recipient = serializers.CharField(required=True)
        message = serializers.CharField(max_length=1000, required=True)

    def get(self, request):

        data = self.NotificationRequestSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        mediums = data.validated_data['mediums']
        recipient = data.validated_data['recipient']
        message = data.validated_data['message']

        send_notification(mediums, recipient, message)
        return Response({'message': 'notification accepted'}, status.HTTP_202_ACCEPTED)


class NotificationLogListView(APIView):
    def get(self, request):
        logs = NotificationLog.objects.order_by('-id')

        data = []
        for log in logs:
            data.append({
                'task_id': log.task_id,
                'medium': log.medium.value,
                'status': log.status.value,
                'recipient': log.recipient,
                'message': log.message,
            })

        return Response(data, status=status.HTTP_200_OK)
