from django.db import models
from datetime import datetime

class Loan(models.Model):
  dateCreated = models.DateField()
  creditor = models.CharField(max_length=100)
  debtor = models.CharField(max_length=100)
  amount = models.IntegerField()
  dateDue = models.DateField()
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.creditor
  