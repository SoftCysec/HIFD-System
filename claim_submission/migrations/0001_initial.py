# Generated by Django 4.2.4 on 2023-08-03 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claimant_name', models.CharField(max_length=100)),
                ('claim_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supporting_documents', models.FileField(blank=True, null=True, upload_to='supporting_documents/')),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]