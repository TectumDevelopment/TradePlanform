from django.shortcuts import render
from django.http import JsonResponse , HttpResponse
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes

# Create your views here.
@csrf_exempt
def auth(request):
    if request.method == "GET":
        data = json.loads(request.body)
        token = data["token"]
        user = request.user
        valid_token =  Token.objects.get(user = user)
        if valid_token.key == token:
            return JsonResponse({'time': str(datetime.now())})
        else:
            return HttpResponse("Invalid token", status = 403 )
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
                    return JsonResponse({"token" : token.key})
                else:
                    token = Token.objects.create(user = user)
                return JsonResponse({"token" : token.key})
            else:
                return HttpResponse("Disabled account")
        else:
            return HttpResponse("Invalid login", status = 403 )
    else:
        return HttpResponse("Non POST Request", status = 404)
