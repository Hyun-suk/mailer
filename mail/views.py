from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import Promotion, Customer
from .services import Mail
from .forms import MarketingForm, SettingsForm
import os


def index(request):
    return render(request, 'index.html', {})

class CustomerListView(ListView):
    model = Customer
    paginate_by = 20
    template_name = 'customers.html'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'

def send_mail(request):
    if request.method == 'POST':
        from_mail = request.POST['from']
        to_email = request.POST['to']

        form = MarketingForm(request.POST)
        if form.is_valid():
            marketing = form.save(commit=False)
            marketing.save()

            mail = Mail()
            mail.send_mail('google', from_mail, to_email, marketing.name, marketing.content)

            customer = Customer.objects.get(email=to_email)
            Promotion.objects.create(marketing=marketing, customer=customer)

            return redirect('mail:index')
    else:
        form = MarketingForm
        return render(request, 'send_mail.html', {'form': form})

def settings(request):
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            settings = form.save(commit=False)
            settings.user = request.user
            settings.save()
            return redirect('mail:settings')
    else:
        form = SettingsForm()

    return render(request, 'settings.html', {'form': form})

def check_open(request, promotion_uuid):
    promotion = Promotion.objects.filter(uuid=promotion_uuid)
    promotion.update(is_read=True)

    img_path = os.path.join(os.path.dirname(__file__), 'static/img/sample.png')
    with open(img_path, 'rb') as f:
        return HttpResponse(f.read(), content_type="image/jpeg")
