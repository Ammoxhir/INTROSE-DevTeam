from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import user, student, event, grade, activitie, note
#from django.contrib.auth import logout
# Create your views here.

def login(request):
    userList = user.objects.all()
    for userTry in userList:
        if userTry.employee_id == int(request.POST['userName']):
            if userTry.user_password == request.POST['userPassword']:
                request.session["user"] = 1
                
    if request.session["user"] == 1:
        return render(request, 'sapApp/dashboard.html')
    else:
        return render(request, 'sapApp/login.html')

def dashboard(request):
    return render(request, 'sapApp/dashboard.html')

def students(request):
    user_list = user.objects.all()
    student_list = student.objects.all().order_by('-sap_id').reverse()
    context = {
        'student_list': student_list,
        'user_list': user_list,
    }
    return render(request, 'sapApp/students.html', context)

def students2(request, sapID):
    currentStudent = get_object_or_404(student, sap_id=sapID)
    context = {
        'currentStudent': currentStudent
    }
    return render(request, 'sapApp/students2.html', context)

def sortIt(request):
    user_list = user.objects.all()
    if request.POST['sortby'] == '3':
        student_list = student.objects.all().order_by('-group_number').reverse()
    elif request.POST['sortby'] == '4':
        student_list = student.objects.all().order_by('-territory').reverse()
    elif request.POST['sortby'] == '5':
        student_list = student.objects.all().order_by('-country').reverse()
    
    context = {
        'student_list': student_list,
        'user_list': user_list,
    }
    return render(request, 'sapApp/students.html', context)

def grades(request):
    return render(request, 'sapApp/grades.html')

def grades2(request):
    return render(request, 'sapApp/grades2.html')

def reports(request):
    return render(request, 'sapApp/reports.html')

def specificreport(request):
    return render(request, 'sapApp/specificreport.html')

def userprofile(request):
    return render(request, 'sapApp/userprofile.html')

def tryLogin(request):
    request.session['user'] = -1
    return render(request, 'SapApp/login.html')

def signup(request):
    return render(request, 'sapApp/signup.html')