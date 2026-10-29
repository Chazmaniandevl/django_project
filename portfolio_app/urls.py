from django.urls import path
from . import views

urlpatterns = [
    path('', views.intro, name='intro'),
    path('home/', views.intro, name='intro'),
    path('index/', views.index, name='index'),
    path('portfolio/<str:titled>', views.portfolio_desc, name='portfolio_desc'),
]
