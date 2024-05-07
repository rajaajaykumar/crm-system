from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("record/<int:pk>/", views.view_record, name="view-record"),
    path("record/create/", views.create_record, name="create-record"),
    path("record/<int:pk>/update", views.update_record, name="update-record"),
    path("record/<int:pk>/delete", views.delete_record, name="delete-record"),
]
