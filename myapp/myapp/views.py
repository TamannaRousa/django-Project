from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    isActive = True
    if request.method=='POST':
        check = request.POST.get('check') #post.get - if value -true else none [no error]
        print(check)
        if check is None: isActive=False
        else: isActive=True
    
    date = datetime.datetime.now()
    name="LearnCodeForDjango"
    list_of_programs=[
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime numbers from 1 to 100',
        'WAP to print pascals triangle'
    ]
    student={
        'student_name':"Tamanna",
        'student_college':"IILM University",
        'student_city':"Noida"
    }
    # print("test function is called from view")
    #data dictionary
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs' : list_of_programs,
        'student_data': student,
    }
    return render(request,"home.html",data)
    # return HttpResponse("<h1>Hello this is index page</h1>" +str(date))

def about(request):
    # return HttpResponse("<h1> This is about page</h1>")
    return render(request,"about.html",{})

def services(request):
    # return HttpResponse("<h1> This is services page</h1>")
    return render(request,"services.html",{})
    