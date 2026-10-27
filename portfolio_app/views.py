from django.shortcuts import render
from .models import Portfolio


def index(request):
    active_portfolios = Portfolio.objects.filter(
     is_active=True
   )


    return render(
         request,
        'portfolio_app/index.html',
        {'active_portfolios':active_portfolios}
   )