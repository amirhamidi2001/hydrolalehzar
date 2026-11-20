from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.CatalogView.as_view(), name="catalog"),
    path("details/", views.ProductDetailsView.as_view(), name="product-details"),
]
