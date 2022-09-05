from django.urls import path
from .views import index_page

urlpatterns = [
    path("accounts/profile/", index_page, name="index")
]