from __future__ import unicode_literals
import json
import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		return timezone.now() - datetime.timedelta(days = 1) <=self.pub_date <= timezone.now()
	was_published_recently.admin_order_field = "pub_date"
	was_published_recently.boolean = True
	was_published_recently.short_description = "Published recently?"
class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)
	def __str__(self):
		return self.choice_text

class QuestionEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, Question):
			return {
					'question': obj.question_text,
					'date': str(obj.pub_date)
			}
		return json.JSONEncoder.default(self, obj)

# Create your models here.
