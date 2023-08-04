# claim_submission/views.py

from django.shortcuts import render, redirect
from .forms import ClaimSubmissionForm
from .models import Claim, FraudDetectionResult

def claim_submission_view(request):
    if request.method == 'POST':
        form = ClaimSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            claim = form.save()
            # Perform fraud detection and save the results
            is_fraudulent, evidence = perform_fraud_detection(claim)
            FraudDetectionResult.objects.create(claim=claim, is_fraudulent=is_fraudulent, evidence=evidence)
            # Redirect to a success page or display a success message
            return redirect('dashboard')  # Replace 'dashboard' with your desired URL name for the dashboard
    else:
        form = ClaimSubmissionForm()
    
    return render(request, 'claim_submission/claim_submission.html', {'form': form})

def fraud_detection_results_view(request, claim_id):
    try:
        claim = Claim.objects.get(pk=claim_id)
        result = FraudDetectionResult.objects.get(claim=claim)
        return render(request, 'claim_submission/fraud_detection_results.html', {'claim': claim, 'result': result})
    except (Claim.DoesNotExist, FraudDetectionResult.DoesNotExist):
        return render(request, 'claim_submission/fraud_detection_results.html', {'claim': None, 'result': None})

def perform_fraud_detection(claim):
    # Placeholder for fraud detection logic
    # Implement your fraud detection algorithm here
    # Example: For demo purposes, we'll assume all claims with an amount greater than 1000 as fraudulent
    is_fraudulent = claim.claim_amount > 1000
    evidence = "Amount exceeds threshold"
    return is_fraudulent, evidence
