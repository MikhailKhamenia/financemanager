from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm
from .models import Transactions, TransactionsPermissions
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def login_excluded(redirect_to):
    """ This decorator kicks authenticated users out of a view """
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to)
            return view_method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper


class LoginView(TemplateView):
    template_name = "registration/login.html"

    redirect_authenticated_user = True
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

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ActionPage(TemplateView):
    template_name = "actions.html"

class  CryptPage(TemplateView):
    template_name = "crypt.html"

class LogoutView(TemplateView):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")



@login_required
def transaction_form(request):
    if request.method == 'POST':
        add_transaction = TransactionForm(request.POST)
        add_transaction.user = request.user
        add_transaction.save()
        TransactionsPermissions.objects.create(user=request.user, whom=request.user)
        if add_transaction.is_valid():
            add_transaction.save()
            lst= Transactions.objects.last()
            lst.user = request.user
            lst.save()

            return redirect(reverse("profile"))
    else:
        add_transaction = TransactionForm()

    return render(request, "add_transaction.html", {'add_transaction': add_transaction})

@login_required
def all_transactions(request):
    search_input = request.GET.get('search_area')
    if search_input:
        transactions = Transactions.objects.filter(full_name__icontains=search_input)
    else:
        search_input = ''
        cp = TransactionsPermissions.objects.filter(user=request.user)
        transactions = Transactions.objects.none()
        for c in cp:
            transactions |= Transactions.objects.filter(user=c.whom)
    return render(request, 'transactions.html', {'transactions':transactions, 'search_input': search_input})




