from django.http import JsonResponse
def Forbidden(text):
     return JsonResponse({'Forbidden': text}, status= 403)
def NotFound(text):
    return JsonResponse({'Request Not Found': text}, status= 404)
