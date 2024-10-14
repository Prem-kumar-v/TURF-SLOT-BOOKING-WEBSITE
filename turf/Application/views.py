from django.shortcuts import render,redirect
from .models import *
from datetime import date
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    return render(request,"index.html")

def loginpage(request):
    if request.method=='POST':
        mail=request.POST["uemail"]
        pwd=request.POST["upwd"]
        data=turfuser.objects.filter(umail=mail,password=pwd)
        
        
        if data:
            for datas in data:
                user_id=datas.id
                user_name=datas.username
            
            
            return redirect("Userdetails",id=user_id,uname=user_name)
            
            
    return render(request,"login.html")

def userdetails(request,id,uname):
    slotinfo=booking.objects.filter(turfuser_id=id)
    userinfo=turfuser.objects.get(id=id)
    mail= userinfo.umail
    return render(request,"user.html",{'slotdata':slotinfo,'uname':uname,'uid':id,'umail':mail,'today':date.today()})

def registerpage(request):
    
    if request.method=='POST':
        
        uname = request.POST["uname"]
        upass = request.POST["upass"]
        uaddr = request.POST["uaddr"]
        ucont = request.POST["ucontact"]
        uemail = request.POST["umail"]
        
        new_user = turfuser(username=uname,password=upass,ucontact=ucont,umail=uemail,uaddress=uaddr)
        new_user.save()
        
        
        settings.EMAIL_HOST_USER = 'sportsclub3115@gmail.com'
        settings.EMAIL_HOST_PASSWORD = 'lkbq ewpe spbz qsya'
        send_mail("Confirmation Mail","You have Registered successfully" + " " + uname ,settings.EMAIL_HOST_USER ,[uemail])
        return redirect("login")
    
    
    return render(request,"register.html")

def contactpage(request):
    return render(request,"contactus.html")

def slotbooking(request,id):
    return render(request,"allsports.html",{'id':id})

