from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path("", views.home),
    path("about/", views.about),
    path("post_list/", views.post_list, name='post_list'),
    # path("post_list/", views.PostListView.as_view(), name='post_list'), # Building Class Based Views
    path("<int:year>/<int:month>/<int:day>/<slug:post>/",
         views.post_details, name='post_details'),
    path("<int:post_id>/share/", views.post_share, name='post_share'),


]
