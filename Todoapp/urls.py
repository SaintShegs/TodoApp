from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

from .views import *


app_name='todos'

urlpatterns=[
    path('', LoginView.as_view(), name="Login"),

    path('logout/', LogoutView.as_view(next_page='todos:Login'), name='Logout'),

    path('signup/', SignupView.as_view(), name='signup'),


    path('change-password/', PasswordChangeView.as_view(template_name='registration/changepassword.html'), name='pswdchange'),


    path('task_lists/', todo_list),
    path('pending/', todo_pending),
    path('completed/', todo_completed),
    path('create/', todo_create),
    path('<id>/', todo_detail),
    path('<id>/update/', todo_update),
    path('<id>/delete/', todo_delete)
]