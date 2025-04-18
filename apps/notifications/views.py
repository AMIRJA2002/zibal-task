from rest_framework.response import Response
from rest_framework.views import APIView
from .sevices import send_notification

class NotifierView(APIView):
    def get(self, request):
        send_notification(['email', 'telegram'], 'amir@amir.com', 'this is a test')
        return Response({'msg': 'ok'})
