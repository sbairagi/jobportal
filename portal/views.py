from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import CreateJob, ApplyUser

# Create your views here.


def Index(request):
    if request.method == 'POST':
        name = request.POST.get('username','')
        email = request.POST.get('email','')
        usertype = request.POST.get('usertype','')
        password = request.POST.get('password','')

        try:
            if name!="" and email!="" and password !="" and usertype=="":
                user = User.objects.create_user(name, email, password)
                user.save()
        except:
            print("getting error signup is not successfull")
        if name!="" and email=="" and password !="" and usertype=="user":
            user = authenticate(request, username=name, password=password)
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return redirect('http://127.0.0.1:8000/userhome')
            else:
                # No backend authenticated the credentials
                print('unauthenticated')
        elif name!="" and email=="" and password !="" and usertype=="company":
            user = authenticate(request, username=name, password=password)
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return redirect('http://127.0.0.1:8000/companyhome')
            else:
                # No backend authenticated the credentials
                print('unauthenticated')
    return render(request, 'index.html')

from django.contrib.auth import logout
def Logout(request):
    logout(request)
    return render(request, 'index.html')

from django.contrib.auth.decorators import login_required

@login_required
def Companyhome(request):
    job_name = request.POST.get('job_name','')
    job_desc = request.POST.get('job_desc','')
    experience = request.POST.get('experience','')
    open_position = request.POST.get('open_position','')
    if job_name!='' and job_desc!="" and experience!="" and open_position!="":
        new_job = CreateJob(user=request.user ,job_name=job_name,job_desc=job_desc,experience=experience,open_position=open_position)
        new_job.save()
    print(job_name, job_desc, experience, open_position)
    return render(request, 'companyhome.html')

@login_required
def Userhome(request):
    all_jobs = CreateJob.objects.all()
    print(all_jobs)
    params = {'all_jobs': all_jobs}
    return render(request, 'userhome.html',params)


@login_required
def Viewmyjobs(request):
    all_jobs = CreateJob.objects.filter(user=request.user)
    print(all_jobs)
    params = {'all_jobs': all_jobs}
    return render(request, 'myjobs.html',params)


@login_required
def Applyjob(request, id):
    return render(request, 'applyjob.html', {'id':id})

@login_required
def SucessfullyApply(request, id):
    if request.method == 'POST':
        f = request.FILES['resume'] 
        print(f.name)
        applyUser = ApplyUser(user=request.user, job=id, resume=f)
        applyUser.save()
    return render(request, 'sucessfullyApply.html')

@login_required
def Viewallapplicant(request, id):
    data = ApplyUser.objects.filter(job=id)
    user = User.objects.filter(id=id)
    print(data, user)
    params = {'data' : data, 'user' : user}
    return render(request, 'viewallapplicant.html', params)


from django.core.mail import send_mail



@login_required
def Sucessfullyshortlistcandident(request, id):
    print(id)
    appliedjob = ApplyUser.objects.filter(id=id)
    user = User.objects.filter(username=appliedjob[0].user)
    print(appliedjob[0].user, user[0].email)
    try:
        send_mail(
        'Congratulations You are Shortlised on JobPortal',
        'Congratulations Are Shortlised for the Position of Softwere Developer',
        'sbairagipanel@gmail.com',
        [user[0].email],
        fail_silently=False,
    )
    except:
        print('could not send')
    return render(request, 'sucessfullyshortlistcandident.html')


    