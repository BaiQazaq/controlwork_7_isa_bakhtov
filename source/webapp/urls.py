from django.urls import path


from webapp.views.base import IndexView
from webapp.views.record_create_view import RecordCreate #, RecordleDeleteView,  RecordView, RecordUpdateView,

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("record/add/", RecordCreate.as_view(), name = 'record_add'),
    
]

# path("articles/add/", ArticleCreate.as_view(), name = 'article_add'),
#     path("articles/<int:pk>/update/", ArticleUpdateView.as_view(), name= "article_update"),
#     path("articles/<int:pk>/delete/", ArticleDeleteView.as_view(), name= "article_delete"),
#     path("articles/<int:pk>/confirm_delete/", ArticleDeleteView.as_view(), name= "confirm_delete"),
#     path("articles/", IndexView.as_view()),
#     path("articles/<int:pk>", ArticleView.as_view(), name = 'article_detail')   