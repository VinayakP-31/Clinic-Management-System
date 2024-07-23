from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import mysql.connector

# Create your views here.
global profile,content
content={}
profile={}
content_recep={}
profile_recep={}

#Displays Homepage
def index(request):
    return render(request,'homepage.html')

#Redirects back to Homepage
def redirect(request):
    return render(request,'homepage.html')

#To register a doctor
def Doc_register(request):

    if request.method=='GET':
        return render(request,'docregister.html')
    elif request.method=='POST':

        doc_name=request.POST['docname']
        doc_no=request.POST['docno']
        doc_clinic=request.POST['docclinic']
        doc_spe=request.POST['docspe']
        doc_email=request.POST['docemail']
        doc_pass=request.POST['docpass']
        
        if request.GET['a']=='docreg':
            con=mysql.connector.connect(host="localhost",user="root",passwd="vini",database="project")
            mycursor=con.cursor()
            if con.is_connected():
                try:
                    sql="insert into appnew_doctorreg values('{}','{}','{}','{}','{}','{}')".format(doc_name,doc_no,doc_clinic,doc_spe,doc_email,doc_pass)
                    mycursor.execute(sql)
                    con.commit()
                except:
                    print("error")
                finally:
                    con.close()
            return render(request,'homepage.html')
        else:
            return render(request,'homepage.html')
            
#Doctor login          
def Doc_signin(request):
    if request.method=='GET':
        return render(request,'docsignin.html')
    elif request.method=='POST':
        con=mysql.connector.connect(host="localhost",user="root",passwd="vini",database="project")
        mycursor=con.cursor()
        docname1=request.POST['docname']
        docemail1=request.POST['docemail']
        docpasswd1=request.POST['docpass']
        if con.is_connected():
            try:
                sql1="select docname,docemail,docpassword,docspe,clinic,docno from appnew_doctorreg"
                mycursor.execute(sql1)
                result=mycursor.fetchall()
                for row in result:
                    if docname1 == row[0]:
                        if docemail1==row[1] and docpasswd1==row[2]:
                            content["doctor_name"]=row[0]
                            content["speciality"]=row[3]
                            content["clinic"]=row[4]
                            profile["doc_name"]=row[0]
                            profile["doc_email"]=row[1]
                            profile["doc_pass"]=row[2]
                            profile["spe"]=row[3]
                            profile["clinic"]=row[4]
                            profile["no"]=row[5]
                            messages.success(request,f"Sign In is successful")
                            messages.info(request,f"Welcome Dr.{docname1}")
                            return render(request,'DoctorPage.html',content)
                            
                        else:
                            messages.error(request,f"invalid username and password")
                            return render(request,'homepage.html')
            except:
                print("error")
            finally:
                con.close()
                
#To register a receptionist
def Recep_register(request):
    if request.method=='GET':
        return render(request,'recepregister.html')
    elif request.method=='POST':
        Recep_Name=request.POST['recepname']
        Recep_No=request.POST['recepno']
        Recep_Clinic=request.POST['recepclinic']
        Recep_Email=request.POST['recepemail']
        Recep_Passwd=request.POST['receppass']
        
        if request.GET['a']=='recepreg':
            con=mysql.connector.connect(host="localhost",user="root",passwd="vini",database="project")
            mycursor=con.cursor()
            if con.is_connected():
                try:
                    sql2="insert into appnew_recepregister values('{}','{}','{}','{}','{}')".format(Recep_Name,Recep_No,Recep_Clinic,Recep_Email,Recep_Passwd)
                    mycursor.execute(sql2)
                    con.commit()
                except:
                    print("error")
                finally:
                    con.close()
            return render(request,'homepage.html')
        else:
            return render(request,'homepage.html')

