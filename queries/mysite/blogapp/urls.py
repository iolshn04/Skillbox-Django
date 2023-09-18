from django.urls import path


from .views import ArticlesListView

app_name = "myauth"

urlpatterns = [
    path("article/", ArticlesListView.as_view(), name="articles"),
]