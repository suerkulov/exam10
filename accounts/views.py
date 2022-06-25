from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, CreateView

from forms import MyUserCreationForm

User = get_user_model()


class UserView(DetailView):
    model = get_user_model()
    template_name = "user_view.html"
    context_object_name = "user_object"


class RegisterView(CreateView):
    model = User
    form_class = MyUserCreationForm
    template_name = "registration.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:product_index')
        return next_url