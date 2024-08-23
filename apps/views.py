from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from apps.models import Product


# Create your views here.

class Home_pageView(ListView):
    queryset = Product.objects.all()
    template_name = 'apps/home-page.html'
    context_object_name = 'products'

    def get_queryset(self):
        qs = super().get_queryset()
        if search := self.request.GET.get('search'):
            qs = qs.filter(Q(name__icontains=search) | Q(name__icontains=search))
        return qs
