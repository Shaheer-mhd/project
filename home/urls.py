from django.urls import path
from home import views

app_name = 'home'
urlpatterns = [
    path('', views.fun, name='fun'),
    path('registration/', views.registration, name='registration'),


]
