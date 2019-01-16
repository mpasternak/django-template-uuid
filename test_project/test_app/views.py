from django.shortcuts import render
from django.views.generic import TemplateView


class Root(TemplateView):
    template_name = "root.html"
