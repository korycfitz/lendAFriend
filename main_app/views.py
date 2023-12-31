from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Loan

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Add new view
def loan_index(request):
  loans = Loan.objects.all()
  return render(request, 'loans/index.html', { 'loans': loans })

def loan_detail(request, loan_id):
  loan = Loan.objects.get(id=loan_id)
  return render(request, 'loans/detail.html', { 'loan': loan })

class LoanCreate(CreateView):
  model = Loan
  fields = '__all__'

class LoanUpdate(UpdateView):
  model = Loan
  #disallow Loan creator to change the name, dateCreated, debtor and amount so that the creditor can't just update the amount after it is accepted by the debtor
  fields = ['dateDue', 'description']

class LoanDelete(DeleteView):
  model = Loan
  success_url = '/loans/'