from django.db import models

class Loan(models.Model):
  dateCreated = models.DateField()
  creditor = models.CharField() #this will be linked to the current object id and will need to  eventuall add logic to make debtor to the current user_id
  debtor = models.CharField() #will need to change once we input the either a model for the other user id or a way to search for them and set equal to this
  amount = models.IntegerField()
  dateDue = models.DateField()
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.creditor