def deleteslot(request,id,date,time,sport,mail):
    
    udata=turfuser.objects.get(id=id)
    data = booking.objects.filter(bdate=date,btime=time,sport=sport)
    data.delete()
    
    settings.EMAIL_HOST_USER = 'sportsclub3115@gmail.com'
    settings.EMAIL_HOST_PASSWORD = 'lkbq ewpe spbz qsya'
    send_mail("Sportz club","Your Slot for " + sport + " on " + date + " at " + time + " has been cancelled successfully",settings.EMAIL_HOST_USER ,[mail])
    
    if time =="05:00 AM - 06:00 AM" and sport == 'cricket':
        
            Cricket.objects.filter(tdate=date).update(FIVEAM="green")
            Cricket1.objects.filter(tdate=date).update(FIVEAM="show")
        
    elif time =="06:00 AM - 07:00 AM" and sport == 'cricket':
        
        Cricket.objects.filter(tdate=date).update(SIXAM="green")
        Cricket1.objects.filter(tdate=date).update(SIXAM="show")
        
    elif time =="07:00 AM - 08:00 AM" and sport == 'cricket':
        
        Cricket.objects.filter(tdate=date).update(SEVENAM="green")
        Cricket1.objects.filter(tdate=date).update(SEVENAM="show")
        
    elif time =="08:00 AM - 09:00 AM" and sport == 'cricket':
        
        Cricket.objects.filter(tdate=date).update(EIGHTAM="green")
        Cricket1.objects.filter(tdate=date).update(EIGHTAM="show")
        
    elif time =="09:00 AM - 10:00 AM" and sport == 'cricket':
        
        Cricket.objects.filter(tdate=date).update(NINEAM="green")
        Cricket1.objects.filter(tdate=date).update(NINEAM="show")
        
    elif time =="10:00 AM - 11:00 AM" and sport == 'cricket':
        
        Cricket.objects.filter(tdate=date).update(TENAM="green")
        Cricket1.objects.filter(tdate=date).update(TENAM="show")
        
    elif time =="11:00 AM - 12:00 PM" and sport == 'cricket':
        
        Cricket.objects.filter(tdate=date).update(ELEAM="green")
        Cricket1.objects.filter(tdate=date).update(ELEAM="show")
        
    elif time =="12:00 PM - 01:00 PM" and sport == 'cricket':
        
        Cricket.objects.filter(tdate=date).update(TWEPM="green")
        Cricket1.objects.filter(tdate=date).update(TWEPM="show")
        
    elif time =="01:00 PM - 02:00 PM" and sport == 'cricket':
        
        Cricket.objects.filter(tdate=date).update(ONEPM="green")
        Cricket1.objects.filter(tdate=date).update(ONEPM="show")
        
    elif time =="02:00 PM - 03:00 PM" and sport == 'cricket':
        
        Cricket.objects.filter(tdate=date).update(TWOPM="green")
        Cricket1.objects.filter(tdate=date).update(TWOPM="show")
        
    elif time =="03:00 PM - 04:00 PM" and sport == 'cricket':
        
        Cricket.objects.filter(tdate=date).update(THREEPM="green")
        Cricket1.objects.filter(tdate=date).update(THREEPM="show")
    
    elif time =="04:00 PM - 05:00 PM" and sport == 'cricket':
        
        Cricket.objects.filter(tdate=date).update(FOURPM="green")
        Cricket1.objects.filter(tdate=date).update(FOURPM="show")
        
    elif time =="05:00 PM - 06:00 PM" and sport == 'cricket':
        
        Cricket.objects.filter(tdate=date).update(FIVEPM="green")
        Cricket1.objects.filter(tdate=date).update(FIVEPM="show")
        
    elif time =="06:00 PM - 07:00 PM" and sport == 'cricket':
        
        Cricket.objects.filter(tdate=date).update(SIXPM="green")
        Cricket1.objects.filter(tdate=date).update(SIXPM="show")
        
    elif time =="07:00 PM - 08:00 PM" and sport == 'cricket':
        
        Cricket.objects.filter(tdate=date).update(SEVENPM="green")
        Cricket1.objects.filter(tdate=date).update(SEVENPM="show")
        
    elif time =="08:00 PM - 09:00 PM" and sport == 'cricket':
        
        Cricket.objects.filter(tdate=date).update(EIGHTPM="green")
        Cricket1.objects.filter(tdate=date).update(EIGHTPM="show")
        
    elif time =="09:00 PM - 10:00 PM" and sport == 'cricket':
        
        Cricket.objects.filter(tdate=date).update(NINEPM="green")
        Cricket1.objects.filter(tdate=date).update(NINEPM="show")
        
    elif time =="10:00 PM - 11:00 PM" and sport == 'cricket':
        Cricket.objects.filter(tdate=date).update(TENPM="green")
        Cricket1.objects.filter(tdate=date).update(TENPM="show")
        
        
    #football delete
    
    elif time =="05:00 AM - 06:00 AM" and sport == 'football':
        
            football.objects.filter(tdate=date).update(FIVEAM="green")
            football1.objects.filter(tdate=date).update(FIVEAM="show")
        
    elif time =="06:00 AM - 07:00 AM" and sport == 'football':
        
        football.objects.filter(tdate=date).update(SIXAM="green")
        football1.objects.filter(tdate=date).update(SIXAM="show")
        
    elif time =="07:00 AM - 08:00 AM" and sport == 'football':
        
        football.objects.filter(tdate=date).update(SEVENAM="green")
        football1.objects.filter(tdate=date).update(SEVENAM="show")
        
    elif time =="08:00 AM - 09:00 AM" and sport == 'football':
        
        football.objects.filter(tdate=date).update(EIGHTAM="green")
        football1.objects.filter(tdate=date).update(EIGHTAM="show")
        
    elif time =="09:00 AM - 10:00 AM" and sport == 'football':
        
        football.objects.filter(tdate=date).update(NINEAM="green")
        football1.objects.filter(tdate=date).update(NINEAM="show")
        
    elif time =="10:00 AM - 11:00 AM" and sport == 'football':
        
        football.objects.filter(tdate=date).update(TENAM="green")
        football1.objects.filter(tdate=date).update(TENAM="show")
        
    elif time =="11:00 AM - 12:00 PM" and sport == 'football':
        
        football.objects.filter(tdate=date).update(ELEAM="green")
        football1.objects.filter(tdate=date).update(ELEAM="show")
        
    elif time =="12:00 PM - 01:00 PM" and sport == 'football':
        
        football.objects.filter(tdate=date).update(TWEPM="green")
        football1.objects.filter(tdate=date).update(TWEPM="show")
        
    elif time =="01:00 PM - 02:00 PM" and sport == 'football':
        
        football.objects.filter(tdate=date).update(ONEPM="green")
        football1.objects.filter(tdate=date).update(ONEPM="show")
        
    elif time =="02:00 PM - 03:00 PM" and sport == 'football':
        
        football.objects.filter(tdate=date).update(TWOPM="green")
        football1.objects.filter(tdate=date).update(TWOPM="show")
        
    elif time =="03:00 PM - 04:00 PM" and sport == 'football':
        
        football.objects.filter(tdate=date).update(THREEPM="green")
        football1.objects.filter(tdate=date).update(THREEPM="show")
    
    elif time =="04:00 PM - 05:00 PM" and sport == 'football':
        
        football.objects.filter(tdate=date).update(FOURPM="green")
        football1.objects.filter(tdate=date).update(FOURPM="show")
        
    elif time =="05:00 PM - 06:00 PM" and sport == 'football':
        
        football.objects.filter(tdate=date).update(FIVEPM="green")
        football1.objects.filter(tdate=date).update(FIVEPM="show")
        
    elif time =="06:00 PM - 07:00 PM" and sport == 'football':
        
        football.objects.filter(tdate=date).update(SIXPM="green")
        football1.objects.filter(tdate=date).update(SIXPM="show")
        
    elif time =="07:00 PM - 08:00 PM" and sport == 'football':
        
        football.objects.filter(tdate=date).update(SEVENPM="green")
        football1.objects.filter(tdate=date).update(SEVENPM="show")
        
    elif time =="08:00 PM - 09:00 PM" and sport == 'football':
        
        football.objects.filter(tdate=date).update(EIGHTPM="green")
        football1.objects.filter(tdate=date).update(EIGHTPM="show")
        
    elif time =="09:00 PM - 10:00 PM" and sport == 'football':
        
        football.objects.filter(tdate=date).update(NINEPM="green")
        football1.objects.filter(tdate=date).update(NINEPM="show")
        
    elif time =="10:00 PM - 11:00 PM" and sport == 'football':
        football.objects.filter(tdate=date).update(TENPM="green")
        football1.objects.filter(tdate=date).update(TENPM="show")
        
    #basketball
    
    elif time =="05:00 AM - 06:00 AM" and sport == 'basketball':
        
            basketball.objects.filter(tdate=date).update(FIVEAM="green")
            basketball1.objects.filter(tdate=date).update(FIVEAM="show")
        
    elif time =="06:00 AM - 07:00 AM" and sport == 'basketball':
        
        basketball.objects.filter(tdate=date).update(SIXAM="green")
        basketball1.objects.filter(tdate=date).update(SIXAM="show")
        
    elif time =="07:00 AM - 08:00 AM" and sport == 'basketball':
        
        basketball.objects.filter(tdate=date).update(SEVENAM="green")
        basketball1.objects.filter(tdate=date).update(SEVENAM="show")
        
    elif time =="08:00 AM - 09:00 AM" and sport == 'basketball':
        
        basketball.objects.filter(tdate=date).update(EIGHTAM="green")
        basketball1.objects.filter(tdate=date).update(EIGHTAM="show")
        
    elif time =="09:00 AM - 10:00 AM" and sport == 'basketball':
        
        basketball.objects.filter(tdate=date).update(NINEAM="green")
        basketball1.objects.filter(tdate=date).update(NINEAM="show")
        
    elif time =="10:00 AM - 11:00 AM" and sport == 'basketball':
        
        basketball.objects.filter(tdate=date).update(TENAM="green")
        basketball1.objects.filter(tdate=date).update(TENAM="show")
        
    elif time =="11:00 AM - 12:00 PM" and sport == 'basketball':
        
        basketball.objects.filter(tdate=date).update(ELEAM="green")
        basketball1.objects.filter(tdate=date).update(ELEAM="show")
        
    elif time =="12:00 PM - 01:00 PM" and sport == 'basketball':
        
        basketball.objects.filter(tdate=date).update(TWEPM="green")
        basketball1.objects.filter(tdate=date).update(TWEPM="show")
        
    elif time =="01:00 PM - 02:00 PM" and sport == 'basketball':
        
        basketball.objects.filter(tdate=date).update(ONEPM="green")
        basketball1.objects.filter(tdate=date).update(ONEPM="show")
        
    elif time =="02:00 PM - 03:00 PM" and sport == 'basketball':
        
        basketball.objects.filter(tdate=date).update(TWOPM="green")
        basketball1.objects.filter(tdate=date).update(TWOPM="show")
        
    elif time =="03:00 PM - 04:00 PM" and sport == 'basketball':
        
        basketball.objects.filter(tdate=date).update(THREEPM="green")
        basketball1.objects.filter(tdate=date).update(THREEPM="show")
    
    elif time =="04:00 PM - 05:00 PM" and sport == 'basketball':
        
        basketball.objects.filter(tdate=date).update(FOURPM="green")
        basketball1.objects.filter(tdate=date).update(FOURPM="show")
        
    elif time =="05:00 PM - 06:00 PM" and sport == 'basketball':
        
        basketball.objects.filter(tdate=date).update(FIVEPM="green")
        basketball1.objects.filter(tdate=date).update(FIVEPM="show")
        
    elif time =="06:00 PM - 07:00 PM" and sport == 'basketball':
        
        basketball.objects.filter(tdate=date).update(SIXPM="green")
        basketball1.objects.filter(tdate=date).update(SIXPM="show")
        
    elif time =="07:00 PM - 08:00 PM" and sport == 'basketball':
        
        basketball.objects.filter(tdate=date).update(SEVENPM="green")
        basketball1.objects.filter(tdate=date).update(SEVENPM="show")
        
    elif time =="08:00 PM - 09:00 PM" and sport == 'basketball':
        
        basketball.objects.filter(tdate=date).update(EIGHTPM="green")
        basketball1.objects.filter(tdate=date).update(EIGHTPM="show")
        
    elif time =="09:00 PM - 10:00 PM" and sport == 'basketball':
        
        basketball.objects.filter(tdate=date).update(NINEPM="green")
        basketball1.objects.filter(tdate=date).update(NINEPM="show")
        
    elif time =="10:00 PM - 11:00 PM" and sport == 'basketball':
        basketball.objects.filter(tdate=date).update(TENPM="green")
        basketball1.objects.filter(tdate=date).update(TENPM="show")
        
    #volleyball
    elif time =="05:00 AM - 06:00 AM" and sport == 'volleyball':
        
            volleyball.objects.filter(tdate=date).update(FIVEAM="green")
            volleyball1.objects.filter(tdate=date).update(FIVEAM="show")
        
    elif time =="06:00 AM - 07:00 AM" and sport == 'volleyball':
        
        volleyball.objects.filter(tdate=date).update(SIXAM="green")
        volleyball1.objects.filter(tdate=date).update(SIXAM="show")
        
    elif time =="07:00 AM - 08:00 AM" and sport == 'volleyball':
        
        volleyball.objects.filter(tdate=date).update(SEVENAM="green")
        volleyball1.objects.filter(tdate=date).update(SEVENAM="show")
        
    elif time =="08:00 AM - 09:00 AM" and sport == 'volleyball':
        
        volleyball.objects.filter(tdate=date).update(EIGHTAM="green")
        volleyball1.objects.filter(tdate=date).update(EIGHTAM="show")
        
    elif time =="09:00 AM - 10:00 AM" and sport == 'volleyball':
        
        volleyball.objects.filter(tdate=date).update(NINEAM="green")
        volleyball1.objects.filter(tdate=date).update(NINEAM="show")
        
    elif time =="10:00 AM - 11:00 AM" and sport == 'volleyball':
        
        volleyball.objects.filter(tdate=date).update(TENAM="green")
        volleyball1.objects.filter(tdate=date).update(TENAM="show")
        
    elif time =="11:00 AM - 12:00 PM" and sport == 'volleyball':
        
        volleyball.objects.filter(tdate=date).update(ELEAM="green")
        volleyball1.objects.filter(tdate=date).update(ELEAM="show")
        
    elif time =="12:00 PM - 01:00 PM" and sport == 'volleyball':
        
        volleyball.objects.filter(tdate=date).update(TWEPM="green")
        volleyball1.objects.filter(tdate=date).update(TWEPM="show")
        
    elif time =="01:00 PM - 02:00 PM" and sport == 'volleyball':
        
        volleyball.objects.filter(tdate=date).update(ONEPM="green")
        volleyball1.objects.filter(tdate=date).update(ONEPM="show")
        
    elif time =="02:00 PM - 03:00 PM" and sport == 'volleyball':
        
        volleyball.objects.filter(tdate=date).update(TWOPM="green")
        volleyball1.objects.filter(tdate=date).update(TWOPM="show")
        
    elif time =="03:00 PM - 04:00 PM" and sport == 'volleyball':
        
        volleyball.objects.filter(tdate=date).update(THREEPM="green")
        volleyball1.objects.filter(tdate=date).update(THREEPM="show")
    
    elif time =="04:00 PM - 05:00 PM" and sport == 'volleyball':
        
        volleyball.objects.filter(tdate=date).update(FOURPM="green")
        volleyball1.objects.filter(tdate=date).update(FOURPM="show")
        
    elif time =="05:00 PM - 06:00 PM" and sport == 'volleyball':
        
        volleyball.objects.filter(tdate=date).update(FIVEPM="green")
        volleyball1.objects.filter(tdate=date).update(FIVEPM="show")
        
    elif time =="06:00 PM - 07:00 PM" and sport == 'volleyball':
        
        volleyball.objects.filter(tdate=date).update(SIXPM="green")
        volleyball1.objects.filter(tdate=date).update(SIXPM="show")
        
    elif time =="07:00 PM - 08:00 PM" and sport == 'volleyball':
        
        volleyball.objects.filter(tdate=date).update(SEVENPM="green")
        volleyball1.objects.filter(tdate=date).update(SEVENPM="show")
        
    elif time =="08:00 PM - 09:00 PM" and sport == 'volleyball':
        
        volleyball.objects.filter(tdate=date).update(EIGHTPM="green")
        volleyball1.objects.filter(tdate=date).update(EIGHTPM="show")
        
    elif time =="09:00 PM - 10:00 PM" and sport == 'volleyball':
        
        volleyball.objects.filter(tdate=date).update(NINEPM="green")
        volleyball1.objects.filter(tdate=date).update(NINEPM="show")
        
    elif time =="10:00 PM - 11:00 PM" and sport == 'volleyball':
        volleyball.objects.filter(tdate=date).update(TENPM="green")
        volleyball1.objects.filter(tdate=date).update(TENPM="show")
        
    #handball
    
    elif time =="05:00 AM - 06:00 AM" and sport == 'handball':
        
            handball.objects.filter(tdate=date).update(FIVEAM="green")
            handball1.objects.filter(tdate=date).update(FIVEAM="show")
        
    elif time =="06:00 AM - 07:00 AM" and sport == 'handball':
        
        handball.objects.filter(tdate=date).update(SIXAM="green")
        handball1.objects.filter(tdate=date).update(SIXAM="show")
        
    elif time =="07:00 AM - 08:00 AM" and sport == 'handball':
        
        handball.objects.filter(tdate=date).update(SEVENAM="green")
        handball1.objects.filter(tdate=date).update(SEVENAM="show")
        
    elif time =="08:00 AM - 09:00 AM" and sport == 'handball':
        
        handball.objects.filter(tdate=date).update(EIGHTAM="green")
        handball1.objects.filter(tdate=date).update(EIGHTAM="show")
        
    elif time =="09:00 AM - 10:00 AM" and sport == 'handball':
        
        handball.objects.filter(tdate=date).update(NINEAM="green")
        handball1.objects.filter(tdate=date).update(NINEAM="show")
        
    elif time =="10:00 AM - 11:00 AM" and sport == 'handball':
        
        handball.objects.filter(tdate=date).update(TENAM="green")
        handball1.objects.filter(tdate=date).update(TENAM="show")
        
    elif time =="11:00 AM - 12:00 PM" and sport == 'handball':
        
        handball.objects.filter(tdate=date).update(ELEAM="green")
        handball1.objects.filter(tdate=date).update(ELEAM="show")
        
    elif time =="12:00 PM - 01:00 PM" and sport == 'handball':
        
        handball.objects.filter(tdate=date).update(TWEPM="green")
        handball1.objects.filter(tdate=date).update(TWEPM="show")
        
    elif time =="01:00 PM - 02:00 PM" and sport == 'handball':
        
        handball.objects.filter(tdate=date).update(ONEPM="green")
        handball1.objects.filter(tdate=date).update(ONEPM="show")
        
    elif time =="02:00 PM - 03:00 PM" and sport == 'handball':
        
        handball.objects.filter(tdate=date).update(TWOPM="green")
        handball1.objects.filter(tdate=date).update(TWOPM="show")
        
    elif time =="03:00 PM - 04:00 PM" and sport == 'handball':
        
        handball.objects.filter(tdate=date).update(THREEPM="green")
        handball1.objects.filter(tdate=date).update(THREEPM="show")
    
    elif time =="04:00 PM - 05:00 PM" and sport == 'handball':
        
        handball.objects.filter(tdate=date).update(FOURPM="green")
        handball1.objects.filter(tdate=date).update(FOURPM="show")
        
    elif time =="05:00 PM - 06:00 PM" and sport == 'handball':
        
        handball.objects.filter(tdate=date).update(FIVEPM="green")
        handball1.objects.filter(tdate=date).update(FIVEPM="show")
        
    elif time =="06:00 PM - 07:00 PM" and sport == 'handball':
        
        handball.objects.filter(tdate=date).update(SIXPM="green")
        handball1.objects.filter(tdate=date).update(SIXPM="show")
        
    elif time =="07:00 PM - 08:00 PM" and sport == 'handball':
        
        handball.objects.filter(tdate=date).update(SEVENPM="green")
        handball1.objects.filter(tdate=date).update(SEVENPM="show")
        
    elif time =="08:00 PM - 09:00 PM" and sport == 'handball':
        
        handball.objects.filter(tdate=date).update(EIGHTPM="green")
        handball1.objects.filter(tdate=date).update(EIGHTPM="show")
        
    elif time =="09:00 PM - 10:00 PM" and sport == 'handball':
        
        handball.objects.filter(tdate=date).update(NINEPM="green")
        handball1.objects.filter(tdate=date).update(NINEPM="show")
        
    elif time =="10:00 PM - 11:00 PM" and sport == 'handball':
        handball.objects.filter(tdate=date).update(TENPM="green")
        handball1.objects.filter(tdate=date).update(TENPM="show")
        
    #kabaddi
    elif time =="05:00 AM - 06:00 AM" and sport == 'kabaddi':
        
            kabaddi.objects.filter(tdate=date).update(FIVEAM="green")
            kabaddi1.objects.filter(tdate=date).update(FIVEAM="show")
        
    elif time =="06:00 AM - 07:00 AM" and sport == 'kabaddi':
        
        kabaddi.objects.filter(tdate=date).update(SIXAM="green")
        kabaddi1.objects.filter(tdate=date).update(SIXAM="show")
        
    elif time =="07:00 AM - 08:00 AM" and sport == 'kabaddi':
        
        kabaddi.objects.filter(tdate=date).update(SEVENAM="green")
        kabaddi1.objects.filter(tdate=date).update(SEVENAM="show")
        
    elif time =="08:00 AM - 09:00 AM" and sport == 'kabaddi':
        
        kabaddi.objects.filter(tdate=date).update(EIGHTAM="green")
        kabaddi1.objects.filter(tdate=date).update(EIGHTAM="show")
        
    elif time =="09:00 AM - 10:00 AM" and sport == 'kabaddi':
        
        kabaddi.objects.filter(tdate=date).update(NINEAM="green")
        kabaddi1.objects.filter(tdate=date).update(NINEAM="show")
        
    elif time =="10:00 AM - 11:00 AM" and sport == 'kabaddi':
        
        kabaddi.objects.filter(tdate=date).update(TENAM="green")
        kabaddi1.objects.filter(tdate=date).update(TENAM="show")
        
    elif time =="11:00 AM - 12:00 PM" and sport == 'kabaddi':
        
        kabaddi.objects.filter(tdate=date).update(ELEAM="green")
        kabaddi1.objects.filter(tdate=date).update(ELEAM="show")
        
    elif time =="12:00 PM - 01:00 PM" and sport == 'kabaddi':
        
        kabaddi.objects.filter(tdate=date).update(TWEPM="green")
        kabaddi1.objects.filter(tdate=date).update(TWEPM="show")
        
    elif time =="01:00 PM - 02:00 PM" and sport == 'kabaddi':
        
        kabaddi.objects.filter(tdate=date).update(ONEPM="green")
        kabaddi1.objects.filter(tdate=date).update(ONEPM="show")
        
    elif time =="02:00 PM - 03:00 PM" and sport == 'kabaddi':
        
        kabaddi.objects.filter(tdate=date).update(TWOPM="green")
        kabaddi.objects.filter(tdate=date).update(TWOPM="show")
        
    elif time =="03:00 PM - 04:00 PM" and sport == 'kabaddi':
        
        kabaddi.objects.filter(tdate=date).update(THREEPM="green")
        kabaddi1.objects.filter(tdate=date).update(THREEPM="show")
    
    elif time =="04:00 PM - 05:00 PM" and sport == 'kabaddi':
        
        kabaddi.objects.filter(tdate=date).update(FOURPM="green")
        kabaddi1.objects.filter(tdate=date).update(FOURPM="show")
        
    elif time =="05:00 PM - 06:00 PM" and sport == 'kabaddi':
        
        kabaddi.objects.filter(tdate=date).update(FIVEPM="green")
        kabaddi1.objects.filter(tdate=date).update(FIVEPM="show")
        
    elif time =="06:00 PM - 07:00 PM" and sport == 'kabaddi':
        
        kabaddi.objects.filter(tdate=date).update(SIXPM="green")
        kabaddi1.objects.filter(tdate=date).update(SIXPM="show")
        
    elif time =="07:00 PM - 08:00 PM" and sport == 'kabaddi':
        
        kabaddi.objects.filter(tdate=date).update(SEVENPM="green")
        kabaddi1.objects.filter(tdate=date).update(SEVENPM="show")
        
    elif time =="08:00 PM - 09:00 PM" and sport == 'kabaddi':
        
        kabaddi.objects.filter(tdate=date).update(EIGHTPM="green")
        kabaddi1.objects.filter(tdate=date).update(EIGHTPM="show")
        
    elif time =="09:00 PM - 10:00 PM" and sport == 'kabaddi':
        
        kabaddi.objects.filter(tdate=date).update(NINEPM="green")
        kabaddi1.objects.filter(tdate=date).update(NINEPM="show")
        
    elif time =="10:00 PM - 11:00 PM" and sport == 'kabaddi':
        kabaddi.objects.filter(tdate=date).update(TENPM="green")
        kabaddi1.objects.filter(tdate=date).update(TENPM="show")
      
    return redirect("Userdetails",id=id,uname=udata.username)


