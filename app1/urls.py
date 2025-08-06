from django.urls import path
from .views import *

urlpatterns = [
    # ✅ Redirect root to login or dashboard
    path('', redirect_root_to_login, name='home_redirect'),

    # ✅ Auth
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

    # ✅ Core Pages
    path("home/", homepage, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("dashboard/", dashboard, name="dashboard"),
    path('about2/', about2, name='about2'),

    # ✅ Students
    path("user/", userDetails, name="user"),
    path("student/", student, name="student"),
    path("add/", add_student, name="add"),
    path("update/<int:id>/", update_student, name="update"),
    path("newStudent/", new_data, name="new"),
    path('deactivate/<int:id>/', deactivate_student, name='deactivate'),
    path('delete/<int:id>/', delete_student, name='delete'),
    path('activate/<int:id>/', activate_student, name='activate'),

    # ✅ Books
    path('books/', bookData, name='book'),
    path("addbook/", add_book, name="addbook"),
    path('deletebook/<int:id>/', delete_book, name='deletebook'),
    path("edit/<int:id>/", update_book, name="edit_book"),

    # ✅ Employees
    path('employees/', employee, name='employees'),
    path('addemployee/', add_employee, name='add_employee'),
    path('edit_emp/<int:id>/', edit_employee, name='edit_employee'),
    path('delete_/<int:id>/', delete_employee, name='delete_employee'),

    path('courses/', course_list, name='course_list'),
    path('courses/add/', course_create, name='course_add'),
    path('courses/edit/<int:id>/', course_update, name='course_edit'),
    path('courses/delete/<int:id>/', course_delete, name='course_delete'),



    # path('home/',home,name="home"),
    # path('contact/',contact,name="contact"),
    # path('about/',about,name="about")
]