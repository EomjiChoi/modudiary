from venv import create
from django.urls import path


from landing import views
# 인터넷 주소창에 넣는 주소에 관여하는 것은 여기에서 결정



app_name="landing"
urlpatterns = [

    path("index", views.index, name="home"),
    path("create/", views.post_create, name="create"),
    path("read-all/", views.post_read_all, name="read_all"),
    path("read/<int:post_id>/", views.post_read, name="read"),
    path("update/<int:post_id>/", views.post_update, name="update"),
    path("delete/<int:post_id>/", views.post_delete, name="delete"),
    path("temptest/", views.temp_test),
    path("path-test/<int:i>/<int:j>/", views.temp_test, name="url_test"),


]