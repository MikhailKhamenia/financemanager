from django.urls import reverse
from django.views.generic import TemplateView,ListView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import TransactionForm
from .models import Transactions




class LoginView(TemplateView):
    template_name = "registration/login.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("profile"))
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)

class ProfilePage(TemplateView):
    template_name = "registration/profile.html"

class  SignUpView(TemplateView):
    template_name = "registration/signup.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse("signup"))

        return render(request, self.template_name)

class  ActionPage(TemplateView):
    template_name = "actions.html"

class  CryptPage(TemplateView):
    template_name = "crypt.html"

class LogoutView(TemplateView):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")

"""Главная страница со ссылками. суммами по каждому Source_types
   и целиком"""


def transaction_form(request):
    if request.method == 'POST':
        add_transaction = TransactionForm(request.POST)
        if add_transaction.is_valid():
            add_transaction.save()
            return redirect(reverse("profile"))
    else:
        add_transaction = TransactionForm()
    return render(request, "add_transaction.html", {'add_transaction': add_transaction})

def all_transactions(request):
    transactions=Transactions.objects.all()
    return render(request, 'transactions.html', {'transactions':transactions})





