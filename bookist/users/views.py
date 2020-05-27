from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic.edit import CreateView

from .models import CustomUser
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = 'login'
    model = CustomUser
    template_name = 'books/user_profile.html'

    def get_success_url(self):
        return reverse('user-profile', kwargs={'pk': self.kwargs['pk'], })


class UserProfileUpdate(LoginRequiredMixin, generic.UpdateView):
    login_url = 'login'
    model = CustomUser
    fields = ('username', 'first_name', 'last_name', 'user_bio', 'location', 'profile_image', 'email')

    def get_success_url(self):
        return reverse('user-profile', kwargs={'pk': self.kwargs['pk'], })


@login_required(login_url='login')
def profile(request, pk=None):
    if pk:
        user = CustomUser.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'users/profile.html', args)