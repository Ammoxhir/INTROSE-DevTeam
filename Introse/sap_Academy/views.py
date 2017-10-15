from django.shortcuts import render, get_object_or_404, redirect
from sap_Academy.forms import RegistrationForm
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Students, Events, Grades, Activities, Notes
from django.contrib.auth import logout

#IMAGE_FILE_TYPES =['png', 'jpg', 'jpeg']

def dashboard(request):
    return render(request, 'sapApp/dashboard.html')

def students(request):
    students_list = Students.objects.all()

    context = {
        'students_list': students_list,
    }
    return render(request, 'sapApp/students.html', context)

def grades(request):
    return render(request, 'sapApp/grades.html')

def grades2(request):
    return render(request, 'sapApp/grades2.html')

def reports(request):
    return render(request, 'sapApp/reports.html')

def login(request):
    return render(request, 'sapApp/login.html')

def signup(request):
    if request.method == 'POST':
        regform = RegistrationForm(request.POST)
        if regform.is_valid():
            regform.save()
            return redirect('/')

    regform = RegistrationForm()

    context = {
        'regform': regform,
    }
    return render(request, 'sapApp/Signup.html', context)