from rest_framework import serializers
from api_polls.models import Polls, Questions, UsersTextAnswers


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'


class UsersTextAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersTextAnswers
        fields = '__all__'


class PollsSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True,
                                               view_name='api_polls:polls-detail')
    questions_display = QuestionsSerializer(many=True, read_only=True, source='questions')

    class Meta:
        model = Polls
        fields = ['id', 'name', 'url', 'start_date', 'finish_date',  'questions_display']
