from re import I
from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, JsonResponse


from .models import (
    Stream,
    Student
)

from .forms import (
    StudentForm
)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def home(request):
    title = "Kilimo High School" 
    all_students = Student.get_allStudents()
    all_streams = Stream.get_allStreams

    students = all_students

    context = {
        "title":title,
        "students": students,
        "streams":all_streams
    }

    return render(request, 'index.html', context)

def student_edit(request, student_id):
    try:        
        student = Student.objects.filter(id=student_id).first()        
        title = student.first_name + ' ' + student.second_name + " Details"

    except ObjectDoesNotExist:
        return redirect('home')
    
    context = {
        "title":title,
        "student":student,
        "form":StudentForm(instance=student)
    }

    if request.method == "POST":        
        form = StudentForm(request.POST)
        if form.is_valid():       
            if is_ajax(request):      
                message = []

                prevname = student.first_name
                name = form.cleaned_data('first_name')
                if prevname != name:
                    student.save(update_fields=['service_img'])
                    message.append(' Student First Name Updated ')             

                print(message)

                data = {'message':message}

                return JsonResponse(data) 

    return render(request, 'student_details.html', context)

def new_student(request):
    title = "New Student"
    form = StudentForm()

    context = {
        "title":title,
        "form":form
    }

    if request.method == "POST":
        if form.is_valid():       
            if is_ajax(request):
                form.save()
                # message = "Student has been added"

                # data = {'message':message}

                # return JsonResponse(data) 
                return redirect('home')        


    return render(request, 'student_upload.html', context)

def stream_view(request,stream_id):
    try :
        stream = Stream.objects.filter(id=stream_id).first()
        title = stream.stream_name + " Details"
    except ObjectDoesNotExist:
        return redirect('home')        

    students = Student.objects.filter(mystream=stream_id)
    all_streams = Stream.get_allStreams

    context = {
        "title":title,
        "students":students,        
        "main_stream":stream_id,
        "streams":all_streams
    }

    return render(request, 'stream_details.html', context)
