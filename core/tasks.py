from celery import shared_task
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from core.models import News, Subscriber


@shared_task
def reset_upvotes():
    print("changed")
    # send_mail(
    #     'Subject here',
    #     'Here is the message.',
    #     'xomurad41@gmail.com',
    #     ['murad.aghazadaa@gmail.com'],
    #     fail_silently=False,
    # )
    news1 = News.objects.order_by('-id')[0]
    news2 = News.objects.order_by('-id')[1]
    news3 = News.objects.order_by('-id')[2]
    news4 = News.objects.order_by('-id')[3]
    news5 = News.objects.order_by('-id')[4]
    subscribers = Subscriber.objects.all()

    for subscriber in subscribers:
        subject, from_email, to = 'hello', 'xomurad41@gmail.com', f'{subscriber.email}'
        text_content = 'This is an important message.'
        html_content = f''' <div class="col-md-6 mb-4"  style="margin-bottom: 30px;" style="margin-bottom: 30px;">
                        <a href="/news/{news1.id}">
                            <div class="news-card-small" style="background-image: linear-gradient(to top, rgba(0, 0, 0, 0.680), rgba(0, 0, 0, 0.076) ), url({news1.banner_image.url}); height: 430px;
        background-repeat: no-repeat;
        background-position: center;
        width: 100%;
        border-radius: 10px;
        padding: 30px;
        transition: all 1s;">
                                <div class="news-data" style="position: absolute;
        bottom: 50px;
        color: white;">
                                
                                
                                    <span></span>
                                    <h2 class="news-title">{news1.title}</h2>

                                </div>
                            </div>
                        </a>
                        </div>
                        
        <div class="col-md-6 mb-4"  style="margin-bottom: 30px;">
                        <a href="/news/{news2.id}">
                            <div class="news-card-small" style="background-image: linear-gradient(to top, rgba(0, 0, 0, 0.680), rgba(0, 0, 0, 0.076) ), url({news2.banner_image.url}); height: 430px;
        background-repeat: no-repeat;
        background-position: center;
        width: 100%;
        border-radius: 10px;
        padding: 30px;
        transition: all 1s;">
                                <div class="news-data" style="position: absolute;
        bottom: 50px;
        color: white;">
                                
                                
                                    <span></span>
                                    <h2 class="news-title">{news2.title}</h2>

                                </div>
                            </div>
                        </a>
                        </div>                
                        
                        
    <div class="col-md-6 mb-4"  style="margin-bottom: 30px;">
                        <a href="/news/{news3.id}">
                            <div class="news-card-small" style="background-image: linear-gradient(to top, rgba(0, 0, 0, 0.680), rgba(0, 0, 0, 0.076) ), url({news3.banner_image.url}); height: 430px;
        background-repeat: no-repeat;
        background-position: center;
        width: 100%;
        border-radius: 10px;
        padding: 30px;
        transition: all 1s;">
                                <div class="news-data" style="position: absolute;
        bottom: 50px;
        color: white;">
                                
                                
                                    <span></span>
                                    <h2 class="news-title">{news3.title}</h2>

                                </div>
                            </div>
                        </a>
                        </div>   



    <div class="col-md-6 mb-4"  style="margin-bottom: 30px;">
                        <a href="/news/{news4.id}">
                            <div class="news-card-small" style="background-image: linear-gradient(to top, rgba(0, 0, 0, 0.680), rgba(0, 0, 0, 0.076) ), url({news4.banner_image.url}); height: 430px;
        background-repeat: no-repeat;
        background-position: center;
        width: 100%;
        border-radius: 10px;
        padding: 30px;
        transition: all 1s;">
                                <div class="news-data" style="position: absolute;
        bottom: 50px;
        color: white;">
                                
                                
                                    <span></span>
                                    <h2 class="news-title">{news4.title}</h2>

                                </div>
                            </div>
                        </a>
                        </div>   



    <div class="col-md-6 mb-4"  style="margin-bottom: 30px;">
                        <a href="/news/{news5.id}">
                            <div class="news-card-small" style="background-image: linear-gradient(to top, rgba(0, 0, 0, 0.680), rgba(0, 0, 0, 0.076) ), url({news5.banner_image.url}); height: 430px;
        background-repeat: no-repeat;
        background-position: center;
        width: 100%;
        border-radius: 10px;
        padding: 30px;
        transition: all 1s;">
                                <div class="news-data" style="position: absolute;
        bottom: 50px;
        color: white;">
                                
                                
                                    <span></span>
                                    <h2 class="news-title">{news5.title}</h2>

                                </div>
                            </div>
                        </a>
                        </div>            
                        '''
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
