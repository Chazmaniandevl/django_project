from django.shortcuts import render
from .models import Portfolio, Project

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