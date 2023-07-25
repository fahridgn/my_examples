from django.urls import path
from .views import SignUpView, UsersLoginHomeView

urlpatterns=[
    path('signup/', SignUpView.as_view(),name='signup'),
    path('', UsersLoginHomeView.as_view(),name='home'),
]