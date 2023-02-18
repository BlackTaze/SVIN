from django.urls import path

from .views import index, news, rules, contacts, RegisterUser, LoginUser, logout_user, submit_review, review_list


urlpatterns = [ 
    path("", index, name="index"), 
    path("news/", news ,name="news" ),
    path("rules/", rules, name="rules"),
    path("contacts/", contacts, name="contacts"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path('submit-review/', submit_review, name='submit_review'),
    path("reviews/",review_list, name="reviews")
    ]