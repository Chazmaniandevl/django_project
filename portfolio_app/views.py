from django.shortcuts import render
from django.views.generic import ListView
from .models import Portfolio, Project, Student

def intro(request):
    return render(request, 'portfolio_app/intro.html')

class StudentListView(ListView):
    model = Student
    template_name = 'portfolio_app/student_list.html'
    context_object_name = 'students'

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


def portfolio_desc( request : str, titled):
    current_portfolio = Portfolio.objects.get(
      title=titled
    )

    projects = Project.objects.filter(
        portfolio__title=current_portfolio.title
    )
    print(projects)

    return render(
         request,
        'portfolio_app/portfolio_desc.html',
        {'current_portfolio': current_portfolio,'projects':projects},
    )