import smtplib
from email.message import EmailMessage

from celery import Celery 
from config import SMTP_USER, SMPT_PASSWORD

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery = Celery('tasks', broker='redis://localhost:6379')

def get_email_template_dashboard(username: str):
    email = EmailMessage()
    email['Subject'] = 'Отчет'
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER
    
    email.set_content(
    '<div>'
    f'< style="color: red;">Здравствуйте, {username}
    '</div>',
    subtype='html'
    )
    return email

@celery.task
def send_email_report_dashboard(username: str):
    email = get_email_template_dashboard(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMPT_PASSWORD)
        server.send_message(email)