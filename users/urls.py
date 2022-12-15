from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    Me,
    Users,
    PublicUser,
    ChangePassword,
    LogIn,
    LogOut,
    PublicUserReviews,
    JWTLogIn,
    GithubLogIn,
    KakaoLogIn,
    NaverLogIn,
    SignUp,
)

urlpatterns = [
    path("", Users.as_view()),
    path("sign-up", SignUp.as_view()),
    path("me", Me.as_view()),
    path("change-password", ChangePassword.as_view()),
    path("log-in", LogIn.as_view()),
    path("log-out", LogOut.as_view()),
    path("token-login", obtain_auth_token),
    path("jwt-login", JWTLogIn.as_view()),
    path("github", GithubLogIn.as_view()),
    path("kakao", KakaoLogIn.as_view()),
    path("naver", NaverLogIn.as_view()),
    path("@<str:username>", PublicUser.as_view()),
    path("@<str:username>/reviews", PublicUserReviews.as_view()),
]
