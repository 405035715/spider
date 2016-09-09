#encoding = 'utf-8'


import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
import schedule

# 发送邮件
def sendEmail() :
    sender = '405035715@qq.com'
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "405035715@qq.com"  # 用户名
    mail_pass = "yoaemizwjxfqcagj"  # 口令
    # sender = 'wherever644@163.com'
    # mail_host = "smtp.163.com"  # 设置服务器
    # mail_user = "wherever644@163.com"  # 用户名
    # mail_pass = "zyh19870910"  # 口令
    receivers = ['405035715@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText('dfienfkd', 'plain', 'utf-8')  # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message['From'] = Header("张跃华", 'utf-8')
    message['To'] = ";".join(receivers)
    subject = '钜典邮件'  # 标题
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        # smtpObj = smtplib.SMTP()
        # smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.close()
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)
        print("Error: 无法发送邮件")


if __name__ == '__main__':
    schedule.every().day.at("6:56").do(sendEmail)  # 每天的11点、14点 查询数据库
    schedule.every().day.at("7:14").do(sendEmail)
    print(time.localtime())
    sendEmail()
    while True:
        schedule.run_pending()
        time.sleep(1)

