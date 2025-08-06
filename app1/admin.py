from django.contrib import admin
from .models import Biodata, BookData, Student, Employee, Course

@admin.register(Biodata)
class BiodataAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'address', 'email', 'phone_number', 'dob', 'created_at', 'updated_at')
    search_fields = ('name', 'email')
    list_filter = ('gender', 'dob')

@admin.register(BookData)
class BookDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'titles', 'author', 'price', 'published_date')
    search_fields = ('titles', 'author')
    list_filter = ('price',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'email', 'created_at', 'updated_at', 'is_active')
    search_fields = ('name',)
    list_filter = ('age',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'department', 'salary', 'email', 'date_joined')
    search_fields = ('name', 'email',)
    list_filter = ('department',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'credits', 'instructor', 'created_at', 'updated_at')
    search_fields = ('name', 'code', 'instructor__name')  # For related instructor search
    list_filter = ('credits', 'created_at')

