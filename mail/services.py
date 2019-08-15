import smtplib, os, pickle
from email.mime.text import MIMEText
from email import encoders  # 파일전송을 할 때 이미지나 문서 동영상 등의 파일을 문자열로 변환할 때 사용할 패키지
from email.mime.multipart import MIMEMultipart   # 메시지를 보낼 때 메시지에 대한 모듈
from email.mime.base import MIMEBase     # 파일을 전송할 때 사용되는 모듈
from dotenv import load_dotenv


load_dotenv()
MAIL_ID = os.getenv('MAIL_ID')
MAIL_PWD = os.getenv('MAIL_PWD')


def send_mail(service, sender, receiver, title, content):
    service_smtp = {
        'google': 'smtp.gmail.com',
        'naver': 'smtp.naver.com',
    }
    server = smtplib.SMTP_SSL(service_smtp[service], 465)
    server.login(MAIL_ID, MAIL_PWD)

    msg = MIMEText(content)
    msg['Subject'] = title
    msg['From'] = sender
    msg['To'] = receiver

    server.sendmail(sender, receiver, msg.as_string())
    server.quit()



if __name__=='__main__':
    me = 'better.imhs@gmail.com'
    you = 'better.imhs@gmail.com'

    send_mail('google', me, you, '타이틀 테스트', '내용 테스트')
