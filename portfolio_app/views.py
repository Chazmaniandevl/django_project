

from django.http import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Portfolio, Project, Student
from django.urls import reverse_lazy, reverse

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

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'major']
    template_name = 'portfolio_app/student_form.html' 

    def form_valid(self, form):
        student = form.save()
        self.pk = student.pk
        return super().form_valid(form)

    def get_success_url(self) :
        return reverse('student_detail', kwargs={'pk': self.pk})

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name','email','major']
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name_suffix = '_confirm_delete.html'
    success_url = reverse_lazy('student_list')


class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio_app/portfolio_desc.html'
    context_object_name = 'current_portfolio'
    queryset = Portfolio.objects.all()
   
class PortfolioCreateView(CreateView):
    model = Portfolio
    fields = ['title','contact_email','about']
    template_name = 'portfolio_app/portfolio_form.html'
    success_url = reverse_lazy('index')
    
  
   
    def form_valid(self, form):
        
        form.instance.student = Student.objects.get(pk = self.kwargs.get('pk'))
        portfolio = form.save()
        self.pk = portfolio.pk
        return super(PortfolioCreateView,self).form_valid(form)

    def get_success_url(self) :
        return reverse('portfolio_desc', kwargs={'pk': self.pk})       

class PortfolioUpdateView(UpdateView):
    model = Portfolio
    fields = ['title','contact_email','about']
    template_name_suffix = "_update_form"

    def form_valid(self,form):
     portfolio = form.save()
     self.pk = portfolio.pk
     return super(PortfolioUpdateView,self).form_valid(form)

    def get_success_url(self) :
            return reverse('portfolio_desc', kwargs={'pk': self.pk})

class PortfolioDeleteView(DeleteView):
    model = Portfolio
    template_name_suffix = "_confirm_delete.html"
    success_url = reverse_lazy('student_list')
