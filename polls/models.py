from django.db import models
from django.db.models.fields.related import ForeignKey

class Poll(models.Model):
    title = models.CharField('Название', max_length=200)
    start_date = models.DateField('Дата начала')
    end_date = models.DateField('Дата окончания')
    description = models.CharField('Описание', max_length=500)
    
    def __str__(self):
        return self.title


class AnswerType(models.Model):
    TEXT = 'Text'
    SINGLE = 'Single'
    MULTI = 'Multi'
    CHOICES = [
        (TEXT, 'текстом'),
        (SINGLE, 'выбор одного варианта'),
        (MULTI, 'выбор нескольких вариантов')
    ]


class Question(models.Model):
    poll= models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_text = models.CharField('Текст вопроса', max_length=200)
    answer_type = models.CharField(
        'Тип ответа',
        max_length = 6,
        choices=AnswerType.CHOICES,
        default = AnswerType.TEXT
    )

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField('Формулировка варианта ответа', max_length=100)

    def __str__(self):
        return self.answer_text


class User(models.Model):
    email = models.CharField(max_length=20)
    
    # ;-)
    password = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.email



class Choice(models.Model):
    user_id = models.IntegerField(default=0)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)