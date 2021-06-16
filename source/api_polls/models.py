from django.db import models


QUESTION_TYPE_TEXT = 'answer with text'
QUESTION_TYPE_CHOICE_ONE = 'choice one answer'
QUESTION_TYPE_CHOICE_MANY = 'multiple choice answer'
QUESTION_TYPE_CHOICES = (
    (QUESTION_TYPE_TEXT, 'answer with text'),
    (QUESTION_TYPE_CHOICE_ONE, 'choice one answer'),
    (QUESTION_TYPE_CHOICE_MANY, 'multiple choice answer')
)


class Polls(models.Model):
    name = models.CharField(max_length=50, verbose_name="Poll")
    start_date = models.DateTimeField(auto_now_add=True, verbose_name='Start time')
    finish_date = models.DateTimeField(verbose_name='Finish time', blank=True)
    description = models.TextField(max_length=3000, verbose_name='Description')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Poll'
        verbose_name_plural = 'Polls'


class Questions(models.Model):
    poll = models.ForeignKey('api_polls.Polls', verbose_name='Poll', related_name='questions',
                             on_delete=models.CASCADE)
    text = models.TextField(max_length=2500, verbose_name='Text')
    questions_type = models.CharField(max_length=35, choices=QUESTION_TYPE_CHOICES, default=QUESTION_TYPE_TEXT,
                                      verbose_name='Type')

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class UsersTextAnswers(models.Model):
    question = models.ForeignKey('api_polls.Questions', verbose_name='question', related_name='answer',
                                 on_delete=models.CASCADE)
    answer = models.TextField(max_length=3500, verbose_name='Users text answer')
    user_id = models.IntegerField(verbose_name='User id')

    def __str__(self):
        return f'{self.answer}'

    class Meta:
        verbose_name = 'Users Answer'
        verbose_name_plural = 'Users Answers'
