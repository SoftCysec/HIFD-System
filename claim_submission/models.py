# claim_submission/models.py

from django.db import models

class Claim(models.Model):
    claimant_name = models.CharField(max_length=100)
    claim_amount = models.DecimalField(max_digits=10, decimal_places=2)
    supporting_documents = models.FileField(upload_to='supporting_documents/', blank=True, null=True)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.claimant_name

class FraudDetectionResult(models.Model):
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE)
    is_fraudulent = models.BooleanField()
    evidence = models.TextField()

    def __str__(self):
        return f"{self.claim.claimant_name} - Fraudulent: {self.is_fraudulent}"
