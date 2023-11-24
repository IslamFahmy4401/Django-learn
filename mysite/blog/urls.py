from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path("", views.home),
    path("about/", views.about),
    path("post_list/", views.post_list, name='post_list'),
    path("<int:id>/", views.post_details, name='post_details')

]