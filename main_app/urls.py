from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('loans/', views.loan_index, name='loan-index'),
  path('loans/<int:loan_id>/', views.loan_detail, name='loan-detail'),
  path('loans/create/', views.LoanCreate.as_view(), name='loan-create'),
  path('loans/<int:pk>/update/', views.LoanUpdate.as_view(), name='loan-update'),
  path('laons/<int:pk>/delete/', views.LoanDelete.as_view(), name='loan-delete'),
]