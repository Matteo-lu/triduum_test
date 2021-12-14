from django.db import models
import uuid

# Create your models here.

class Search(models.Model):
    """[summary]

    Args:
        models ([type]): [description]
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    keyword = models.CharField(max_length=256, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    results = models.IntegerField()

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return "[{}]: ({}) {}".format(self.__name__, self.id, self.keyword)
