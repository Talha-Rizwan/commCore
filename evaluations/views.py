from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import Student
from .models import Evaluation

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = []

@login_required
def evaluation_view(request):
    # Check if user is a student
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        messages.error(request, 'Only students can request evaluations.')
        return redirect('evaluations:evaluation_list')
    
    # Check if student already has an evaluation request
    existing_evaluation = Evaluation.objects.filter(student=student).first()
    if existing_evaluation:
        messages.warning(request, f'You have already submitted an evaluation request on {existing_evaluation.evaluation_date.strftime("%B %d, %Y")}. Status: {existing_evaluation.status}')
        return redirect('evaluations:evaluation_list')
    
    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():
            evaluation = form.save(commit=False)
            evaluation.student = student
            evaluation.save()
            messages.success(request, f'Evaluation request has been submitted successfully.')
            return redirect('evaluations:evaluation_success')
    else:
        form = EvaluationForm()
    
    return render(request, 'evaluations/evaluation_form.html', {
        'form': form, 
        'student': student
    })

def evaluation_success(request):
    return render(request, 'evaluations/evaluation_success.html')

def evaluation_list(request):
    evaluations = Evaluation.objects.all().order_by('-evaluation_date')
    
    # Check if current user can request evaluation
    can_request_evaluation = False
    if request.user.is_authenticated:
        try:
            student = Student.objects.get(user=request.user)
            existing_evaluation = Evaluation.objects.filter(student=student).first()
            can_request_evaluation = not existing_evaluation
        except Student.DoesNotExist:
            can_request_evaluation = False
    
    return render(request, 'evaluations/evaluation_list.html', {
        'evaluations': evaluations,
        'can_request_evaluation': can_request_evaluation
    })