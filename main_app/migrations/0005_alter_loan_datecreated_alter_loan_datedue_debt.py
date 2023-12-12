# Generated by Django 4.2.5 on 2023-12-12 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_loan_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='dateCreated',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='loan',
            name='dateDue',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('dateCreated', models.DateField()),
                ('amount', models.IntegerField()),
                ('dateDue', models.DateField()),
                ('description', models.TextField()),
                ('creditor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.loan')),
            ],
        ),
    ]
