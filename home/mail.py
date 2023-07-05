from django.core.mail import send_mail
import random

#To Send Mail
def Send_Mail(email, subject, message):
    send_mail(
        subject, 
        message,
        "Expensermessages@gmail.com",
        [email],
        fail_silently=False,
    )



#To Generate OTP
def GenerateOTP():
    otp = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(6))
    return otp