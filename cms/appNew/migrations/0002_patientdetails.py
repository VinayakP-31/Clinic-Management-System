# Generated by Django 3.0.6 on 2020-07-28 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appNew', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='patientdetails',
            fields=[
                ('pname', models.CharField(max_length=75)),
                ('pcontact', models.CharField(max_length=75)),
                ('pateid', models.CharField(max_length=75, primary_key=True, serialize=False)),
                ('ppasswd', models.CharField(max_length=75)),
            ],
        ),
    ]