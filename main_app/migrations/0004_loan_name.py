# Generated by Django 4.2.5 on 2023-11-30 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_loan_creditor_alter_loan_debtor'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='name',
            field=models.CharField(default='place holder'),
            preserve_default=False,
        ),
    ]