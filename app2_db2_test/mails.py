import smtplib
from email.mime.text import MIMEText
from email.header import Header

#发生邮箱服务器
smtpserver = 'smtp.163.com'
#发送用户和密码
user = '18212707348@163.com'
password = 'MPLGBLGLJXRHYSAR'
#发送邮箱
sender = '18212707348@163.com'
#接收邮箱
receiver = '2665254503@qq.com'
#发送邮箱主题
subject = 'python test'
msg = MIMEText('<html><h1>你好！我是python测试邮件！</h1><html>','html','utf-8')
msg['Subject'] = Header(subject,'utf-8')
#连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()


