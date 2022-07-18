# from django.db import models
#
#
# class Store(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=800)
#     rating = models.IntegerField()
#
#     class Meta:
#         db_table = 'stores'

from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=800)
    rating = models.IntegerField()
    owner = models.ForeignKey(
        'auth.User',
        related_name='stores',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'stores'
