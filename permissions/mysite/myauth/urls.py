from django.urls import path
from django.contrib.auth.views import LoginView


from .views import (
    AboutMeView,
    MyLogoutView,
    get_session_view,
    get_cookie_view,
    set_cookie_view,
    set_session_view,
    RegisterView,
)

app_name = "myauth"

urlpatterns = [
    path("about-me/", AboutMeView.as_view(), name="about-me"),
    path("login/",
             LoginView.as_view(
                 template_name="myauth/login.html",
                 redirect_authenticated_user=True,
             ),
             name="login",
        ),
    path("logout/", MyLogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("cookie/get/", get_cookie_view, name="cookie-get"),
    path("cookie/set/", set_cookie_view, name="cookie-set"),
    path("session/get/", get_session_view, name="session-get"),
    path("session/set/", set_session_view, name="session-set"),
]
