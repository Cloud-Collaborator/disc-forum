from API.views import CreateUserView, ThreadDetailView, ThreadListCreateView, TopicCreateListView, TopicDetailView, UserDetailView
from django.urls import path, include

urlpatterns = [
    path('user/', CreateUserView.as_view()),
    path('user/<int:pk>', UserDetailView.as_view()),
    path('threads/', ThreadListCreateView.as_view()),
    path('threads/<int:pk>', ThreadDetailView.as_view()),
    path('topics/', TopicCreateListView.as_view()),
    path('topics/<int:pk>', TopicDetailView.as_view()),
]