def cricketview(request,id):
    
    if request.method=='POST':
            cdate=request.POST["demo"]
            slotinfo=Cricket.objects.get(tdate=cdate)
            dateinfo=Cricket1.objects.get(tdate=cdate)
            userinfo=turfuser.objects.get(id=id)
            uname = userinfo.username
            return render(request,"cricket.html",{'id':id,'datas':slotinfo,'values':dateinfo,'seldate':cdate,'uname':uname})
    
    info = Cricket.objects.get(tdate=date.today())
    info1 = Cricket1.objects.get(tdate=date.today())
    userinfo=turfuser.objects.get(id=id)
    uname = userinfo.username
    
    #return render(request,"user.html",{'userdata':userinfo,'uname':uname,'uid':id,'today':date.today()})
    
    return render(request,"cricket.html",{'id':id,'datas':info,'values':info1,'uname':uname})


def Cricketbook(request):
    
    
     if request.method == 'POST':
        bid=int(request.POST["bid"])
        bdate=request.POST["bdate"]
        btime=request.POST["btime"]
        sport=request.POST["sport"]
        amount=request.POST["amt"]
        
        new_data = booking(bdate=bdate,btime=btime,sport=sport,amount=amount,turfuser_id=bid)
        user = turfuser.objects.get(id=bid)
        mail=user.umail
        new_data.save()
        settings.EMAIL_HOST_USER = 'sportsclub3115@gmail.com'
        settings.EMAIL_HOST_PASSWORD = 'lkbq ewpe spbz qsya'
        send_mail("Sportz club","Your Slot for cricket "  + " on " + bdate + " at " + btime + " has been booked successfully",settings.EMAIL_HOST_USER ,[mail])
        
        if btime == "05:00 AM - 06:00 AM":
            Cricket.objects.filter(tdate=bdate).update(FIVEAM="red")
            Cricket1.objects.filter(tdate=bdate).update(FIVEAM="hide")
        
        elif btime == "06:00 AM - 07:00 AM":
            Cricket.objects.filter(tdate=bdate).update(SIXAM="red")
            Cricket1.objects.filter(tdate=bdate).update(SIXAM="hide")
            
        elif btime == "07:00 AM - 08:00 AM":
            Cricket.objects.filter(tdate=bdate).update(SEVENAM="red")
            Cricket1.objects.filter(tdate=bdate).update(SEVENAM="hide")
            
        elif btime == "08:00 AM - 09:00 AM":
            Cricket.objects.filter(tdate=bdate).update(EIGHTAM="red")
            Cricket1.objects.filter(tdate=bdate).update(EIGHTAM="hide")
            
        elif btime == "09:00 AM - 10:00 AM":
            Cricket.objects.filter(tdate=bdate).update(NINEAM="red")
            Cricket1.objects.filter(tdate=bdate).update(NINEAM="hide")
            
        elif btime == "10:00 AM - 11:00 AM":
            Cricket.objects.filter(tdate=bdate).update(TENAM="red")
            Cricket1.objects.filter(tdate=bdate).update(TENAM="hide")
            
        elif btime == "11:00 AM - 12:00 PM":
            Cricket.objects.filter(tdate=bdate).update(ELEAM="red")
            Cricket1.objects.filter(tdate=bdate).update(ELEAM="hide")
            
        elif btime == "12:00 PM - 01:00 PM":
            Cricket.objects.filter(tdate=bdate).update(TWEPM="red")
            Cricket1.objects.filter(tdate=bdate).update(TWEPM="hide")
            
        elif btime == "01:00 PM - 02:00 PM":
            Cricket.objects.filter(tdate=bdate).update(ONEPM="red")
            Cricket1.objects.filter(tdate=bdate).update(ONEPM="hide")
            
        elif btime == "02:00 PM - 03:00 PM":
            Cricket.objects.filter(tdate=bdate).update(TWOPM="red")
            Cricket1.objects.filter(tdate=bdate).update(TWOPM="hide")
            
        elif btime == "03:00 PM - 04:00 PM":
            Cricket.objects.filter(tdate=bdate).update(THREEPM="red")
            Cricket1.objects.filter(tdate=bdate).update(THREEPM="hide")
            
        elif btime == "04:00 PM - 05:00 PM":
            Cricket.objects.filter(tdate=bdate).update(FOURPM="red")
            Cricket1.objects.filter(tdate=bdate).update(FOURPM="hide")
            
        elif btime == "05:00 PM - 06:00 PM":
            Cricket.objects.filter(tdate=bdate).update(FIVEPM="red")
            Cricket1.objects.filter(tdate=bdate).update(FIVEPM="hide")
            
        elif btime == "06:00 PM - 07:00 PM":
            Cricket.objects.filter(tdate=bdate).update(SIXPM="red")
            Cricket1.objects.filter(tdate=bdate).update(SIXPM="hide")
            
        elif btime == "07:00 PM - 08:00 PM":
            Cricket.objects.filter(tdate=bdate).update(SEVENPM="red")
            Cricket1.objects.filter(tdate=bdate).update(SEVENPM="hide")
            
        elif btime == "08:00 PM - 09:00 PM":
            Cricket.objects.filter(tdate=bdate).update(EIGHTPM="red")
            Cricket1.objects.filter(tdate=bdate).update(EIGHTPM="hide")
            
        elif btime == "09:00 PM - 10:00 PM":
            Cricket.objects.filter(tdate=bdate).update(NINEPM="red")
            Cricket1.objects.filter(tdate=bdate).update(NINEPM="hide")
            
        else:
            Cricket.objects.filter(tdate=bdate).update(TENPM="red")
            Cricket1.objects.filter(tdate=bdate).update(TENPM="hide")
            
        return redirect("Cricket",id=bid)
    
   
      
            


