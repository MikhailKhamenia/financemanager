from django.urls import path
from .views import SignUpView
from .views import LoginView
from .views import ProfilePage
from .views import ActionPage
from .views import CryptPage
from .views import LogoutView
from .views import transaction_form, all_transactions

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name="login"),
    path('profile/', ProfilePage.as_view(), name="profile"),
    path('actions/', ActionPage.as_view(), name="actions"),
    path('crypt/', CryptPage.as_view(), name="crypt"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('transactions/', all_transactions, name='all_transactions'),
    path('add_transaction/', transaction_form, name='add_transaction'),

]