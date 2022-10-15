from django.utils import timezone
from django.db import models
from django.db.models import TextChoices


# Create your models here.
class StatusChoices(TextChoices):
    ACTIVE = 'active', 'Активна'
    NOT_ACTIVE = 'blocked', 'Заблокировано'
    
    
class Record(models.Model):
    author = models.CharField(verbose_name='Автор', max_length=50, null=False, blank=False, default="No name")
    email = models.EmailField(verbose_name = 'Почта', max_length=256, null=False, blank=False)
    text = models.TextField(verbose_name='Текст', max_length=2000, null=False, blank=False)
    status = models.CharField(verbose_name='Статус', choices=StatusChoices.choices, max_length=100, default=StatusChoices.ACTIVE)
    is_deleted = models.BooleanField(verbose_name="Удалено", default=False, null=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, default=None)
    
    
    def __str__(self):
        return f"{self.author} - {self.email} - {self.text}"
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        
    
    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()