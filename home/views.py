from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Expense, Code, Feedback
from django.db.models import Sum
from .mail import Send_Mail, GenerateOTP
from django.contrib import messages
from .forms import Registration
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='userlogin')
def home(request):
    co = Expense.objects.filter(user_id = request.user.id)
    info = Expense.objects.filter(user_id = request.user.id).order_by('-id')[0:10]
    sum = Expense.objects.filter(user_id = request.user.id).aggregate(Sum('amount'))
    cout = len(co)
    
    context = {'info': info, 'sum': sum, 'count':cout}
    return render(request, 'home.html', context)

@login_required(login_url='userlogin')
def data(request):
    if request.method == 'POST':
        user_id = request.user.id
        desc = request.POST['desc']
        amt = request.POST['amount']
        info = Expense(user_id = user_id, desc = desc, amount = amt)
        info.save()
    return redirect('home')


@login_required(login_url='userlogin')
def show(request, pk):
    info = Expense.objects.get(id=pk)
    return render(request, 'show.html', {'info':info})


@login_required(login_url='userlogin')
def remove(request, pk):
    info = Expense.objects.get(id=pk)
    info.delete()
    return redirect('home')

@login_required(login_url='userlogin')
def remove_statement(pk):
    info = Expense.objects.get(id=pk)
    info.delete()
    return redirect('statement')
    


def start(request):
    if request.method == 'POST':
        email1 = request.POST['email']
        print(email1)
        if email1 == "":
            messages.error(request, 'Something Went Wrong')
        else:

            otp = GenerateOTP()
            form = Code(email = email1, code = otp)
            form.save()
            subject = "Email Verification"
            message = "Verification Code \n" + otp + '\n\nRegards Team Expenser'
            try:
                Send_Mail(email1, subject, message)
                return redirect('verify')
            except:
                messages.error(request, "Something Went Wrong")
            


    return render(request, 'start.html')


def Verify(request):
    if request.method == 'POST':
        otp = request.POST['code']
        try:
            code = Code.objects.get(code = otp)
            s = reverse('regis', args=[code.code])
            return redirect(s)
        except:
            messages.error(request, 'Verification Failed..., Check Your Verification Code')
    return render(request, 'verify.html')


def regis(request, pk):
    form = Registration()
    mail = " "
    try:
        code = Code.objects.get(code = pk)
        mail = code.email
        code.delete()
    except:
        messages.error(request, "Check Your Verification Code..")
    if request.method == 'POST':
        info = Registration(request.POST)
        if info.is_valid():
            obj = info.save(commit=False)
            obj.email = mail
            obj.save()
            #Need to Change After(Important)
            return redirect('home')
        else:
            messages.error(request, 'Something Went Wrong.. Try Again')
    return render(request, 'regis.html', {'form':form, 'mail': mail})



#Login 

def UserLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Something Went Wrong... Check Your Credentials..')
    return render(request, 'login.html')


#Logout User
@login_required(login_url='userlogin')
def UserLogout(request):
    logout(request)
    return redirect('userlogin')

#statement
@login_required(login_url='userlogin')
def Statement(request):
    info = Expense.objects.filter(user_id = request.user.id)
    paginator = Paginator(info, 10)

    sum = Expense.objects.filter(user_id = request.user.id).aggregate(Sum('amount'))
    email = request.user.email

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'statement.html', {"page_obj": page_obj, 'sum':sum, 'email':email})

#Feedback
@login_required(login_url='userlogin')
def Report(request):
    if request.method == 'POST':
        mesage = request.POST.get('mesage')
        user_mail = request.user.email
        user_name = request.user.username
        
        info = Feedback(userid = request.user, message = mesage)
        info.save()

        message2 = "Hi " + user_name + "\n\n" + "Thank You for your valuable Feedback....\nWe will resolve your issue soon...\n\nTeam Expenser"

        try:
            Send_Mail(user_mail, "Thankyou for Feedback", message2)
        except:
            messages.error(request, 'Something Went Wrong')
    return render(request, 'report.html')


#Feedback Page
@login_required(login_url='userlogin')
def Feed(request):
    info = Feedback.objects.all()
    return render(request, 'feed.html', {'info':info})


#FeedV
@login_required(login_url='userlogin')
def FeedV(request, pk):
    if request.user.is_superuser:
        info = Feedback.objects.get(id=pk)
        context = {'info':info}
        return render(request, 'feedv.html', context)
    else:
        return redirect('home')