from django.urls import path
from .views import ArticleList, ArticleDetails

urlpatterns = [
	path('articles/', ArticleList.as_view()),
	path('articles/<int:pk>/', ArticleDetails.as_view()),

    # path('articles', article_list),
    # path('articles/<int:pk>/', article_details),
]