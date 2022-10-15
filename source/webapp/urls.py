from django.urls import path


from webapp.views.base import IndexView
from webapp.views.record_create_view import RecordCreate
from webapp.views.record_edit_view import RecordEditView
from webapp.views.record_delete_view import RecordDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("record/add/", RecordCreate.as_view(), name = 'record_add'),
    path("record/<int:pk>/edit/", RecordEditView.as_view(), name= "record_edit"),
    path("articles/<int:pk>/delete/", RecordDeleteView.as_view(), name= "record_delete"),
    path("articles/<int:pk>/confirm_delete/", RecordDeleteView.as_view(), name= "confirm_delete")
    
]


#     path("articles/<int:pk>/update/", ArticleUpdateView.as_view(), name= "article_update"),
#     path("articles/<int:pk>/delete/", ArticleDeleteView.as_view(), name= "article_delete"),
#     path("articles/<int:pk>/confirm_delete/", ArticleDeleteView.as_view(), name= "confirm_delete"),
#     path("articles/", IndexView.as_view()),
#     path("articles/<int:pk>", ArticleView.as_view(), name = 'article_detail')   