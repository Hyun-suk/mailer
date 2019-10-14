import smtplib, os, pickle
from email.mime.text import MIMEText
from email import encoders  # 파일전송을 할 때 이미지나 문서 동영상 등의 파일을 문자열로 변환할 때 사용할 패키지
from email.mime.multipart import MIMEMultipart   # 메시지를 보낼 때 메시지에 대한 모듈
from email.mime.base import MIMEBase     # 파일을 전송할 때 사용되는 모듈
from dotenv import load_dotenv, find_dotenv
import re

class Mail:

    def __init__(self, mail_id, mail_key):
        self.mail_id = mail_id
        self.mail_key = mail_key

    def send_mail(self, sender, receiver, title, content):
        regex = re.compile(r'(?<=@)[^.]+(?=\.)')
        domain = regex.search(sender).group(0)

        smtp_servers = {
            'gmail': 'smtp.gmail.com',
            'naver': 'smtp.naver.com',
        }

        server = smtplib.SMTP_SSL(smtp_servers.get(domain), 465)
        server.login(self.mail_id, self.mail_key)

        msg = MIMEText(content, 'html')
        msg['Subject'] = title
        msg['From'] = sender
        msg['To'] = receiver

        server.sendmail(sender, receiver, msg.as_string())
        server.quit()


if __name__=='__main__':
    load_dotenv(find_dotenv())

    mail = Mail(os.getenv('MAIL_ID'), os.getenv('MAIL_PWD'))
    me = 'better.imhs@gmail.com'
    you = 'better.imhs@gmail.com'

    mail.send_mail('better.imhs@gmail.com', you, '타이틀 테스트', '내용 테스트')
