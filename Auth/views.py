from django.shortcuts import render
from django.http import JsonResponse , HttpResponse
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import logout as django_logout

# Create your views here.
def checkToken(request):
    data = json.loads(request.body)
    token = data["token"]
    user = data["username"]
    valid_token =  Token.objects.get(user = user)
    if valid_token.key == token:
        return True
    else:
        return False
@csrf_exempt
def getToken(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data["username"]
        password = data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                token = Token.objects.get(user = user)
                if token:
                    Token.objects.filter(user=user).update(key= token.generate_key())
                    token = Token.objects.get(user = user)
                    logout(request)
                    return JsonResponse({"token" : token.key})
                else:
                    token = Token.objects.create(user = user)
                    logout(request)
                return JsonResponse({"token" : token.key})
            else:
                logout(request)
                return HttpResponse("Disabled account")
        else:
            logout(request)
            return HttpResponse("Invalid login", status = 403 )
    else:
        return HttpResponse("Non POST Request", status = 404)
@csrf_exempt
def getTime(request):
     if checkToken(request):
         return JsonResponse({'time': str(datetime.now())})
     else:
         return JsonResponse({'error': 'Token is not valid'}, status = 403)
