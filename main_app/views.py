from django.shortcuts import render
from django.http import HttpResponse
# Add the Cat class & list and view function below the imports
class Loan:  # Note that parens are optional if not inheriting from another class
  def __init__(self, dateCreated, debtor, creditor, amount, dateDue, description):
    self.dateCreated = dateCreated
    self.debtor = debtor
    self.creditor = creditor
    self.amount = amount
    self.dateDue = dateDue
    self.description = description

loans = [
  Loan('10/31/23', 'Lolo', 'tabby', 1200, '1/1/24', "rent"),
  Loan('11/1/23', 'Mike', 'Kory', 500, '12/31/23', "books"),
  Loan('11/16/23', 'John', 'Smith', 85, '1/1/24', "ticket"),
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Welcome to LendAFriend</h1>')

def about(request):
  return render(request, 'about.html')

