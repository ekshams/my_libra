from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, Http404
from django.template import loader
from . models import *
from .form import *
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib import messages, auth
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.template import RequestContext


class HomeView(LoginRequiredMixin, generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'index.html'
    context_object_name = 'books'
    login_url = 'login'
    raise_exception = True

    def get_queryset(self):
        return Book.objects.all()


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'book_form.html'
    raise_exception = True
    # we can use one method from following methods
    form_class = BookForm
    # fields = ['name', 'author_name', 'subject']


class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'book_form.html'
    form_class = BookForm
    raise_exception = True


class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('home')
    raise_exception = True

    # the following function used to avoid the delete confirmation page
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'

    # display blank form
    def get(self, request ):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process the form
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return User objects if credential are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('home')

            return render(request, self.template_name, {'form': form})


class LoginView(View):
    form_class = LoginForm
    template_name = 'login_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process the form
    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse("Inactive user")
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


def handler404(request):
    return render(request, "404.html")


def handler500(request):
    return render(request, "500.html")


def handler403(request):
    return render(request, "403.html")




