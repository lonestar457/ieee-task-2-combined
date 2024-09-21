from django.urls import path
from. import views

urlpatterns = [
    path('', views.home, name = 'myshkhome'),
    path('about',views.about, name= 'myshkabout')
]
