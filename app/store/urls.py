from django.urls import path

from . import views

app_name = "store"

urlpatterns = [
    path("", views.home, name="home"),
    path("test/", views.test, name="test"),
    path("upload/", views.Fileuploadrederer, name="upload"),
    path("mouth/", views.Mouthrederer, name="mouth"),
    path("files/", views.list_of_files, name="files"),
    path("list_of_mouth/", views.list_of_mouth, name="list_of_mouth"),
    path("list_of_admin_mouth/", views.list_of_admin_mouth, name="list_of_admin_mouth"),
    path("use/", views.use, name="use"),
    path("video_details/<slug:slug>/", views.video_details, name="video_details"),
    path("mouth_details/<slug:slug>/", views.mouth_details, name="mouth_details"),
    path("question/", views.Questionrederer, name="question"),
    path("about/", views.Aboutrederer, name="about"),
    path("blog/", views.Blog_list, name="blog_list"),
    path("blog_details/<slug:slug>/", views.blog_details, name="blog_details"),
]

