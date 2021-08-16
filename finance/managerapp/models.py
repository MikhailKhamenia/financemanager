import time
from django.db import models
"""самая важная таблица
   транзакции, которая будет содержать
   записи о получении денег, затрате денег
   тип транзакции - Приход/расход (Transactions_types)
   тип источника - карта, наличные и т.д. (Source_types)
   дата в формате Год-месяц-день
   сумма транзакции
   описание, например - "Купил XBox"""
class Transactions(models.Model):
    transaction_sum = models.IntegerField()
    comment = models.CharField(max_length=128, default='food')
    date = models.DateField()
    def __str__(self):
        return f'{self.comment} {self.transaction_sum} {self.date}'


    class Meta:
        verbose_name="Транзакция"
        verbose_name_plural="Транзакции"



