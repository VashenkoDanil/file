from django.views.generic import TemplateView
from django.shortcuts import redirect


class MultipleFilesView(TemplateView):
    template_name = "file/sending_multiple_files.html"

    def post(self, request, *args, **kwargs):
        return redirect('/')
