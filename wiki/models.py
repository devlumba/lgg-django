from django.db import models


class FeedbackPost(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    content = models.TextField()

    def __str__(self):
        return self.name, self.date
