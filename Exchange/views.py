from django.shortcuts import render
from Auth.views import checkToken
from JsonFactory.JsonFactory import Forbidden, NotFound
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from .models import Commodity ,Asset
from decimal import Decimal
# Create your views here.
def createAsset(request):
    data = json.loads(request.body)
    user_name = data['username']
    if checkToken(request):
        try:
            user = User.objects.get(username = user_name )
        except:
            return NotFound("No such user " + user_name)
        сommodity_name = data["Asset"]["Commodity"]["сommodity_name"]
        try:
            commodity = Commodity.objects.get(name = сommodity_name)
        except:
            return NotFound("No such commodity " + сommodity_name)
        amount = Decimal(data["Asset"]["ammount"])
        if len(Asset.objects.filter(commodity= commodity , user = user)) > 0:
            asset = Asset.objects.get(commodity= commodity ,user = user)
            asset.amount = asset.amount + amount
            asset.save()
            return JsonResponse({"Success":"added" , "amount" :asset.amount })
        else:
            asset = Asset.objects.create(commodity= commodity ,user = user , amount = amount )
            return JsonResponse({"Success":"created" , "amount" :asset.amount })


    else:
        return Forbidden("Invalid token")
