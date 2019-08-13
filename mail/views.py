from django.shortcuts import render
from django.http import HttpResponse
from .models import Promotion
import os


def check_open(request, promotion_uuid):
    promotion = Promotion.objects.filter(uuid=promotion_uuid)
    promotion.update(is_read=True)

    img_path = os.path.join(os.path.dirname(__file__), 'static/img/sample.png')
    with open(img_path, 'rb') as f:
        return HttpResponse(f.read(), content_type="image/jpeg")
