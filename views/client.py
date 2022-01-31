from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView
from sweetify.views import SweetifySuccessMixin
from django.urls import reverse_lazy
from ..list_descriptors import modules
from ..models.client import Client
from ..forms.client import ClientForm


class ClientCreateView(SweetifySuccessMixin, BSModalCreateView):

    template_name = 'core/single_create_modal.html'
    form_class = ClientForm
    success_message = 'Cadastro Salvo'
    sweetify_options = {'text': 'Informações do Cliente salvas com sucesso.',
                        'timer': 2500
                        }
    success_url = reverse_lazy('pop_netmanager:clientes')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['parameters'] = modules.get('clientes')
        return context


class ClientUpdateView(SweetifySuccessMixin, BSModalUpdateView):

    template_name = 'core/single_create_modal.html'
    form_class = ClientForm
    success_message = 'Cadastro Salvo'
    sweetify_options = {'text': 'Informações do Cliente \
                        alteradas com sucesso.',
                        'timer': 2500
                        }
    success_url = reverse_lazy('pop_netmanager:clientes')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['parameters'] = modules.get('clientes')
        return context

    def get_queryset(self, **kwargs):
        return Client.objects.filter(pk=self.kwargs['pk'])
