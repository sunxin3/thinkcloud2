import smtplib
from email.mime.text import MIMEText

def send_mail(to_list, sub, content, mail_host):
    mail_user="sysadmin"
    mail_pass=""
    mail_postfix="thinkcloudlab.com"
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content, 'plain', 'UTF-8')
    msg['Subject'] = sub
    msg['From'] = me
    print to_list
    print type(to_list)
    print "sunxin"
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