def footballview(request,id):
    
    if request.method=='POST':
            cdate=request.POST["demo"]
            slotinfo=football.objects.get(tdate=cdate)
            dateinfo=football1.objects.get(tdate=cdate)
            return render(request,"football.html",{'id':id,'datas':slotinfo,'values':dateinfo,'seldate':cdate})
    
    info = football.objects.get(tdate=date.today())
    info1 = football1.objects.get(tdate=date.today())
    userinfo=turfuser.objects.get(id=id)
    uname = userinfo.username
    
    return render(request,"football.html",{'id':id,'datas':info,'values':info1,'uname':uname})

def footballbook(request):
    
    
     if request.method == 'POST':
        bid=int(request.POST["bid"])
        bdate=request.POST["bdate"]
        btime=request.POST["btime"]
        sport=request.POST["sport"]
        amount=request.POST["amt"]
        
        new_data = booking(bdate=bdate,btime=btime,sport=sport,amount=amount,turfuser_id=bid)
        new_data.save()
        data = turfuser.objects.get(id=bid)
        mail = data.umail
        settings.EMAIL_HOST_USER = 'sportsclub3115@gmail.com'
        settings.EMAIL_HOST_PASSWORD = 'lkbq ewpe spbz qsya'
        send_mail("Sportz club","Your Slot for Football "  + " on " + bdate + " at " + btime + " has been booked successfully",settings.EMAIL_HOST_USER ,[mail])
        
        if btime == "05:00 AM - 06:00 AM":
            football.objects.filter(tdate=bdate).update(FIVEAM="red")
            football1.objects.filter(tdate=bdate).update(FIVEAM="hide")
        
        elif btime == "06:00 AM - 07:00 AM":
            football.objects.filter(tdate=bdate).update(SIXAM="red")
            football1.objects.filter(tdate=bdate).update(SIXAM="hide")
            
        elif btime == "07:00 AM - 08:00 AM":
            football.objects.filter(tdate=bdate).update(SEVENAM="red")
            football1.objects.filter(tdate=bdate).update(SEVENAM="hide")
            
        elif btime == "08:00 AM - 09:00 AM":
            football.objects.filter(tdate=bdate).update(EIGHTAM="red")
            football1.objects.filter(tdate=bdate).update(EIGHTAM="hide")
            
        elif btime == "09:00 AM - 10:00 AM":
            football.objects.filter(tdate=bdate).update(NINEAM="red")
            football1.objects.filter(tdate=bdate).update(NINEAM="hide")
            
        elif btime == "10:00 AM - 11:00 AM":
            football.objects.filter(tdate=bdate).update(TENAM="red")
            football1.objects.filter(tdate=bdate).update(TENAM="hide")
            
        elif btime == "11:00 AM - 12:00 PM":
            football.objects.filter(tdate=bdate).update(ELEAM="red")
            football1.objects.filter(tdate=bdate).update(ELEAM="hide")
            
        elif btime == "12:00 PM - 01:00 PM":
            football.objects.filter(tdate=bdate).update(TWEPM="red")
            football1.objects.filter(tdate=bdate).update(TWEPM="hide")
            
        elif btime == "01:00 PM - 02:00 PM":
            football.objects.filter(tdate=bdate).update(ONEPM="red")
            football1.objects.filter(tdate=bdate).update(ONEPM="hide")
            
        elif btime == "02:00 PM - 03:00 PM":
            football.objects.filter(tdate=bdate).update(TWOPM="red")
            football1.objects.filter(tdate=bdate).update(TWOPM="hide")
            
        elif btime == "03:00 PM - 04:00 PM":
            football.objects.filter(tdate=bdate).update(THREEPM="red")
            football1.objects.filter(tdate=bdate).update(THREEPM="hide")
            
        elif btime == "04:00 PM - 05:00 PM":
            football.objects.filter(tdate=bdate).update(FOURPM="red")
            football1.objects.filter(tdate=bdate).update(FOURPM="hide")
            
        elif btime == "05:00 PM - 06:00 PM":
            football.objects.filter(tdate=bdate).update(FIVEPM="red")
            football1.objects.filter(tdate=bdate).update(FIVEPM="hide")
            
        elif btime == "06:00 PM - 07:00 PM":
            football.objects.filter(tdate=bdate).update(SIXPM="red")
            football1.objects.filter(tdate=bdate).update(SIXPM="hide")
            
        elif btime == "07:00 PM - 08:00 PM":
            football.objects.filter(tdate=bdate).update(SEVENPM="red")
            football1.objects.filter(tdate=bdate).update(SEVENPM="hide")
            
        elif btime == "08:00 PM - 09:00 PM":
            football.objects.filter(tdate=bdate).update(EIGHTPM="red")
            football1.objects.filter(tdate=bdate).update(EIGHTPM="hide")
            
        elif btime == "09:00 PM - 10:00 PM":
            football.objects.filter(tdate=bdate).update(NINEPM="red")
            football1.objects.filter(tdate=bdate).update(NINEPM="hide")
            
        else:
            football.objects.filter(tdate=bdate).update(TENPM="red")
            football1.objects.filter(tdate=bdate).update(TENPM="hide")
            
        return redirect("Football",id=bid)

