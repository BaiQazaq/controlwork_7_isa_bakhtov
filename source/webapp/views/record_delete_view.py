from django.views.generic import DeleteView
from django.urls import reverse_lazy

from webapp.models import Record


class RecordDeleteView(DeleteView):
    template_name = 'record_confirm_delete.html'
    model = Record
    success_url = reverse_lazy('index')