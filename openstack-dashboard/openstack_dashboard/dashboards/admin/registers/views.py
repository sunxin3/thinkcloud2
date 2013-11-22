from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django.views.generic import list_detail
from .forms import RegistrationForm

import smtplib
from email.mime.text import MIMEText


mail_to="sunxin3@lenovo.com,zhaokc1@lenovo.com,chenzg4@lenovo.com"

def send_mail(to_list,sub,content):
    mail_host="localhost"
    mail_user=""
    mail_pass=""
    mail_postfix="thinkcloud.com"
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to_list
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        print '1'
        return True
    except Exception, e:
        print '2'
        print str(e)
        return False

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']  
            realname = form.cleaned_data['realname']  
            email = form.cleaned_data['email']  
            password = form.cleaned_data['password']  
	    if send_mail(mail_to,"hello","this is python sent"):
                return HttpResponse("Register Success!")  
	    else:
                return HttpResponse("Register Failed!")  
    else:
        form = RegistrationForm()
    variables = RequestContext(request,{'form':form})
    return render_to_response('registers/register.html',variables)
