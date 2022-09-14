from testing import views
from django.urls import path,include

urlpatterns = [
    path('book/',views.getbook),
]
