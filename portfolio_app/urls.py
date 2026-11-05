from django.urls import path
from . import views

urlpatterns = [
    path('', views.intro, name='intro'),
    path('home/', views.intro, name='intro'),
    path('index/', views.index, name='index'),
    path('portfolio/<int:pk>', views.portfolio_desc, name='portfolio_desc'),
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
]
