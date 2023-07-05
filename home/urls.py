from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('data', views.data, name='data'),
    path('remove/<str:pk>/', views.remove, name='remove'),
    path('start/', views.start, name='start'),
    path('verify/', views.Verify, name='verify'),
    path('show/<str:pk>/', views.show, name='show'),
    path('regis/<str:pk>/', views.regis, name='regis'),
    path('userlogin/', views.UserLogin, name='userlogin'),
    path('userlogout/', views.UserLogout, name='userlogout'),
    path('statement/', views.Statement, name='statement'),
    path('report/', views.Report, name='report'),
    path('remove_statement/<str:pk>/', views.remove_statement, name='remove_statement'),
    path('feed/', views.Feed, name='feed'),
    path('feedv/<str:pk>/', views.FeedV, name='feedv'),
]