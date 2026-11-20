from django.views.generic import TemplateView


class CatalogView(TemplateView):
    template_name = "catalog/catalog.html"


class ProductDetailsView(TemplateView):
    template_name = "catalog/product-details.html"
