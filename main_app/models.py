from django.db import models

class Loan(models.Model):
  creditor = models.TextField()
  dateCreated = models.CharField(max_length=100)
  debtor = models.TextField()
  amount = models.IntegerField()
  dateDue = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.creditor
  