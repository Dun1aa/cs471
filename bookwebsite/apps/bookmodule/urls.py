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
    path('search', views.search, name="books.search"),  #  رابط صفحة البحث حق لاب 6
    path("add/", views.add_book, name="add_book"), #حق لاب 7 تاسك2 ستيب 4
    path("simple/query", views.simple_query, name="simple_query"),#لاب7 تاسك3 ستيب2
    path("complex/query", views.complex_query, name="complex_query"),#لاب 7 ستيب4
    path("lab8/task1", views.lab8_task1, name="lab8_task1"),#لاب 8 ستيب1
    path("lab8/task2", views.lab8_task2, name="lab8_task2"),#لاب 8 ستيب2
    path("lab8/task3", views.lab8_task3, name="lab8_task3"),#لاب8ستيب3
    path("lab8/task4", views.lab8_task4, name="lab8_task4"),#لاب8ستيب4
    path("lab8/task5", views.lab8_task5, name="lab8_task5"),#لاب8ستيب5
    path("lab8/task7", views.lab8_task7, name="lab8_task7"),#لاب8ستيب7
    path("lab9/task1", views.lab9_task1, name="lab9_task1"),#لاب9 تاسك1
    path("lab9/task2", views.lab9_task2, name="lab9_task2"),#لاب9تاسك2
    path("lab9/task3", views.lab9_task3, name="lab9_task3"),#لاب9 تاسك3
    path("lab9/task4", views.lab9_task4, name="lab9_task4"),#لاب9تاسك4
    path("lab9/task5", views.lab9_task5, name="lab9_task5"),
    path("lab9/task6", views.lab9_task6, name="lab9_task6"),
]
