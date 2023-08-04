# claim_submission/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.claim_submission_view, name='claim_submission'),
    path(r'<int:claim_id>/', views.fraud_detection_results_view, name='fraud_detection_results'),
]
