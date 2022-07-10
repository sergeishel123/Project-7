from django_filters import FilterSet

from .models import Post

class PostFilter(FilterSet):

    class Meta:

        model = Post

        fields = {
                  'heading': ['icontains'],
                  'author_post__user__username': ['icontains'],
                  'time_in' : ['gte']
                  }