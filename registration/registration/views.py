from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy



class IndexView(TemplateView):
    template_name='index.html'


# class SecretView(LoginRequiredMixin, TemplateView):
    # template_name='special.html'


@login_required
def secret(request):
    return render(request, 'special.html',{})
