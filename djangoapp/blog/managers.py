from django.db import models


class PostManager(models.Manager):
    def get_published(self):
        return self.filter(is_published=True).order_by('-pk')
