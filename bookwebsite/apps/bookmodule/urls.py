from django.urls import path  #  ملف جديد لروابط تطبيق الكتب
from . import views

urlpatterns = [
    path('', views.index),
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>', views.viewbook),
]