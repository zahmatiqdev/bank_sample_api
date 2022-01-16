from django.urls import path

from .views import AccountListAPIView, AccountAPIDetailView


app_name = 'bank'

urlpatterns = [
    # This url for create & list data 
    path("account/", AccountListAPIView.as_view(), name="create"),

    # This url for retrieve & update & delete data
    path("account/<int:pk>/", AccountAPIDetailView.as_view(), name="detail"),
]
