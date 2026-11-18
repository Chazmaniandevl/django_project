from django.urls import path
from . import views

urlpatterns = [
    path('', views.intro, name='intro'),
    path('home/', views.intro, name='intro'),

#student paths \/
    path('students/', views.StudentListView.as_view(), name='student_list'),#list
    path('students/view/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),#single student
    path('students/create/', views.StudentCreateView.as_view(),name='student-create'),#create
    path('students/<int:pk>/',views.StudentUpdateView.as_view(), name="student-update"),#update    
    path('students/delete/<int:pk>/',views.StudentDeleteView.as_view(), name ='student-delete'),#delete

#portfolio paths \/
    path('index/', views.index, name='index'),#list
    path('portfolio/<int:pk>/', views.PortfolioDetailView.as_view(), name='portfolio_desc'),#single desc
    path('portfolio/create/<int:pk>/', views.PortfolioCreateView.as_view(), name ='portfolio-create'),#creation
    path('portfolio/update/<int:pk>/', views.PortfolioUpdateView.as_view(), name='portfolio-update'),#updating
    path('portfolio/delete/<int:pk>/', views.PortfolioDeleteView.as_view(), name='portfolio-delete'),#deletion

#project paths \/
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('project/create/<int:pk>/', views.ProjectCreateView.as_view(), name='project-create'),

    
]
