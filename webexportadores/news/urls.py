from django.urls import path
from . import views
from .views import PostsListView, PostDetailView, CategoryListView, PostCreateView, PostUpdateView

urlpatterns = [
    path('', PostsListView.as_view(), name="news"),
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),
    path('category/<int:pk>/', CategoryListView.as_view(), name='category'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='update'),
]
