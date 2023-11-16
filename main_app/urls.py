from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('loans/', views.loan_index, name='loan-index'),
  path('loans/<int:loan_id>/', views.loan_detail, name='loan-detail'),
]