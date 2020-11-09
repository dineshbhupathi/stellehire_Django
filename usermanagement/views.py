from rest_framework.generics import *
from .models import *
from .serializers import *
from django.contrib.auth import login, authenticate,logout
from rest_framework.response import Response
import json

class UsersView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


'''
{
"username": "dky",
"password":"dinesh123"
}
'''
class Login(views.APIView):
    def post(self, request):
        if not request.data:
            return Response({'Error': "Please provide username/password"}, status="400")
        username = request.data['username']
        password = request.data['password']
        try:
            user = authenticate(username=username, password=password)
        except User.DoesNotExist:
            return Response({'Error': "Invalid username/password"}, status="400")
        print(user,'nee')
        if user:
            login(request, user)
            print(user,'skldfjkl')
            return Response(
                json.dumps({'success': "loged in"}),
                status=200,
                content_type="application/json"
            )
        else:
            return Response(
                json.dumps({'Error': "Invalid credentials"}),
                status=404,
                content_type="application/json"
            )
