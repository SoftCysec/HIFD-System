# claim_submission/forms.py

from django import forms
from .models import Claim

class ClaimSubmissionForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['claimant_name', 'claim_amount', 'supporting_documents']
