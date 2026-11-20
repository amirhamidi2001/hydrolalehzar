from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "website/index.html"


class AboutView(TemplateView):
    template_name = "website/about.html"


class ContactView(TemplateView):
    template_name = "website/contact.html"


class FaqView(TemplateView):
    template_name = "website/faq.html"


class PrivacyView(TemplateView):
    template_name = "website/privacy.html"


class SupportView(TemplateView):
    template_name = "website/support.html"


class TosView(TemplateView):
    template_name = "website/tos.html"


class PageNotFoundView(TemplateView):
    template_name = "website/404.html"

