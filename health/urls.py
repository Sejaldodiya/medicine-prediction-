from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about,name='about'),
    path('doctors/',views.doctors,name='doctors'),
    path('login/',views.login,name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/',views.register,name='register'),
   path('predict/<str:username>/', views.predict, name='predict'),
   path('predictView/', views.predictView, name='predictView'),
]
