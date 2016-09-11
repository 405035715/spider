#encoding = 'utf-8'


import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
import datetime
import schedule
import pyodbc

#数据库
# 用户: jd  密码: jd,1234
# 地址: 121.40.123.131
# 存储过程: jd_GetLatestFirstRecord

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

#查询数据库
def selSql(selStr):
    sqlresult =[]
    connectStr = 'DRIVER={SQL Server};SERVER=121.40.123.131;PORT=1433;DATABASE=espacs;UID=jd;PWD=jd,1234; '
    cnxn = pyodbc.connect(connectStr)
    cursor = cnxn.cursor()
    try:
        cursor.execute(selStr)
    except Exception as e:
        print(e)
    sum = 0
    while 1:
        row = cursor.fetchone()
        sum = sum + 1
        if not row:
            break
        sqlresult.append(list(row))
        #print(row)
    #print(sum)
    cnxn.close
    return sqlresult


if __name__ == '__main__':
    schedule.every().day.at("11:00").do(sendEmail)  # 每天的11点、15点 查询数据库
    schedule.every().day.at("15:00").do(sendEmail)
    nowTime = datetime.datetime.now()
    # sendEmail()
    selstr_doctors = 'SET NOCOUNT ON; EXEC  tj_P_RUN_PROCDURE_WITH_SELECTRETURN  \'jd_GetLatestFirstRecord\' ,\'\'  ' #查询每个医院的影像的最晚时间
    doctors_tmp = selSql(selstr_doctors)
    for hospital in doctors_tmp:
        if (nowTime-hospital[0]).seconds > 60*60*2:
            print('%s上传影像有异常，请注意！最后一次上传影像时间：%s \n' % (hospital[1], hospital[0]))
    while True:
        schedule.run_pending()
        time.sleep(1)