def basketballview(request,id):
    
    if request.method=='POST':
            cdate=request.POST["demo"]
            slotinfo=basketball.objects.get(tdate=cdate)
            dateinfo=basketball1.objects.get(tdate=cdate)
            return render(request,"basketball.html",{'id':id,'datas':slotinfo,'values':dateinfo,'seldate':cdate})
    
    info = basketball.objects.get(tdate=date.today())
    info1 = basketball1.objects.get(tdate=date.today())
    userinfo=turfuser.objects.get(id=id)
    uname = userinfo.username
    
    return render(request,"basketball.html",{'id':id,'datas':info,'values':info1,'uname':uname})


def basketballbook(request):
    
    
     if request.method == 'POST':
        bid=int(request.POST["bid"])
        bdate=request.POST["bdate"]
        btime=request.POST["btime"]
        sport=request.POST["sport"]
        amount=request.POST["amt"]
        
        new_data = booking(bdate=bdate,btime=btime,sport=sport,amount=amount,turfuser_id=bid)
        new_data.save()
        data = turfuser.objects.get(id=bid)
        mail = data.umail
        settings.EMAIL_HOST_USER = 'sportsclub3115@gmail.com'
        settings.EMAIL_HOST_PASSWORD = 'lkbq ewpe spbz qsya'
        send_mail("Sportz club","Your Slot for Basketball "  + " on " + bdate + " at " + btime + " has been booked successfully",settings.EMAIL_HOST_USER ,[mail])
        
        if btime == "05:00 AM - 06:00 AM":
            basketball.objects.filter(tdate=bdate).update(FIVEAM="red")
            basketball1.objects.filter(tdate=bdate).update(FIVEAM="hide")
        
        elif btime == "06:00 AM - 07:00 AM":
            basketball.objects.filter(tdate=bdate).update(SIXAM="red")
            basketball1.objects.filter(tdate=bdate).update(SIXAM="hide")
            
        elif btime == "07:00 AM - 08:00 AM":
            basketball.objects.filter(tdate=bdate).update(SEVENAM="red")
            basketball1.objects.filter(tdate=bdate).update(SEVENAM="hide")
            
        elif btime == "08:00 AM - 09:00 AM":
            basketball.objects.filter(tdate=bdate).update(EIGHTAM="red")
            basketball1.objects.filter(tdate=bdate).update(EIGHTAM="hide")
            
        elif btime == "09:00 AM - 10:00 AM":
            basketball.objects.filter(tdate=bdate).update(NINEAM="red")
            basketball1.objects.filter(tdate=bdate).update(NINEAM="hide")
            
        elif btime == "10:00 AM - 11:00 AM":
            basketball.objects.filter(tdate=bdate).update(TENAM="red")
            basketball1.objects.filter(tdate=bdate).update(TENAM="hide")
            
        elif btime == "11:00 AM - 12:00 PM":
            basketball.objects.filter(tdate=bdate).update(ELEAM="red")
            basketball1.objects.filter(tdate=bdate).update(ELEAM="hide")
            
        elif btime == "12:00 PM - 01:00 PM":
            basketball.objects.filter(tdate=bdate).update(TWEPM="red")
            basketball1.objects.filter(tdate=bdate).update(TWEPM="hide")
            
        elif btime == "01:00 PM - 02:00 PM":
            basketball.objects.filter(tdate=bdate).update(ONEPM="red")
            basketball1.objects.filter(tdate=bdate).update(ONEPM="hide")
            
        elif btime == "02:00 PM - 03:00 PM":
            basketball.objects.filter(tdate=bdate).update(TWOPM="red")
            basketball1.objects.filter(tdate=bdate).update(TWOPM="hide")
            
        elif btime == "03:00 PM - 04:00 PM":
            basketball.objects.filter(tdate=bdate).update(THREEPM="red")
            basketball1.objects.filter(tdate=bdate).update(THREEPM="hide")
            
        elif btime == "04:00 PM - 05:00 PM":
            basketball.objects.filter(tdate=bdate).update(FOURPM="red")
            basketball1.objects.filter(tdate=bdate).update(FOURPM="hide")
            
        elif btime == "05:00 PM - 06:00 PM":
            basketball.objects.filter(tdate=bdate).update(FIVEPM="red")
            basketball1.objects.filter(tdate=bdate).update(FIVEPM="hide")
            
        elif btime == "06:00 PM - 07:00 PM":
            basketball.objects.filter(tdate=bdate).update(SIXPM="red")
            basketball1.objects.filter(tdate=bdate).update(SIXPM="hide")
            
        elif btime == "07:00 PM - 08:00 PM":
            basketball.objects.filter(tdate=bdate).update(SEVENPM="red")
            basketball1.objects.filter(tdate=bdate).update(SEVENPM="hide")
            
        elif btime == "08:00 PM - 09:00 PM":
            basketball.objects.filter(tdate=bdate).update(EIGHTPM="red")
            basketball1.objects.filter(tdate=bdate).update(EIGHTPM="hide")
            
        elif btime == "09:00 PM - 10:00 PM":
            basketball.objects.filter(tdate=bdate).update(NINEPM="red")
            basketball1.objects.filter(tdate=bdate).update(NINEPM="hide")
            
        else:
            basketball.objects.filter(tdate=bdate).update(TENPM="red")
            basketball1.objects.filter(tdate=bdate).update(TENPM="hide")
            
        return redirect("Basketball",id=bid)

