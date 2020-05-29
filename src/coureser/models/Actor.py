from django.db import models


class Actor(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName + " " + self.lastName