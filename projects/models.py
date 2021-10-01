from django.db import models
from django.db.models.fields import CharField, DateTimeField
import uuid
# Create your models here.

class Tag(models.Model):
    name = CharField(max_length=100, blank=True, null=True)
    created       = DateTimeField(auto_now_add=True)
    id            = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Tag'

class Projects(models.Model):
    title         = models.CharField(max_length=200, null=True, blank=True)
    description   = models.TextField(null=True, blank=True)
    demo_link     = models.CharField(max_length=200, blank=True, null=True)
    source_link   = models.CharField(max_length=200, blank=True, null=True)
    vote_ratio    = models.IntegerField(blank=True, null=True)
    vote_count    = models.IntegerField(blank=True, null=True) 
    tags          = models.ManyToManyField(Tag, blank=True) 
    created       = DateTimeField(auto_now_add=True)
    id            = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Projects'
        ordering  = ['-created']


class Review(models.Model):
    VOTE_TYPE = (
        ('up','Up Vote'),
        ('down','Down Vote'),
    )

    owner = models.ForeignKey(Projects, on_delete=models.CASCADE) 
    vote = models.CharField(max_length=200,choices=VOTE_TYPE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)


    created       = DateTimeField(auto_now_add=True)
    id            = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)

    def __str__(self):
        return self.vote

    class Meta:
        # Remove the 's' in the admin panel
        verbose_name_plural = 'Review'