def handballview(request,id):
    
    if request.method=='POST':
            cdate=request.POST["demo"]
            slotinfo=handball.objects.get(tdate=cdate)
            dateinfo=handball1.objects.get(tdate=cdate)
            return render(request,"handball.html",{'id':id,'datas':slotinfo,'values':dateinfo,'seldate':cdate})
    
    info = handball.objects.get(tdate=date.today())
    info1 = handball1.objects.get(tdate=date.today())
    userinfo=turfuser.objects.get(id=id)
    uname = userinfo.username
    
    return render(request,"handball.html",{'id':id,'datas':info,'values':info1,'uname':uname})


def handballbook(request):
    
    
     if request.method == 'POST':
        bid=int(request.POST["bid"])
        bdate=request.POST["bdate"]
        btime=request.POST["btime"]
        sport=request.POST["sport"]
        amount=request.POST["amt"]
        
        new_data = booking(bdate=bdate,btime=btime,sport=sport,amount=amount,turfuser_id=bid)
        new_data.save()
        data = turfuser.objects.get(id=bid)
        mail = data.umail
        settings.EMAIL_HOST_USER = 'sportsclub3115@gmail.com'
        settings.EMAIL_HOST_PASSWORD = 'lkbq ewpe spbz qsya'
        send_mail("Sportz club","Your Slot for Handball "  + " on " + bdate + " at " + btime + " has been booked successfully",settings.EMAIL_HOST_USER ,[mail])
        
        if btime == "05:00 AM - 06:00 AM":
            handball.objects.filter(tdate=bdate).update(FIVEAM="red")
            handball1.objects.filter(tdate=bdate).update(FIVEAM="hide")
        
        elif btime == "06:00 AM - 07:00 AM":
            handball.objects.filter(tdate=bdate).update(SIXAM="red")
            handball1.objects.filter(tdate=bdate).update(SIXAM="hide")
            
        elif btime == "07:00 AM - 08:00 AM":
            handball.objects.filter(tdate=bdate).update(SEVENAM="red")
            handball1.objects.filter(tdate=bdate).update(SEVENAM="hide")
            
        elif btime == "08:00 AM - 09:00 AM":
            handball.objects.filter(tdate=bdate).update(EIGHTAM="red")
            handball1.objects.filter(tdate=bdate).update(EIGHTAM="hide")
            
        elif btime == "09:00 AM - 10:00 AM":
            handball.objects.filter(tdate=bdate).update(NINEAM="red")
            handball1.objects.filter(tdate=bdate).update(NINEAM="hide")
            
        elif btime == "10:00 AM - 11:00 AM":
            handball.objects.filter(tdate=bdate).update(TENAM="red")
            handball1.objects.filter(tdate=bdate).update(TENAM="hide")
            
        elif btime == "11:00 AM - 12:00 PM":
            handball.objects.filter(tdate=bdate).update(ELEAM="red")
            handball1.objects.filter(tdate=bdate).update(ELEAM="hide")
            
        elif btime == "12:00 PM - 01:00 PM":
            handball.objects.filter(tdate=bdate).update(TWEPM="red")
            handball1.objects.filter(tdate=bdate).update(TWEPM="hide")
            
        elif btime == "01:00 PM - 02:00 PM":
            handball.objects.filter(tdate=bdate).update(ONEPM="red")
            handball1.objects.filter(tdate=bdate).update(ONEPM="hide")
            
        elif btime == "02:00 PM - 03:00 PM":
            handball.objects.filter(tdate=bdate).update(TWOPM="red")
            handball1.objects.filter(tdate=bdate).update(TWOPM="hide")
            
        elif btime == "03:00 PM - 04:00 PM":
            handball.objects.filter(tdate=bdate).update(THREEPM="red")
            handball1.objects.filter(tdate=bdate).update(THREEPM="hide")
            
        elif btime == "04:00 PM - 05:00 PM":
            handball.objects.filter(tdate=bdate).update(FOURPM="red")
            handball1.objects.filter(tdate=bdate).update(FOURPM="hide")
            
        elif btime == "05:00 PM - 06:00 PM":
            handball.objects.filter(tdate=bdate).update(FIVEPM="red")
            handball1.objects.filter(tdate=bdate).update(FIVEPM="hide")
            
        elif btime == "06:00 PM - 07:00 PM":
            handball.objects.filter(tdate=bdate).update(SIXPM="red")
            handball1.objects.filter(tdate=bdate).update(SIXPM="hide")
            
        elif btime == "07:00 PM - 08:00 PM":
            handball.objects.filter(tdate=bdate).update(SEVENPM="red")
            handball1.objects.filter(tdate=bdate).update(SEVENPM="hide")
            
        elif btime == "08:00 PM - 09:00 PM":
            handball.objects.filter(tdate=bdate).update(EIGHTPM="red")
            handball1.objects.filter(tdate=bdate).update(EIGHTPM="hide")
            
        elif btime == "09:00 PM - 10:00 PM":
            handball.objects.filter(tdate=bdate).update(NINEPM="red")
            handball1.objects.filter(tdate=bdate).update(NINEPM="hide")
            
        else:
            handball.objects.filter(tdate=bdate).update(TENPM="red")
            handball1.objects.filter(tdate=bdate).update(TENPM="hide")
            
        return redirect("Handball",id=bid)

