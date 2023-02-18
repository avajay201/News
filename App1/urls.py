from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name=''),
    path('sign-up', views.Sign_Up.as_view(), name='sign-up'),
    path('sign-in', views.Sign_In.as_view(), name='sign-in')
]
