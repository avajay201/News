from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.Index.as_view(), name=''),
    path('sign-up', views.Sign_Up.as_view(), name = 'sign-up'),
    path('sign-in', views.Sign_In.as_view(), name = 'sign-in'),
    path('logout', views.Logout.as_view(), name = 'logout'),
    path('post-view/<int:id>', views.Post_View.as_view(), name = 'post-view')
    # path('about-us', views.About_Us.as_view(), name='about-us'),
    # path('contact-us', views.Contact_Us.as_view(), name='contact-us'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
