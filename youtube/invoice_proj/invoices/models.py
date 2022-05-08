import imp
from django.db import models
from profiles.models import Profile
from receivers.models import Receiver


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

# Create your models here.
class Invoice(models.Model):
    """
    
    """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    number = models.CharField(max_length=150)
    completion_date = models.DateField()
    issue_date = models.DateField()
    payment_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    # if closed == True then
    closed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)

    
    def __str__(self) -> str:
        return f"Invoice Number {self.number}, pk: {self.pk}"
    @property
    def get_tags(self):
        return self.tags.all()
    @property
    def get_positions(self):
        return self.position_set.all()
    @property
    def get_total_amount(self):
        total = 0
        qs = self.get_positions
        for pos in qs:
            total += pos.amount # 
        return total