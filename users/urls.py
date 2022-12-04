from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from users.views import SignupView, SigninView, SignoutView

urlpatterns = [
    path('sign-up/', SignupView.as_view()),
    path('sign-in/', csrf_exempt(SigninView.as_view())),
    path('sign-out/', SignoutView.as_view()),
]
