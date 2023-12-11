from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime


class Loan(models.Model):
  name = models.CharField()
  creditor = models.IntegerField()
  dateCreated = models.CharField(max_length=100)
  debtor = models.IntegerField()
  amount = models.IntegerField()
  dateDue = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('loan-detail', kwargs={'loan_id': self.id})

class Debt(models.Model):
  name = models.CharField()
  creditor = models.IntegerField() 
  dateCreated = models.DateField() 
  debtor = models.IntegerField() #should ref. Loan
  amount = models.IntegerField()
  dateDue = models.DateField()
  description = models.TextField(max_length=250)
