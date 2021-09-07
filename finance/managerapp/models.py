from django.db import models
import datetime
from django.contrib.auth.forms import User


class Transactions(models.Model):
    CHOICES=(
        ('Food','Food'),
        ('House', 'House'),
        ('Entertainments', 'Entertainments'),
        ('Transport', 'Transport'),
        ('Other', 'Other'),
    )
    transaction_sum = models.IntegerField()
    comment = models.CharField(max_length=128, choices=CHOICES)
    date = models.DateField(default=datetime.date.today())
    user = models.ForeignKey(User, related_name='User',on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f'{self.comment} {self.transaction_sum} {self.date}'


    class Meta:
        verbose_name="Транзакция"
        verbose_name_plural="Транзакции"

class TransactionsPermissions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    whom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='whom')

    class Meta:
        verbose_name="Транзакции пользователя"
        verbose_name_plural="Транзакции пользователей"



