from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from .models import Frontpage


class FrontpageDetail(DetailView):
    template_name = 'index.html'

    def get_object(self, *args, **kwargs):
        if 'pk' in self.kwargs:
            get_object_or_404(Frontpage, pk=self.kwargs['pk'])
        return get_object_or_404(Frontpage, activated=True)