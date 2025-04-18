from rest_framework.response import Response
from rest_framework.views import APIView
from .sevices import send_notification
from rest_framework import status
from .models import NotificationLog


class NotifierView(APIView):
    def get(self, request):
        send_notification(['email', 'telegram'], 'ja.amir2002@gmail.com', 'this is a test')
        return Response({'msg': 'ok'})


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
