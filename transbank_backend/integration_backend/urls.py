from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('transbank/create/', views.TransbankCreate.as_view()),
    path('transbank/commit/<str:tokenws>', views.TransbankCommit.as_view()),
    path('transbank/reverseorcancel/<str:tokenws>', views.TransbankReverseOrCancel.as_view()),
]