from django.db import models
from django.urls import reverse, timezone
from django.contrib.auth.models import User

class Loan(models.Model):
  name = models.CharField(max_length=100)  # Adjust the max_length as per your requirements
  creditor = models.IntegerField()  # Should reference Profile - consider using ForeignKey instead of IntegerField
  dateCreated = models.DateField(default=timezone.now().date)
  debtor = models.OneToOneField(
        'Debt',
        on_delete=models.CASCADE,
        null=True,  # Allows null values
        default=None  # Sets default value to None
  )
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('loan-detail', kwargs={'loan_id': self.id})

class Debt(models.Model):
  name = models.CharField()
  # Create a loan_id column in the database
  creditor = models.OneToOneField(Loan, on_delete=models.CASCADE)
  dateCreated = models.DateField(default=timezone.now().date)
  amount = models.IntegerField()
  dateDue = models.DateField(default=timezone.now().date)
  description = models.TextField()

  #make choices for creating loan
  def __str__(self):
    return self.name
