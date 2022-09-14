from django.urls import path,include
from api import views
urlpatterns = [
    path('studentapi/', views.StudentListCreate.as_view()),
    path('studentapi/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),
    path('bookapi/', views.BookListCreate.as_view()),
    path('bookapi/<int:pk>/', views.BookRetrieveUpdateDestroy.as_view()),
]
