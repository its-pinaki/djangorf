from django.contrib import admin
from testing.models import Student,Book

# Register your models here.
class BookInline(admin.TabularInline):
    extra = 0
    model = Book
    list_display = ('id', 'student','name' )
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [BookInline]
    list_display = ('id', 'name', 'roll', 'city')



