from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Biodata, BookData, Student, Employee, Course


def redirect_root_to_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')


def homepage(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")

@login_required(login_url='login')
def contact(request):
    return render(request, 'contact.html')


@login_required(login_url='login')
def userDetails(request):
    user_data = Biodata.objects.all()
    book_data = BookData.objects.all()
    context = {"user_data": user_data, "book_data": book_data}
    return render(request, "users.html", context)


@login_required(login_url='login')
def bookData(request):
    book_data = BookData.objects.all()
    context = {"book_data": book_data}
    return render(request, "books.html", context)


@login_required(login_url='login')
def student(request):
    stu_data = Student.objects.all()
    context = {"stu_data": stu_data}
    return render(request, "student.html", context)


@login_required(login_url='login')
def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST.get('name'),
            age=request.POST.get('age'),
            email=request.POST.get('email'),
            profile_pic=request.FILES.get('profile_pic'),
            resume=request.FILES.get('resume')
        )
        return redirect("new")
    return render(request, "form.html")


@login_required(login_url='login')
def update_student(request, id):
    student_data = Student.objects.filter(id=id).first()
    if request.method == "POST":
        student_data.name = request.POST.get('name')
        student_data.age = request.POST.get('age')
        student_data.email = request.POST.get('email')
        if request.FILES.get('profile_pic'):
            student_data.profile_pic = request.FILES.get('profile_pic')
        if request.FILES.get('resume'):
            student_data.resume = request.FILES.get('resume')
        student_data.save()
        messages.success(request, "✅ Student updated successfully!")
        return redirect("new")
    return render(request, "update.html", {"student_data": student_data})


@login_required(login_url='login')
def new_data(request):
    stu_data = Student.objects.all()
    return render(request, "newStudent.html", {"stu_data": stu_data})


@login_required(login_url='login')
def delete_student(request, id):
    if request.method == 'POST':
        student = Student.objects.filter(id=id).first()
        student.delete()
    return redirect('new')


@login_required(login_url='login')
def deactivate_student(request, id):
    if request.method == 'POST':
        student = Student.objects.filter(id=id).first()
        student.is_active = False
        student.save()
        messages.error(request, f"{request.user.username} user deactivated successfully!")
    return redirect('new')


@login_required(login_url='login')
def activate_student(request, id):
    if request.method == 'POST':
        student = Student.objects.filter(id=id).first()
        student.is_active = True
        student.save()
        messages.error(request, f"{request.user.username} user activated successfully!")
    return redirect('new')


@login_required(login_url='login')
def add_book(request):
    if request.method == "POST":
        BookData.objects.create(
            titles=request.POST.get('titles'),
            author=request.POST.get('author'),
            price=request.POST.get('price'),
            published_date=request.POST.get('published_date')
        )
        messages.success(request, "✅ Book added successfully!")
        return redirect('book')
    return render(request, "addbooks.html")


@login_required(login_url='login')
def update_book(request, id):
    book_data = BookData.objects.filter(id=id).first()
    if request.method == "POST":
        book_data.titles = request.POST.get('titles')
        book_data.author = request.POST.get('author')
        book_data.price = request.POST.get('price')
        book_data.published_date = request.POST.get('published_date')
        book_data.save()
        messages.success(request, "✅ Book updated successfully!")
        return redirect("book")
    return render(request, "bookedit.html", {"book_data": book_data})


@login_required(login_url='login')
def delete_book(request, id):
    if request.method == 'POST':
        book = BookData.objects.filter(id=id).first()
        if book:
            book.delete()
            messages.success(request, "🗑️ Book deleted successfully!")
    return redirect('book')


@login_required(login_url='login')
def employee(request):
    emp_data = Employee.objects.all()
    return render(request, "EmployeeData.html", {"emp_data": emp_data})


@login_required(login_url='login')
def add_employee(request):
    if request.method == "POST":
        Employee.objects.create(
            name=request.POST.get('name'),
            department=request.POST.get('department'),
            salary=request.POST.get('salary'),
            email=request.POST.get('email'),
            date_joined=request.POST.get('date_joined')
        )
        messages.success(request, "✅ Employee added successfully!")
        return redirect("employees")
    return render(request, "addemp.html")


@login_required(login_url='login')
def edit_employee(request, id):
    employee = Employee.objects.filter(id=id).first()
    if request.method == "POST":
        employee.name = request.POST.get('name')
        employee.position = request.POST.get('position')
        employee.salary = request.POST.get('salary')
        employee.email = request.POST.get('email')
        employee.date_joined = request.POST.get('date_joined')
        employee.save()
        messages.success(request, "✅ Employee updated successfully!")
        return redirect("employees")
    return render(request, "empedit.html", {"employee": employee})


@login_required(login_url='login')
def delete_employee(request, id):
    employee = Employee.objects.filter(id=id)
    if employee.exists():
        employee.delete()
        messages.success(request, "🗑️ Employee deleted successfully!")
    return redirect('employees')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username_input = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=username_input).first() or User.objects.filter(email=username_input).first()
        if user_obj:
            user = authenticate(request, username=user_obj.username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome {user.username}!")
                return redirect('dashboard')
            messages.error(request, 'Incorrect password.')
        else:
            messages.error(request, 'User not found.')
    return render(request, 'auth/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')
        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')
    return render(request, 'auth/register.html')

def about2(request):
    return render(request, 'about2.html')

@login_required(login_url='login')
def course_list(request):
    courses = Course.objects.all().order_by('-created_at')
    return render(request, 'course/course_list.html', {'courses': courses})


@login_required(login_url='login')
def course_create(request):
    if request.method == 'POST':
        Course.objects.create(
            name=request.POST.get('name'),
            code=request.POST.get('code'),
            credit=request.POST.get('credit'),
            instructor=request.POST.get('instructor'),
            description=request.POST.get('description')
        )
        messages.success(request, "✅ Course added successfully!")
        return redirect('course_list')
    return render(request, 'course/course_form.html', {'title': 'Add Course'})


@login_required(login_url='login')
def course_update(request, id):
    course = Course.objects.filter(id=id).first()
    if request.method == 'POST':
        course.name = request.POST.get('name')
        course.code = request.POST.get('code')
        course.credit = request.POST.get('credit')
        course.instructor = request.POST.get('instructor')
        course.description = request.POST.get('description')
        course.save()
        messages.success(request, "✅ Course updated successfully!")
        return redirect('course_list')
    return render(request, 'course/course_form.html', {'course': course, 'title': 'Edit Course'})


@login_required(login_url='login')
def course_delete(request, id):
    course = Course.objects.filter(id=id).first()
    if request.method == 'POST':
        course.delete()
        messages.success(request, "🗑️ Course deleted successfully!")
        return redirect('course_list')
    return render(request, 'course/course_confirm_delete.html', {'course': course})
