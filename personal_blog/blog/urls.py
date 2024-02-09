from django.urls import path, include
from .views import Index, DetailArticleView, DeleteArticleView, LikeArticle, Featured, CommentArticle, DeleteCommentView

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', Index.as_view(), name='index'),
    path('<int:pk>/', DetailArticleView.as_view(), name='detail_article'),
    path('<int:pk>/like', LikeArticle.as_view(), name='like_article'),
    path('<int:pk>/comment_article', CommentArticle.as_view(), name='comment_article'),
    path('featured/', Featured.as_view(), name='featured'),
    path('<int:pk>/delete', DeleteArticleView.as_view(), name='delete_article'),
    path('comments/<int:pk>/delete/', DeleteCommentView.as_view(), name='delete_comment'),
]
