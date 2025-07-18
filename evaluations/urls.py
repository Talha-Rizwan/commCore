from django.urls import path
from django.shortcuts import redirect
from . import views

app_name = 'evaluations'

def evaluation_home(request):
    return redirect('evaluations:evaluation_list')

urlpatterns = [
    path('', evaluation_home, name='evaluation_home'),
    path('request/', views.evaluation_view, name='evaluation_view'),
    path('success/', views.evaluation_success, name='evaluation_success'),
    path('list/', views.evaluation_list, name='evaluation_list'),
]