from django.db import models

# Create your models here.

class DoctorReg(models.Model):
    docname=models.CharField(max_length=50,primary_key=True)
    docno=models.CharField(max_length=10)
    clinic=models.CharField(max_length=30,null=False)
    docspe=models.CharField(max_length=20)
    docemail=models.CharField(max_length=20)
    docpassword=models.CharField(max_length=15)

class RecepRegister(models.Model):
    recepname=models.CharField(max_length=50,primary_key=True)
    recepno=models.CharField(max_length=10)
    recepclinic=models.CharField(max_length=50)
    recepemail=models.CharField(max_length=50)
    receppasswd=models.CharField(max_length=15)
    
class patientdetails(models.Model):
    pname=models.CharField(max_length=75)
    pcontact=models.CharField(max_length=75)
    pateid=models.CharField(max_length=75,primary_key=True)
    ppasswd=models.CharField(max_length=75) 
    
    
    
