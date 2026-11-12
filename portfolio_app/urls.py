from django.urls import path
from . import views

urlpatterns = [
    path('', views.intro, name='intro'),
    path('home/', views.intro, name='intro'),

#portfolio paths \/
    path('index/', views.index, name='index'),#list
    path('portfolio/<int:pk>', views.PortfolioDetailView.as_view(), name='portfolio_desc'),#single desc
    path('portfolio/create/', views.PortfolioCreateView.as_view(), name ='portfolio-create'),#creation

#student paths \/
    path('students/', views.StudentListView.as_view(), name='student_list'),#list
    path('students/<int:pk>/view', views.StudentDetailView.as_view(), name='student_detail'),#single student
    path('students/create/', views.StudentCreateView.as_view(),name='student-create'),#create
    path('students/<int:pk>/',views.StudentUpdateView.as_view(), name="student-update"),#update

#project paths \/
    
]
