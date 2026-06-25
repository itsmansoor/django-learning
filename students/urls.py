from django.urls import path
from .views import home, about, contact,students_list,create_student,single_student,filter_students,update_student,delete_student

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path("students/", students_list, name="students"),
    path("create/", create_student),
    path("student/", single_student),
    path("filter/", filter_students),
    path("update/", update_student),
    path("delete/", delete_student),
]