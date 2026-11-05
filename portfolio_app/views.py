from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Portfolio, Project, Student

#render for homepage
def intro(request):
    return render(request, 'portfolio_app/intro.html')


def index(request):
    active_portfolios = Portfolio.objects.filter(
     is_active=True
   )
#filter for if portfolios are marked as active, saved into active_portfolios
    return render(
         request,
        'portfolio_app/index.html',
        {'active_portfolios': active_portfolios}
   )


class StudentListView(ListView):
    model = Student
    template_name = 'portfolio_app/student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'portfolio_app/student_detail.html'
    context_object_name = 'student'



def portfolio_desc( request : int, pk):
    current_portfolio = Portfolio.objects.get(
      id = pk
    )
    
    projects = Project.objects.filter(
        portfolio__title=current_portfolio.title
    )
  

    return render(
         request,
         'portfolio_app/portfolio_desc.html',
         {'current_portfolio': current_portfolio
          ,'projects':projects
          },
    )