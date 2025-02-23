
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
   path('', views.home,name='home'),
   path('about/', views.about,name='about'),
   path('contact/', views.contact,name='contact'),
   path('dashboard/', views.dashboard,name='dashboard'),
   path('signup/', views.signup,name='signup'),
   path('login/', views.user_login,name='login'),
   path('logout/', views.user_logout,name='logout'),
   path('createpost/', views.createpost,name='createpost'),
   path('updatepost/<int:id>/', views.updatepost,name='updatepost'),
   path('deletepost/<int:id>/', views.deletepost,name='deletepost'),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
