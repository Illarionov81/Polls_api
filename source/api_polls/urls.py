from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_polls.views import PollsViewSet, AnswerViewSet

app_name = 'api_polls'

router = DefaultRouter()
router.register(r'polls', PollsViewSet)
router.register(r'answers', AnswerViewSet)


urlpatterns = [
    path('', include(router.urls))
]
