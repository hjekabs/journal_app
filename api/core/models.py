from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(BaseModel):
    DAY_RATING = (
        ("Terrible", "Terrible"),
        ("Bad", "Bad"),
        ("Average", "Average"),
        ("Good", "Good"),
        ("Great", "Great"),
    )
    body_text = models.TextField()
    day_rating = models.CharField(choices=DAY_RATING, max_length=20)
    audio_message = models.TextField(null=True)
