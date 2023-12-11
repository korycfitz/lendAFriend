from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime


CREDITORS = (
  ('1', 'User 1'),
  ('2', 'User 2'),
  ('3', 'User 3'),
  ('4', 'User 4'),
  ('5', 'User 5')
)

class Loan(models.Model):
  name = models.CharField()
  creditor = models.IntegerField() #should ref Profile
  dateCreated = models.DateField()
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
  creditor = models.IntegerField(
    max_length=1, 
    choices=CREDITORS,
    default=CREDITORS[0][0]
  ) 
  dateCreated = models.DateField() 
  amount = models.IntegerField()
  dateDue = models.DateField()
  description = models.TextField()

  #make choices for creating loan
  def __str__(self):
    return self.name
