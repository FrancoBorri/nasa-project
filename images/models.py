from django.db import models


class Astronomical_images(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    date = models.DateField()
    description = models.TextField()


class Meta:
    db_table = "astronomical_images"


class Favourite_images(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    astronomical_images = models.ForeignKey(
        "images.Astronomical_images", on_delete=models.CASCADE
    )
    saved_at = models.DateTimeField(auto_now_add=True)


class Meta:
    db_table = "favourite_images"
