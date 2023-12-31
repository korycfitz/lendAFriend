# Generated by Django 4.2.5 on 2023-12-12 21:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_loan_datecreated_alter_loan_datedue_debt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='creditor',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.loan'),
        ),
        migrations.AlterField(
            model_name='debt',
            name='dateCreated',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='debt',
            name='dateDue',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='debt',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='loan',
            name='dateCreated',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='loan',
            name='dateDue',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='loan',
            name='debtor',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.debt'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
