from re import I
from django.shortcuts import render,redirect,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, JsonResponse,HttpResponse


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
     
    return render(request, 'student_details.html', context)

def update_student(request, student_id):
    student = get_object_or_404(Student, id = student_id)    

    if request.method == "POST":        
        form = StudentForm(request.POST)        
        if form.is_valid():                         
            message = []

            prevfname = student.first_name
            fname = form.cleaned_data['first_name']
            if prevfname != fname:
                Student.objects.filter(id=student_id).update(first_name=fname)
                message.append(' Student First Name Updated ')             

            prevsname = student.second_name
            sname = form.cleaned_data['second_name']
            if prevsname != sname:
                Student.objects.filter(id=student_id).update(second_name=sname)                
                message.append(' Student Second Name Updated ')

            prevage = student.age
            age = form.cleaned_data['age']
            if prevage != age:
                Student.objects.filter(id=student_id).update(age=age)                
                message.append(' Student Age Updated ')

            prevstream = student.mystream
            stream = form.cleaned_data['mystream']
            if prevstream != stream:                
                Student.objects.filter(id=student_id).update(mystream=stream)                
                message.append(' Student Stream Updated ') 

            prevadm_no = student.adm_no
            adm_no = form.cleaned_data['adm_no']
            if prevadm_no != adm_no:
                student.save(update_fields=['adm_no'])
                Student.objects.filter(id=student_id).update(adm_no=adm_no)                
                message.append(' Student Admission Number Updated ')                    

            data = {'message':message}

            return JsonResponse(data)


def new_student(request):
    title = "New Student"
    form = StudentForm()

    context = {
        "title":title,
        "form":form
    }                        

    return render(request, 'student_upload.html', context)

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)        
        if form.is_valid():             
            if is_ajax(request):
                fname = form.cleaned_data.get('first_name')
                form.save()
                student = get_object_or_404(Student, first_name = fname)                    
                message = "Student has been added"
                new_url = redirect('studentDetails', student_id=student.id).url

                data = {'message':message, 'new_url':new_url}

                return JsonResponse(data)  

def delete_student(request,student_id):

    student = get_object_or_404(Student, id = student_id)    
    student.delete()   

    return HttpResponseRedirect("/")

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
