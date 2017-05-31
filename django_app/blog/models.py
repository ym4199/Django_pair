import datetime

from django.utils import timezone

from django.db import models

# Create your models here.


class Question(models.Model):
    author = models.ForeignKey('auth.User', null=True)
    question_title = models.CharField(max_length=200, null=True)
    question_text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now, null=True
    )
    pub_date = models.DateTimeField('date published',
                                    blank=True, null=True)

    def __str__(self):
        return self.question_title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
