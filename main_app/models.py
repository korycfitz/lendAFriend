from django.db import models
from django.urls import reverse
from django.utils import timezone

class Loan(models.Model):
    name = models.CharField(max_length=100)
    creditor = models.IntegerField()  # Consider using ForeignKey to reference a User or Profile model
    dateCreated = models.DateField(default=timezone.now)
    debtor = models.ForeignKey('Debt', on_delete=models.CASCADE, null=True, default=None)
    amount = models.IntegerField()
    dateDue = models.DateField(default=timezone.now)
    description = models.TextField(max_length=250)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('loan-detail', kwargs={'loan_id': self.id})

class Debt(models.Model):
    name = models.CharField(max_length=100)  # Define max_length for CharField
    creditor = models.ForeignKey('Loan', on_delete=models.CASCADE, null=True, default=None)
    dateCreated = models.DateField(default=timezone.now)
    amount = models.IntegerField()
    dateDue = models.DateField(default=timezone.now)
    description = models.TextField()
    
    def __str__(self):
        return self.name
