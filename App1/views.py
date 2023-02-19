from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from .forms import *
from django.db.models import Q
from .models import Post

class Index(View):
    def get(self, request):
        posts = Post.objects.all()
        sign_up_form = Sign_Up_Form()
        sign_in_form = Sign_In_Form()
        return render(request, 'App1/index.html', locals())
    
    def post(self, request):
        post_id = request.POST.get('post_id')
        like_status = request.POST.get('like_status')
        post = Post.objects.filter(id = post_id).first()
        if like_status == 'plus':
            post.total_likes = post.total_likes + 1
            post.save()
        else:
            post.total_likes = post.total_likes - 1
            post.save()
        response = {
            'post_likes': post.total_likes
        }
        return JsonResponse(response)

class Sign_Up(View):
    def post(self, request):
        form_data = Sign_Up_Form(request.POST)
        if form_data.is_valid():
            username = form_data.cleaned_data['username']
            password = form_data.cleaned_data['password']
            email = form_data.cleaned_data['email']
            user = User.objects.filter(Q(username = username) | Q(email = email)).first()
            if user:
                response = {
                    'fail': 'User already registered with this username or email.'
                }
            else:
                user = User.objects.create_user(username, email, password)
                user.save()
                response = {
                    'success': 'Your account created successfully.'
                }
            return JsonResponse(response)
        else:
            response = {
                'errors': form_data.errors
            }
            return JsonResponse(response)
        
class Sign_In(View):
    def post(self, request):
        form_data = Sign_In_Form(request.POST)
        if form_data.is_valid():
            username = form_data.cleaned_data['username']
            password = form_data.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                response = {
                    'success': 'Sign in successfully..'
                }
            else:
                response = {
                    'fail': 'Please enter correct username or password.'
                }
            return JsonResponse(response)
        else:
            response = {
                'errors': form_data.errors
            }
            return JsonResponse(response)

class Logout(View):
    def post(self, request):
        logout(request)
        response = {
            'success': True
        }
        return JsonResponse(response)

# class About_Us(View):
#     def get(self, request):
#         return render(request, 'App1/about-us.html')

# class Contact_Us(View):
#     def get(self, request):
#         return render(request, 'App1/contact-us.html')