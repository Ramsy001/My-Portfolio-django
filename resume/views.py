from django.shortcuts import render,redirect
from django.http import FileResponse,HttpResponse
import smtplib
from email.message import EmailMessage
from django.core.mail import send_mail




from .models import ProfileInfo,TechStack,Projects,Experience,Ceritifications,Resume

from django.contrib.staticfiles.storage import staticfiles_storage

def home(request):
    image = ProfileInfo.objects.first()
    return render(request, 'home.html',{
        'profile': image
        })
# Create your views here.


def about(request):
    image = ProfileInfo.objects.first()
    techstack = TechStack.objects.all()
    context = {
        "techstack": techstack,
        "image": image
    }
    return render(request,"about.html",context)

def projects(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects
    }
    return render(request,'projects.html',context)

def experience(request):
    Experiences = Experience.objects.all()
    context = {
        'Experiences': Experiences
    }
    return render(request,'experience.html', context)

def certifications(request):
    certifications = Ceritifications.objects.all()
    context = {
        'certifications': certifications
    }
    return render(request,'certifications.html',context)

def contacts(request):
    if request.method == 'GET':
        return render(request,'Contacts.html')
    if request.method == 'POST':
        # print(request.POST)
        # msg = EmailMessage()
        # msg.set_content(f'''
        #   name: {request.POST.get('name')} 
        #   no: {request.POST.get('phone')} 
        #   email : {request.POST.get('email')}
        #   message: "{request.POST.get('mes')}"''')
        # msg['Subject'] = 'Portfolio contact '
        # msg['From'] = 'mwaleramsy@gmail.com'
        # msg['To'] = 'bett3304@gmail.com'

        msg = f'''
          name: {request.POST.get('name')} 
          no: {request.POST.get('phone')} 
          email : {request.POST.get('email')}
          message: "{request.POST.get('mes')}"'''

        # s = smtplib.SMTP('smtp.sendgrid.com')
     
        # s.send_message(msg)
        # s.quit()
        with smtplib.SMTP('smtp.gmail.com', 587) as server:            
            server.ehlo()
            server.starttls()
            server.login('mwaleramsy0@gmail.com', 'sjfn pnoe yvye cmcw')  
            server.sendmail('mwaleramsy@gmail0.com', 'mwaleramsy@gmail.com',msg )  
        return redirect('/')
      


def resume(request):
    file_path = Resume.objects.first().resume.path    
    with open(file_path,'rb') as file_obj:    
        response = HttpResponse(file_obj.read(),content_type='application/pdf')
        response['Content-Disposition']='attachment; filename="resume.pdf"'
        return response

def certificate(request,pk):
    file_path = f'{Ceritifications.objects.get(id=pk).file.path}'   
    with open(file_path,'rb') as file_obj:    
        response = HttpResponse(file_obj.read(),content_type='application/pdf')
        response['Content-Disposition']=f'attachment; filename="ramsymwale-{Ceritifications.objects.get(id=pk).name}.pdf"'
        return response