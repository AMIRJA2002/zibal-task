from rest_framework.response import Response
from rest_framework.views import APIView
from .sevices import send_notification

class NotifierView(APIView):
    def get(self, request):
        send_notification(['email', 'telegram'], 'amir@amir.com', 'this is a test')
        return Response({'msg': 'ok'})


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from mongoengine.queryset.visitor import Q

from .models import NotificationLog, MediumEnum, StatusEnum


class NotificationLogListView(APIView):
    def get(self, request):
        medium = request.GET.get('medium')  # email, sms, telegram
        status_param = request.GET.get('status')  # pending, failed, etc.

        query = Q()
        if medium:
            query &= Q(medium=medium)
        if status_param:
            query &= Q(status=status_param)

        logs = NotificationLog.objects(query).order_by('-id')  # جدیدترین بالا

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
