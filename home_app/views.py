from django.shortcuts import render
from feature_box.models import Feature
from testimonial_app.models import Testimonial
from contactus_app.models import Contactus
from projectbox_app.models import Boxproject


def home(request):
    feature_box = Feature.objects.all()
    testimonial = Testimonial.objects.all()
    box = Boxproject.objects.all()

    n = request.POST.get('name')
    p = request.POST.get('phone')
    e = request.POST.get('email')
    t = request.POST.get('text')

    if n and p and e and t:
        print('hi')
        Contactus.objects.create(name=n, phone=p, email=e, text=t)

    return render(request, 'home_app/index.html', context={'feature': feature_box, 'testimonial': testimonial , 'box':box})
