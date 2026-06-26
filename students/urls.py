from django.urls import path
from .views import home, about, contact,students_list,create_student,single_student,filter_students,update_student,delete_student,add_student

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
    path("add/", add_student, name="add_student"),
    path("update/<int:id>/", update_student, name="update_student"),
    path("delete/<int:id>/", delete_student, name="delete_student"),
]