from django.shortcuts import render
from datetime import datetime
# Add the Loan class & list and view function below the imports
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

class Loan:  # Note that parens are optional if not inheriting from another class
  def __init__(self, dateCreated, creditor, debtor, amount, dateDue, description):
    self.dateCreated = dateCreated
    self.creditor = creditor
    self.debtor = debtor
    self.amount = amount
    self.dateDue = dateDue
    self.description = description

