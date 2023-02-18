from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from .forms import *

class Index(View):
    def get(self, request):
        sign_up_form = Sign_Up_Form()
        sign_in_form = Sign_In_Form()
        return render(request, 'App1/index.html', locals())
    
class Sign_Up(View):
    def post(self, request):
        form_data = Sign_Up_Form(request.POST)
        if form_data.is_valid():
            print(form_data, '+++++++++++++++++')
        else:
            print('not valid form.')
        
        return True
        # try:
        #     user = User.objects.get(username = username)
        #     if user:
        #         response = {
        #             'fail': 'User already registered with this username.'
        #         }
        #     else:
        #         user = User.objects.create_user(username, email, password)
        #         user.save()
        #         response = {
        #             'success': 'Your account created successfully.'
        #         }
        #     return JsonResponse(response)
        # except Exception as e:
        #     print(e, '===')
        #     response = {
        #         'error': 'Please try again.'
        #     }
        #     return JsonResponse(response)

class Sign_In(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(username = username, password = password)
            if user:
                response = {
                    'success': 'Sign in successfully..'
                }
            else:
                response = {
                    'fail': 'Entered username or password is not exists.'
                }
            return JsonResponse(response)
        except Exception as e:
            print(e, '===')
            response = {
                'error': 'Please try again.'
            }
            return JsonResponse(response)