from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Loan(models.Model):
  dateCreated = models.DateField()
  creditor = models.CharField()
  debtor = models.CharField()
  amount = models.IntegerField()
  dateDue = models.DateField()
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.creditor
  