from django.urls import path
from .views import PostsList,OnePost,NewsSearch,Add

urlpatterns = [
    path('',PostsList.as_view()),
    path('<int:pk>',OnePost.as_view()),
    path('search',NewsSearch.as_view()),
    path('add',Add.as_view())
]

