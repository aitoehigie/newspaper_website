from django.urls import path

from . import views

urlpatterns = [
        path('create_article/', views.ArticleCreateView.as_view(), name="create_article"),
	path('', views.ArticleListView.as_view(), name='article_list'),
        path('<int:pk>/edit/', views.ArticleUpdateView.as_view(), name = "article_edit"),
	path('<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
	path('<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
]
