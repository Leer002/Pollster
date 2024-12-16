from django.db import models
from django.utils.translation import gettext_lazy as _ 

class Question(models.Model):
    question_text = models.CharField(_("question"), max_length=200)
    pub_date = models.DateTimeField(_("date published"))

    def __str__(self):
        return self.question_text
    

class Choice(models.Model):
    question = models.ForeignKey(Question, verbose_name=_("question"), on_delete=models.CASCADE)
    choice_text = models.CharField(_("choice"), max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
