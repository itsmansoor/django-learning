from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .forms import StudentForm

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


def add_student(request):

    if request.method == "POST":

        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")

        Student.objects.create(
            name=name,
            age=age,
            email=email
        )

        return redirect("students")

    return render(request, "add_student.html")

def update_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":

        student.name = request.POST.get("name")
        student.age = request.POST.get("age")
        student.email = request.POST.get("email")

        student.save()

        return redirect("students")

    return render(request, "update_student.html", {
        "student": student
    })

def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    student.delete()

    return redirect("students")

def add_student(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("students")

    else:
        form = StudentForm()

    return render(request, "add_student.html", {
        "form": form
    })