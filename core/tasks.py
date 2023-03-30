from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from core.models import News, Subscriber
from django.template.loader import get_template


@shared_task
def send_emails():
    print("changed")
    
    subscribers = Subscriber.objects.all()

    for subscriber in subscribers:
        d ={"news": News.objects.order_by('-id')[:10]}
        subject, from_email, to = 'Innovation News', 'phinnovationstream@outlook.com', f'{subscriber.email}'
        html = get_template('email.html')
        html_content2 = html.render(d)
        text_content = 'This is an important message.'
        msg = EmailMultiAlternatives(subject, html_content2, from_email, [to])
        
        msg.attach_alternative(html_content2, "text/html")
        msg.send()

