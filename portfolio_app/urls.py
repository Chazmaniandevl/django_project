from django.urls import path
from . import views

urlpatterns = [
    path('', views.intro, name='intro'),
    path('home/', views.intro, name='intro'),

    path('index/', views.index, name='index'),
    path('portfolio/<int:pk>', views.portfolio_desc, name='portfolio_desc'),
    # path('portfolio/<int:pk>', views.PortfolioDetailView.as_view(), name='portfolio_desc'),
    path('portfolio/create/<int:pk>/', views.PortfolioCreateView.as_view(), name ='portfolio-create'),

    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/view', views.StudentDetailView.as_view(), name='student_detail'),
    path('students/create/', views.StudentCreateView.as_view(),name='student-create'),
    path('students/<int:pk>/',views.StudentUpdateView.as_view(), name="student-update"),
    
]
