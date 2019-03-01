from django.urls import path
from . import views

urlpatterns = [
    path('assets/create', views.createAsset),
    path('tenders/create', views.createTender),
    path('tenders/<int:tender_id>/buy', views.buyTender),
]
