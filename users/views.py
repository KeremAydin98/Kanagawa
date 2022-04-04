from .forms import CustomUserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

class SignUpPageView(CreateView):

    form_class = CustomUserCreationForm

    success_url = reverse_lazy('login')

    template_name = 'registration/signup.html'





