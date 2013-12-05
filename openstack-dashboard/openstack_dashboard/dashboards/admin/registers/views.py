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
        return True
    except Exception, e:
        print str(e)
        return False

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']  
            realname = form.cleaned_data['realname']  
            department = form.cleaned_data['department']  
            email = form.cleaned_data['email']  
            password = form.cleaned_data['password']  
	    mail_body = 'There is a new user to register our ThinkCloud website, the detail information is below:\n'
	    mail_body += 'User Name: '
	    mail_body += username
	    mail_body += '\n'
	    mail_body += 'Password: '
	    mail_body += password 
	    mail_body += '\n'
	    mail_body += 'Real Name: '
	    mail_body += realname
	    mail_body += '\n'
	    mail_body += 'Department: '
	    mail_body += department
	    mail_body += '\n'
	    mail_body += 'Email: '
	    mail_body += email 
	    mail_body += '\n'
	    mail_body += 'Please help to handle this request, Thanks!'
	    if send_mail(mail_to,"Think Cloud Register Mail",mail_body):
                return render_to_response("registers/register_success.html")  
	    else:
                return render_to_response("registers/register_fail.html")  
    else:
        form = RegistrationForm()
    variables = RequestContext(request,{'form':form})
    return render_to_response('registers/register.html',variables)
