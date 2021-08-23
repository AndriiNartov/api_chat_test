from django.db import models
from .validators import CONTENT_TEXT_LENGTH_VALIDATOR, EMAIL_VALIDATOR


class Message(models.Model):

    author_email = models.EmailField(validators=[EMAIL_VALIDATOR], verbose_name='Author email')
    content_text = models.TextField(
        validators=[CONTENT_TEXT_LENGTH_VALIDATOR],
        verbose_name='Message text'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date of update')

    def __str__(self):
        return f'Message_{self.id}, created {self.created_at.strftime("%Y-%m-%d, %H:%M:%S")}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ['-created_at']
