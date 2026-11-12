from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Portfolio, Project, Student
from django.urls import reverse_lazy

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
    success_url = reverse_lazy('portfolio-create')

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name','email','major']
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
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
        form.instance.student = Student.objects.latest("pk")
        return super().form_valid(form)


    