#Receptionist Login
def Recep_signin(request):
    if request.method=='GET':
        return render(request,'RecepSignIn.html')
    elif request.method=='POST':
        con=mysql.connector.connect(host="localhost",user="root",passwd="vini",database="project")
        mycursor=con.cursor()
        Recep_name1=request.POST['recepname']
        Recep_email1=request.POST['recepemail']
        Recep_passwd1=request.POST['receppass']
        if con.is_connected():
            try:
                sql3="select recepname,recepemail, receppasswd,recepclinic,recepno from appnew_recepregister"
                mycursor.execute(sql3)
                result=mycursor.fetchall()
                for row in result:
                    if Recep_name1== row[0]:
                        if Recep_email1==row[1] and Recep_passwd1==row[2]:
                            profile_recep["recep_name"]=row[0]
                            profile_recep["recep_no"]=row[4]
                            profile_recep["recep_clinic"]=row[3]
                            profile_recep["recep_email"]=row[1]
                            profile_recep["recep_passwd"]=row[2]
                            content_recep["Rep_name"]=row[0]
                            content_recep["Rep_clinic"]=row[3]
                            messages.success(request,f"Sign In is successful")
                            messages.info(request,f"Welcome Dr.{Recep_name1}")
                            return render(request,'ReceptionistPage.html',content_recep)
                            
                        else:
                            messages.error(request,f"invalid username and password")
                            return render(request,'homepage.html')
            except:
                print("error")
            finally:
                con.close()

#To view the profile of doctor
def ViewProfile(request):
    return render(request,'ViewProfile.html',profile)

#To edit the profile of doctor
def EditProfile(request):
    if request.method=='GET':
        return render(request,'EditProfile.html')
    elif request.method=='POST':
        con=mysql.connector.connect(host="localhost",user="root",passwd="vini",database="project")
        mycursor=con.cursor()
        Doc_no=request.POST['docno']
        Doc_clinic=request.POST['docclinic']
        Doc_spec=request.POST['docspe']
        Doc_email=request.POST['docemail']
        Doc_pass=request.POST['docpass']
        Doc_name=profile["doc_name"]

        if con.is_connected():
            try:
                sql4="UPDATE appnew_doctorreg set docno='{}',clinic='{}',docspe='{}',docemail='{}',docpassword='{}' where docname='{}'".format(Doc_no,Doc_clinic,Doc_spec,Doc_email,Doc_pass,Doc_name)
                mycursor.execute(sql4)
                con.commit()
                profile["doc_email"]=Doc_email
                profile["doc_pass"]=Doc_pass
                profile["spe"]=Doc_spec
                profile["clinic"]=Doc_clinic
                profile["no"]=Doc_no
                content["speciality"]=Doc_spec
                content["clinic"]=Doc_clinic
                messages.warning(request,f"Successfully changed your profile details")
                return render(request,'DoctorPage.html',content)
            except:
                print("error")
            finally:
                con.close()

#To register a patient               
def addpatient(request):
    if request.method=="GET":
        return render(request,'patregister.html')
    elif request.method=="POST":
        patname=request.POST.get("naming")
        patcontact=request.POST.get("contact")
        patemail=request.POST.get("emailid")
        patpassword=request.POST.get("passwd")
        if request.GET['a']=='regis':
            con = mysql.connector.connect(host="localhost", user="root", passwd="vini",database="project")
            mycursor = con.cursor()
            if con.is_connected():
                try:
                    sql="insert into appnew_patientdetails values('{}','{}','{}','{}')".format(patname,patcontact,patemail,patpassword)
                    mycursor.execute(sql)
                    con.commit()
                except:
                    print("error")
                finally:
                    con.close()
            messages.success(request, f"Registration is successful")
            return render(request,'homepage.html')
        else:
            return render(request,'homepage.html')

#Patient login        
def loginpat(request):
    if request.method=="GET":
        return render(request,'patlogin.html')
    elif request.method=="POST":
        con = mysql.connector.connect(host="localhost", user="root", passwd="vini", database="project")
        mycursor = con.cursor()
        emailidforlogin=request.POST.get("emailid")
        passwdforlogin=request.POST.get("passwd")
        if request.GET['a']=="sign":
            if con.is_connected():
                try:
                    sql1 = "select pateid,ppasswd from appnew_patientdetails;"
                    mycursor.execute(sql1)
                    result = mycursor.fetchall()
                    for row in result:
                        if emailidforlogin==row[0]:
                            if passwdforlogin==row[1]:
                                messages.success(request,f"Sign In is successful")
                                return render(request,'patpage.html')
                            else:
                                messages.error(request,f"invalid username and password")
                                return render(request,'homepage.html')
                except:
                    print("error!")
                finally:
                    con.close()

#To view receptionist's profile details
def ViewRecepProfile(request):
    return render(request,"RecepProfile.html",profile_recep)

#To edit receptionist's profile details
def EditRecepProfile(request):

#Logout               
def logout(request):
    if request.method=="GET":
        return render(request,'homepage.html')        


            
            
