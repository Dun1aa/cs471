from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="books.index"),  #  أضفت name عشان أستخدمه في القوالب مع {% url %}
    path('list_books/', views.list_books, name="books.list_books"),  # رابط صفحة قائمة الكتب
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),  #  أضفت name وشرطة في الآخر
    path('aboutus/', views.aboutus, name="books.aboutus"),  # رابط صفحة About
    path('index2/<int:val1>/', views.index2),  # خليتها من لاب 3 وما لها name لأن ما أحتاجها في القوالب
]