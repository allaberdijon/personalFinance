from django.shortcuts import render
from .models import Expense
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .forms import Expenseform
from .models import Expense
# Create your views here.

def expenses_list(request):
    expenses = Expense.objects.all()
    return render(request,'expenses_list.html',{'expenses':expenses})

class ExpensesCreateView(CreateView):
    model = Expense
    form_class = Expenseform
    template_name = 'expenses_create.html'
    success_url = reverse_lazy('expenses_list')

class ExpensesDetailView(DetailView):
    model = Expense
    context_object_name = 'expense'
    template_name = 'expenses_detail.html'