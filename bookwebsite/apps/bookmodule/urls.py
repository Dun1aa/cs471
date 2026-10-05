from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('index2/<int:val1>/', views.index2),
    path('html5/links', views.html5_links, name="books.html5_links"),  # رابط صفحة الروابط حق لاب 5
    path('html5/text/formatting', views.html5_text_formatting, name="books.html5_text_formatting"),  # تاسك2 رابط صفحة تنسيق النص حق لاب 5
    path('html5/listing', views.html5_listing, name="books.html5_listing"),  #تاسك3 رابط صفحة القوائم حق لاب 5
        path('html5/tables', views.html5_tables, name="books.html5_tables"),  # تاسك4 رابط صفحة الجداول حق لاب 5
]
