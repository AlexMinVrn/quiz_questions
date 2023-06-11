from django.db import models


class Questions(models.Model):
    """Модель для вопросов."""
    id_question = models.CharField(max_length=100)
    text_question = models.TextField(unique=True)
    text_answer = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
