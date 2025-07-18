from django.urls import path
from django.shortcuts import redirect
from . import views

app_name = 'student_requests'

def student_requests_home(request):
    return redirect('student_requests:student_requests_list')

urlpatterns = [
    path('', student_requests_home, name='student_requests_home'),
    path('request/', views.evaluation_view, name='evaluation_view'),
    path('success/', views.evaluation_success, name='evaluation_success'),
    path('list/', views.evaluation_list, name='evaluation_list'),
]