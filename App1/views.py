from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from .forms import *
from django.db.models import Q
from .models import Post, PostLike, Slider_Post

class Index(View):
    def get(self, request):
        posts = Post.objects.all()
        user_id = request.user.id
        liked_post = Post.objects.prefetch_related('postlike_set').filter(postlike__user = user_id)
        liked_post_id = []
        for post in liked_post:
            liked_post_id.append(post.id)
        sign_up_form = Sign_Up_Form()
        sign_in_form = Sign_In_Form()
        slider_posts = Slider_Post.objects.all()
        return render(request, 'App1/index.html', locals())

    def post(self, request):
        post_id = request.POST.get('post_id')
        user_id = request.POST.get('user_id')
        like_status = request.POST.get('like_status')
        post_data = Post.objects.filter(id = post_id).first()
        if like_status == 'plus':
            post_like = PostLike.objects.create(user_id = user_id, post_id = post_id)
            post_like.save()
            post_data.total_likes = post_data.total_likes + 1
            post_data.save()
        else:
            post_like = PostLike.objects.filter(user_id = user_id)
            post_like.delete()
            post_data.total_likes = post_data.total_likes - 1
            post_data.save()
        response = {
            'post_likes': post_data.total_likes
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