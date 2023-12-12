from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

class Loan(models.Model):
  name = models.CharField()
  creditor = models.IntegerField() #should ref Profile
  dateCreated = models.DateField(
    default = datetime.datetime.now().date()
  )
  debtor = models.IntegerField() #should ref Debt
  amount = models.IntegerField()
  dateDue = models.DateField()
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('loan-detail', kwargs={'loan_id': self.id})

class Debt(models.Model):
  name = models.CharField()
  # Create a loan_id column in the database
  creditor = models.OneToOneField(Loan, on_delete=models.CASCADE)
  dateCreated = models.DateField(
    default = datetime.datetime.now().date()
  ) 
  amount = models.IntegerField()
  dateDue = models.DateField()
  description = models.TextField()

  #make choices for creating loan
  def __str__(self):
    return self.name
