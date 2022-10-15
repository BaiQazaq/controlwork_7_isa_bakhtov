from django.views.generic import UpdateView
from django.urls import reverse_lazy

from webapp.forms import RecordForm
from webapp.models import Record



class RecordEditView(UpdateView):
    template_name = 'record_edit.html'
    form_class = RecordForm
    model = Record
    pk_url_kwarg = 'pk'
    context_object_name = 'record'
    success_url = reverse_lazy('index')
    
    