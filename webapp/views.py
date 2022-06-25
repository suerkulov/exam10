from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from forms import AdvertisementForm
from models import Advertisement


class IndexView(ListView):
    model = Advertisement
    template_name = "advertisement/index.html"
    ordering = ['-publicated_at']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        advertisements = Advertisement.objects.filter(is_public=True)
        context['advertisements'] = advertisements
        return context


class AdvertisementView(DetailView):
    model = Advertisement
    template_name = 'advertisement/view.html'


class AdvertisementCreateView(LoginRequiredMixin,CreateView):
    model = Advertisement
    template_name = 'advertisement/create.html'
    form_class = AdvertisementForm
    success_url = reverse_lazy('webapp:index')

    def form_valid(self, form):
        advertisement = form.save(commit=False)
        advertisement.author = self.request.user
        advertisement.save()
        return redirect('webapp:index')