from django.shortcuts import render
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

loans = [
  Loan('10/31/23', 'Lolo', 'tabby', 1200, '1/1/24', "rent"),
  Loan('11/1/23', 'Mike', 'Kory', 500, '12/31/23', "books"),
  Loan('11/16/23', 'John', 'Smith', 85, '1/1/24', "ticket"),
]