"""
Module containg the Search class
"""


from django.db import models
import uuid

# Create your models here.

class Search(models.Model):
    """
    Search model
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    keyword = models.CharField(max_length=256, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    results = models.IntegerField()

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        """string representation

        Returns:
            str: string representation
        """
        return "[{}]: ({}) {}".format(self.__name__, self.id, self.keyword)