def volleyballview(request,id):
    
    if request.method=='POST':
            cdate=request.POST["demo"]
            slotinfo=volleyball.objects.get(tdate=cdate)
            dateinfo=volleyball1.objects.get(tdate=cdate)
            return render(request,"volleyball.html",{'id':id,'datas':slotinfo,'values':dateinfo,'seldate':cdate})
    
    info = volleyball.objects.get(tdate=date.today())
    info1 = volleyball1.objects.get(tdate=date.today())
    userinfo=turfuser.objects.get(id=id)
    uname = userinfo.username
    
    return render(request,"volleyball.html",{'id':id,'datas':info,'values':info1,'uname':uname})


def volleyballbook(request):
    
    
     if request.method == 'POST':
        bid=int(request.POST["bid"])
        bdate=request.POST["bdate"]
        btime=request.POST["btime"]
        sport=request.POST["sport"]
        amount=request.POST["amt"]
        
        new_data = booking(bdate=bdate,btime=btime,sport=sport,amount=amount,turfuser_id=bid)
        new_data.save()
        data = turfuser.objects.get(id=bid)
        mail = data.umail
        settings.EMAIL_HOST_USER = 'sportsclub3115@gmail.com'
        settings.EMAIL_HOST_PASSWORD = 'lkbq ewpe spbz qsya'
        send_mail("Sportz club","Your Slot for Volleyball "  + " on " + bdate + " at " + btime + " has been booked successfully",settings.EMAIL_HOST_USER ,[mail])
        
        if btime == "05:00 AM - 06:00 AM":
            volleyball.objects.filter(tdate=bdate).update(FIVEAM="red")
            volleyball1.objects.filter(tdate=bdate).update(FIVEAM="hide")
        
        elif btime == "06:00 AM - 07:00 AM":
            volleyball.objects.filter(tdate=bdate).update(SIXAM="red")
            volleyball1.objects.filter(tdate=bdate).update(SIXAM="hide")
            
        elif btime == "07:00 AM - 08:00 AM":
            volleyball.objects.filter(tdate=bdate).update(SEVENAM="red")
            volleyball1.objects.filter(tdate=bdate).update(SEVENAM="hide")
            
        elif btime == "08:00 AM - 09:00 AM":
            volleyball.objects.filter(tdate=bdate).update(EIGHTAM="red")
            volleyball1.objects.filter(tdate=bdate).update(EIGHTAM="hide")
            
        elif btime == "09:00 AM - 10:00 AM":
            volleyball.objects.filter(tdate=bdate).update(NINEAM="red")
            volleyball1.objects.filter(tdate=bdate).update(NINEAM="hide")
            
        elif btime == "10:00 AM - 11:00 AM":
            volleyball.objects.filter(tdate=bdate).update(TENAM="red")
            volleyball1.objects.filter(tdate=bdate).update(TENAM="hide")
            
        elif btime == "11:00 AM - 12:00 PM":
            volleyball.objects.filter(tdate=bdate).update(ELEAM="red")
            volleyball1.objects.filter(tdate=bdate).update(ELEAM="hide")
            
        elif btime == "12:00 PM - 01:00 PM":
            volleyball.objects.filter(tdate=bdate).update(TWEPM="red")
            volleyball1.objects.filter(tdate=bdate).update(TWEPM="hide")
            
        elif btime == "01:00 PM - 02:00 PM":
            volleyball.objects.filter(tdate=bdate).update(ONEPM="red")
            volleyball1.objects.filter(tdate=bdate).update(ONEPM="hide")
            
        elif btime == "02:00 PM - 03:00 PM":
            volleyball.objects.filter(tdate=bdate).update(TWOPM="red")
            volleyball1.objects.filter(tdate=bdate).update(TWOPM="hide")
            
        elif btime == "03:00 PM - 04:00 PM":
            volleyball.objects.filter(tdate=bdate).update(THREEPM="red")
            volleyball1.objects.filter(tdate=bdate).update(THREEPM="hide")
            
        elif btime == "04:00 PM - 05:00 PM":
            volleyball.objects.filter(tdate=bdate).update(FOURPM="red")
            volleyball1.objects.filter(tdate=bdate).update(FOURPM="hide")
            
        elif btime == "05:00 PM - 06:00 PM":
            volleyball.objects.filter(tdate=bdate).update(FIVEPM="red")
            volleyball1.objects.filter(tdate=bdate).update(FIVEPM="hide")
            
        elif btime == "06:00 PM - 07:00 PM":
            volleyball.objects.filter(tdate=bdate).update(SIXPM="red")
            volleyball1.objects.filter(tdate=bdate).update(SIXPM="hide")
            
        elif btime == "07:00 PM - 08:00 PM":
            volleyball.objects.filter(tdate=bdate).update(SEVENPM="red")
            volleyball1.objects.filter(tdate=bdate).update(SEVENPM="hide")
            
        elif btime == "08:00 PM - 09:00 PM":
            volleyball.objects.filter(tdate=bdate).update(EIGHTPM="red")
            volleyball1.objects.filter(tdate=bdate).update(EIGHTPM="hide")
            
        elif btime == "09:00 PM - 10:00 PM":
            volleyball.objects.filter(tdate=bdate).update(NINEPM="red")
            volleyball1.objects.filter(tdate=bdate).update(NINEPM="hide")
            
        else:
            volleyball.objects.filter(tdate=bdate).update(TENPM="red")
            volleyball1.objects.filter(tdate=bdate).update(TENPM="hide")
            
        return redirect("volleyball",id=bid)

