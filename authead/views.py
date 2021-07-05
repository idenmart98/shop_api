from datetime import timedelta

from django.utils.timezone import now
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.models import Token


from .serializers import EmailRegistrationSerializer
from .models import ConfirmationCode

from .tasks import send_verify_url, code_expired, code_confirm, user_expired


User = get_user_model()

class EmailRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = EmailRegistrationSerializer

    def perform_create(self, serializer):
        password = self.request.POST['password']
        self.request.data._mutable = True
        self.request.POST['password'] = make_password(password)
        self.request.data._mutable = False
        obj = serializer.save()
        code = ConfirmationCode.objects.create(user=obj)
        code_expired.apply_async((code.id, ), eta=now() + timedelta(seconds=15))
        user_expired.apply_async((obj.id,), eta=now() + timedelta(seconds=15))
        send_verify_url.apply_async((f'http://127.0.0.1:8000/authe/email_verify/{code.code}', obj.email))

@api_view(['GET'])
def confirm_email(request, code):
    code = ConfirmationCode.objects.filter(code=code)
    if code:
        code_confirm(code)
        token = Token.objects.update_or_create(user_id=code.user.id)
        return Response({
            "success": True, 
            "data": {'token': str(token[0])}}, 
            status.HTTP_200_OK)
    return Response({
        "success": True, 
        "data": {'code':'invalid'}}, 
        status.HTTP_400_BAD_REQUEST)
    

