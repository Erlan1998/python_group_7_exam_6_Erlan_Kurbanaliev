from django.db import models

status_choices = [('active', 'Активно'), ('blocked', 'Заблокировано')]
# Create your models here.

class Guest(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    mail = models.EmailField(max_length=100)
    description = models.TextField(max_length=2000, null=False, blank=False)
    date_creat = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    date_update = models.DateTimeField(auto_now=True, editable=True, blank=True)
    status = models.CharField(max_length=100, null=False, blank=False, default='active', choices=status_choices)

    class Meta:
        db_table = 'Books'
        verbose_name = 'Гость'
        verbose_name_plural = 'Гости'

    def __str__(self):
        return f'{self.id}. {self.date_creat}: {self.name}'
