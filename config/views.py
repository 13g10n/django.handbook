from django.contrib.auth import get_user_model
from django.views.generic import TemplateView


class TestView(TemplateView):
    template_name = "test.html"

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data()


