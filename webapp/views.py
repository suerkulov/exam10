from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .forms import AdvertisementForm, ModeratorForm
from .models import Advertisement


class IndexView(ListView):
    model = Advertisement
    template_name = "advertisement/index.html"
    ordering = ['-publicated_at']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        advertisements = Advertisement.objects.filter(status='Publiced')
        context['advertisements'] = advertisements
        return context


class ModerateIndexView(PermissionRequiredMixin,ListView):
    model = Advertisement
    template_name = "advertisement/moderate_index.html"
    ordering = ['-created_at']
    permission_required = 'webapp.staff'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ModerateIndexView, self).get_context_data()
        advertisements = Advertisement.objects.filter(status='InModiration')
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
    permission_required = 'webapp.add_advertisement'

    def form_valid(self, form):
        advertisement = form.save(commit=False)
        advertisement.author = self.request.user
        advertisement.save()
        return redirect('webapp:index')


class ModerateUpdateView(PermissionRequiredMixin, UpdateView):
    model = Advertisement
    form_class = ModeratorForm
    template_name = 'advertisement/update.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.staff'


class AdvertisementUpdateView(PermissionRequiredMixin, UpdateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = 'advertisement/update.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.change_advertisement'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.object.author


class AdvertisementDeleteView(PermissionRequiredMixin, DeleteView):
    model = Advertisement
    template_name = 'advertisement/delete.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_advertisement'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.object.author