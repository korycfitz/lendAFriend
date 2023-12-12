from django.contrib import admin
# import your models here
from .models import Loan, Debt

# Register your models here
admin.site.register(Loan)
# register the new Debt Model 
admin.site.register(Debt)