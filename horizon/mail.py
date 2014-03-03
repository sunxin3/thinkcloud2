import smtplib
from email.mime.text import MIMEText

def send_mail(sub, content, extra_to_list=None):

    to_list=['sunxin@lenovo.com', 'chenzg4@lenovo.com']
    if extra_to_list: 
	to_list.append(extra_to_list)
    mail_host="thinkcloudlab.com" 
    mail_user="sysadmin"
    mail_pass=""
    mail_postfix="thinkcloudlab.com"
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content, 'plain', 'UTF-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
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

__version__ = '0.1'
