from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Promotion
from .services import Mail
import os


def index(request):
    return render(request, 'index.html', {})

def send_mail(request):
    if request.method == 'POST':
        title = request.POST['title']
        from_mail = request.POST['from']
        to_email = request.POST['to']
        messages = request.POST['messages']

        mail = Mail()
        print(mail.send_mail('google', from_mail, to_email, title, messages))

        return redirect('mail:index')
    else:
        return render(request, 'send_mail.html', {})


def check_open(request, promotion_uuid):
    promotion = Promotion.objects.filter(uuid=promotion_uuid)
    promotion.update(is_read=True)

    img_path = os.path.join(os.path.dirname(__file__), 'static/img/sample.png')
    with open(img_path, 'rb') as f:
        return HttpResponse(f.read(), content_type="image/jpeg")
