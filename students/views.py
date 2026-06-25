from django.shortcuts import render
from .models import Student

def home(request):
    return render(request, "home.html",{
         "name": "Muhammad Mansoor",
        "course": "Django"
    })

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")



def students_list(request):
    students = Student.objects.all()

    return render(request, "students.html", {
        "students": students
    })

def create_student(request):

    Student.objects.create(
        name="Ali",
        age=22,
        email="ali@gmail.com"
    )

    return render(request, "success.html")

def single_student(request):

    student = Student.objects.get(id=1)

    return render(request, "single_student.html", {
        "student": student
    })

def filter_students(request):

    students = Student.objects.filter(age=22)

    return render(request, "students.html", {
        "students": students
    })

def update_student(request):

    student = Student.objects.get(id=1)

    student.name = "Muhammad Mansoor"
    student.save()

    return render(request, "success.html")

def delete_student(request):

    student = Student.objects.get(id=1)

    student.delete()

    return render(request, "success.html")