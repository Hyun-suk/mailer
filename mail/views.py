from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Promotion, Customer, Settings
from .services import Mail
from .forms import MarketingForm, SettingsForm, AddressForm
import os


def index(request):
    return render(request, 'index.html', {})

@method_decorator(login_required, name='dispatch')
class CustomerListView(ListView):
    model = Customer
    paginate_by = 20
    template_name = 'customers.html'

@method_decorator(login_required, name='dispatch')
class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'

@login_required
def send_mail(request):
    if request.method == 'POST':
        marketing_form = MarketingForm(request.POST)
        address_form = AddressForm(request.user, request.POST)

        if marketing_form.is_valid() and address_form.is_valid():
            marketing = marketing_form.save(commit=False)
            marketing.save()

            sender = address_form.cleaned_data.get('from_mail')
            receivers = address_form.cleaned_data.get('to_mail')
            smtp_key = request.user.settings.get(email=sender).smtp_key

            mail = Mail(sender, smtp_key)

            for receiver in receivers:
                mail.send_mail(sender.email, receiver.email, marketing.name, marketing.content)
                Promotion.objects.create(marketing=marketing, customer=receiver)

            del mail

            return redirect('mail:index')
    else:
        marketing_form = MarketingForm
        address_form = AddressForm(request.user)
        return render(request, 'send_mail.html', {
            'marketing_form': marketing_form,
            'address_form': address_form
        })

@login_required
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
        settings = Settings.objects.filter(user=request.user)

    return render(request, 'settings.html', {'form': form, 'settings': settings})

@login_required
def delete_setting(request, setting_id):
    setting = Settings.objects.get(id=setting_id)
    if setting.user == request.user:
        setting.delete()
        return redirect('mail:settings')
    else:
        return render(request, 'warning.html')

    return render(request, 'settings.html', {'form': form, 'settings': settings})

@login_required
def check_open(request, promotion_uuid):
    promotion = Promotion.objects.filter(uuid=promotion_uuid)
    promotion.update(is_read=True)

    img_path = os.path.join(os.path.dirname(__file__), 'static/img/sample.png')
    with open(img_path, 'rb') as f:
        return HttpResponse(f.read(), content_type="image/jpeg")
