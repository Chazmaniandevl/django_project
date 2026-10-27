from django.shortcuts import render
from .models import Portfolio


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