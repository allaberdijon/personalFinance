from django import forms 
from .models import Expense

class Expenseform(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category','amount','date','description']