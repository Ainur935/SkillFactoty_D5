from django_filters import FilterSet, CharFilter, DateFilter
from .models import Post



class PostFilter(FilterSet):
    time_filter = DateFilter(field_name = 'creation_time', lookup_expr='gt', label='Опубликовано после ')
    title_filter = CharFilter(field_name= 'heading', lookup_expr='icontains', label='Заголовок')
    author_filter = CharFilter(field_name='author__user__username', lookup_expr='icontains', label='Автор')
    class Meta:
        model = Post
        fields = ('time_filter', 'title_filter', 'author_filter')

