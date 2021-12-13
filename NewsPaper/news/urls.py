from django.urls import path
from .views import PostList, PostDetail, PostSearchList, PostCreateList, PostUpdateList, PostDeleteList

urlpatterns =[
    path('',PostList.as_view()),
    path('<int:pk>',PostDetail.as_view(), name = 'post_detail'),
    path('search', PostSearchList.as_view()),
    path('add', PostCreateList.as_view(), name='add'),
    path('<int:pk>/edit', PostUpdateList.as_view(), name='edit'),
    path('<int:pk>/delete', PostDeleteList.as_view(), name='post_delete'),
]