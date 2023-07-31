from django.db import models


class IsPublishedManager(models.Manager):
    def get_published(self):
        return self.filter(is_published=True).order_by('-pk')
