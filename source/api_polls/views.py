from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from datetime import datetime

from api_polls.serializers import PollsSerializer, UsersTextAnswersSerializer
from api_polls.models import Polls, UsersTextAnswers


class PollsViewSet(ViewSet):
    queryset = Polls.objects.all()

    def list(self, request):
        today = datetime.today()
        objects = Polls.objects.filter(start_date__lte=today, finish_date__gte=today)
        slr = PollsSerializer(objects, many=True, context={'request': request})
        return Response(slr.data)

    def retrieve(self, request, pk=None):
        article = get_object_or_404(Polls, pk=pk)
        slr = PollsSerializer(article, context={'request': request})
        return Response(slr.data)


class AnswerViewSet(ViewSet):
    queryset = UsersTextAnswers.objects.all()

    def create(self, request):
        slr = UsersTextAnswersSerializer(data=request.data, context={'request': request})
        if slr.is_valid():
            slr.save()
            return Response(slr.data)
        else:
            return Response(slr.errors, status=400)