def kabaddiview(request,id):
    
    if request.method=='POST':
            cdate=request.POST["demo"]
            slotinfo=kabaddi.objects.get(tdate=cdate)
            dateinfo=kabaddi1.objects.get(tdate=cdate)
            return render(request,"kabaddi.html",{'id':id,'datas':slotinfo,'values':dateinfo,'seldate':cdate})
    
    info = kabaddi.objects.get(tdate=date.today())
    info1 = kabaddi1.objects.get(tdate=date.today())
    userinfo=turfuser.objects.get(id=id)
    uname = userinfo.username
    
    return render(request,"kabaddi.html",{'id':id,'datas':info,'values':info1,'uname':uname})


def kabaddibook(request):
    
    
     if request.method == 'POST':
        bid=int(request.POST["bid"])
        bdate=request.POST["bdate"]
        btime=request.POST["btime"]
        sport=request.POST["sport"]
        amount=request.POST["amt"]
        
        new_data = booking(bdate=bdate,btime=btime,sport=sport,amount=amount,turfuser_id=bid)
        new_data.save()
        data = turfuser.objects.get(id=bid)
        mail = data.umail
        settings.EMAIL_HOST_USER = 'sportsclub3115@gmail.com'
        settings.EMAIL_HOST_PASSWORD = 'lkbq ewpe spbz qsya'
        send_mail("Sportz club","Your Slot for kabaddi "  + " on " + bdate + " at " + btime + " has been booked successfully",settings.EMAIL_HOST_USER ,[mail])
        
        if btime == "05:00 AM - 06:00 AM":
            kabaddi.objects.filter(tdate=bdate).update(FIVEAM="red")
            kabaddi1.objects.filter(tdate=bdate).update(FIVEAM="hide")
        
        elif btime == "06:00 AM - 07:00 AM":
            kabaddi.objects.filter(tdate=bdate).update(SIXAM="red")
            kabaddi1.objects.filter(tdate=bdate).update(SIXAM="hide")
            
        elif btime == "07:00 AM - 08:00 AM":
            kabaddi.objects.filter(tdate=bdate).update(SEVENAM="red")
            kabaddi1.objects.filter(tdate=bdate).update(SEVENAM="hide")
            
        elif btime == "08:00 AM - 09:00 AM":
            kabaddi.objects.filter(tdate=bdate).update(EIGHTAM="red")
            kabaddi1.objects.filter(tdate=bdate).update(EIGHTAM="hide")
            
        elif btime == "09:00 AM - 10:00 AM":
            kabaddi.objects.filter(tdate=bdate).update(NINEAM="red")
            kabaddi1.objects.filter(tdate=bdate).update(NINEAM="hide")
            
        elif btime == "10:00 AM - 11:00 AM":
            kabaddi.objects.filter(tdate=bdate).update(TENAM="red")
            kabaddi1.objects.filter(tdate=bdate).update(TENAM="hide")
            
        elif btime == "11:00 AM - 12:00 PM":
            kabaddi.objects.filter(tdate=bdate).update(ELEAM="red")
            kabaddi1.objects.filter(tdate=bdate).update(ELEAM="hide")
            
        elif btime == "12:00 PM - 01:00 PM":
            kabaddi.objects.filter(tdate=bdate).update(TWEPM="red")
            kabaddi1.objects.filter(tdate=bdate).update(TWEPM="hide")
            
        elif btime == "01:00 PM - 02:00 PM":
            kabaddi.objects.filter(tdate=bdate).update(ONEPM="red")
            kabaddi1.objects.filter(tdate=bdate).update(ONEPM="hide")
            
        elif btime == "02:00 PM - 03:00 PM":
            kabaddi.objects.filter(tdate=bdate).update(TWOPM="red")
            kabaddi1.objects.filter(tdate=bdate).update(TWOPM="hide")
            
        elif btime == "03:00 PM - 04:00 PM":
            kabaddi.objects.filter(tdate=bdate).update(THREEPM="red")
            kabaddi1.objects.filter(tdate=bdate).update(THREEPM="hide")
            
        elif btime == "04:00 PM - 05:00 PM":
            kabaddi.objects.filter(tdate=bdate).update(FOURPM="red")
            kabaddi1.objects.filter(tdate=bdate).update(FOURPM="hide")
            
        elif btime == "05:00 PM - 06:00 PM":
            kabaddi.objects.filter(tdate=bdate).update(FIVEPM="red")
            kabaddi1.objects.filter(tdate=bdate).update(FIVEPM="hide")
            
        elif btime == "06:00 PM - 07:00 PM":
            kabaddi.objects.filter(tdate=bdate).update(SIXPM="red")
            kabaddi1.objects.filter(tdate=bdate).update(SIXPM="hide")
            
        elif btime == "07:00 PM - 08:00 PM":
            kabaddi.objects.filter(tdate=bdate).update(SEVENPM="red")
            kabaddi1.objects.filter(tdate=bdate).update(SEVENPM="hide")
            
        elif btime == "08:00 PM - 09:00 PM":
            kabaddi.objects.filter(tdate=bdate).update(EIGHTPM="red")
            kabaddi1.objects.filter(tdate=bdate).update(EIGHTPM="hide")
            
        elif btime == "09:00 PM - 10:00 PM":
            kabaddi.objects.filter(tdate=bdate).update(NINEPM="red")
            kabaddi1.objects.filter(tdate=bdate).update(NINEPM="hide")
            
        else: 
            kabaddi.objects.filter(tdate=bdate).update(TENPM="red")
            kabaddi1.objects.filter(tdate=bdate).update(TENPM="hide")
            
        return redirect("kabaddi",id=bid)