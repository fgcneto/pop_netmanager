from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models.network_equipament import \
    Network, \
    Olt, \
    Cdi, \
    Ca1, \
    Switch, \
    Device, \
    Onu, \
    AccessPoint
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView
from sweetify.views import SweetifySuccessMixin
from django.urls import reverse_lazy
from ..list_descriptors import modules
from ..forms.network import \
    NetworkForm, \
    OltForm, \
    CdiForm, \
    Ca1Form, \
    DeviceForm, \
    SwitchForm, \
    OnuForm, \
    AccessPointForm
import sweetify


class NetworkCreateView(SweetifySuccessMixin, BSModalCreateView):

    template_name = 'core/single_create_modal.html'
    form_class = NetworkForm
    success_message = 'Cadastro Salvo'
    sweetify_options = {'text': 'Informações da Rede salvas com sucesso.',
                        'timer': 2500
                        }
    success_url = reverse_lazy('pop_netmanager:redes')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['parameters'] = modules.get('redes')
        return context


class NetworkUpdateView(SweetifySuccessMixin, BSModalUpdateView):

    template_name = 'core/single_create_modal.html'
    form_class = NetworkForm
    success_message = 'Cadastro Salvo'
    sweetify_options = {'text': 'Informações da Rede alteradas com sucesso.',
                        'timer': 2500
                        }
    success_url = reverse_lazy('pop_netmanager:redes')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['parameters'] = modules.get('redes')
        return context

    def get_queryset(self, **kwargs):
        return Network.objects.filter(pk=self.kwargs['pk'])


@login_required
def network_delete(request, pk):
    if id:
        Network.objects.filter(id=pk).delete()
        sweetify.success(request, 'Cadastro Excluído ',
                         text='Informações da Rede excluídas com \
                                 sucesso.', timer=1500)
        return redirect('pop_netmanager:redes')


class OltCreateView(SweetifySuccessMixin, BSModalCreateView):

    template_name = 'core/single_create_modal.html'
    form_class = OltForm
    success_message = 'Cadastro Salvo'
    sweetify_options = {'text': 'Informações da OLT salvas com sucesso.',
                        'timer': 2500
                        }
    success_url = reverse_lazy('pop_netmanager:olts')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['parameters'] = modules.get('olts')
        return context


class OltUpdateView(SweetifySuccessMixin, BSModalUpdateView):

    template_name = 'core/single_create_modal.html'
    form_class = OltForm
    success_message = 'Cadastro Salvo'
    sweetify_options = {'text': 'Informações da OLT alteradas com sucesso.',
                        'timer': 2500
                        }
    success_url = reverse_lazy('pop_netmanager:olts')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['parameters'] = modules.get('olts')
        return context

    def get_queryset(self, **kwargs):
        return Olt.objects.filter(pk=self.kwargs['pk'])


@login_required
def olt_delete(request, pk):
    if id:
        Olt.objects.filter(id=pk).delete()
        sweetify.success(request, 'Cadastro Excluído ',
                         text='Informações da OLT excluídas com \
                                 sucesso.', timer=1500)
        return redirect('pop_netmanager:olts')


class CdiCreateView(SweetifySuccessMixin, BSModalCreateView):

    template_name = 'core/single_create_modal.html'
    form_class = CdiForm
    success_message = 'Cadastro Salvo'
    sweetify_options = {'text': 'Informações da CDI salvas com sucesso.',
                        'timer': 2500
                        }
    success_url = reverse_lazy('pop_netmanager:cdis')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['parameters'] = modules.get('cdis')
        return context


class CdiUpdateView(SweetifySuccessMixin, BSModalUpdateView):

    template_name = 'core/single_create_modal.html'
    form_class = CdiForm
    success_message = 'Cadastro Salvo'
    sweetify_options = {'text': 'Informações da CDI alteradas com sucesso.',
                        'timer': 2500
                        }
    success_url = reverse_lazy('pop_netmanager:cdis')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['parameters'] = modules.get('cdis')
        return context

    def get_queryset(self, **kwargs):
        return Cdi.objects.filter(pk=self.kwargs['pk'])


@login_required
def cdi_delete(request, pk):
    if id:
        Cdi.objects.filter(id=pk).delete()
        sweetify.success(request, 'Cadastro Excluído ',
                         text='Informações da CD-I excluídas com \
                                 sucesso.', timer=1500)
        return redirect('pop_netmanager:cdis')


class Ca1CreateView(SweetifySuccessMixin, BSModalCreateView):

    template_name = 'core/single_create_modal.html'
    form_class = Ca1Form
    success_message = 'Cadastro Salvo'
    sweetify_options = {'text': 'Informações da CA-1 salvas com sucesso.',
                        'timer': 2500
                        }
    success_url = reverse_lazy('pop_netmanager:ca1s')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['parameters'] = modules.get('ca1s')
        return context


class Ca1UpdateView(SweetifySuccessMixin, BSModalUpdateView):

    template_name = 'core/single_create_modal.html'
    form_class = Ca1Form
    success_message = 'Cadastro Salvo'
    sweetify_options = {'text': 'Informações da Ca-1 alteradas com sucesso.',
                        'timer': 2500
                        }
    success_url = reverse_lazy('pop_netmanager:ca1s')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['parameters'] = modules.get('ca1s')
        return context

    def get_queryset(self, **kwargs):
        return Ca1.objects.filter(pk=self.kwargs['pk'])


@login_required
def ca1_delete(request, pk):
    if id:
        Ca1.objects.filter(id=pk).delete()
        sweetify.success(request, 'Cadastro Excluído ',
                         text='Informações da CA-1 excluídas com \
                                 sucesso.', timer=1500)
        return redirect('pop_netmanager:ca1s')


@login_required
def accesspoint_create(request):

    accesspoint_form = AccessPointForm(request.POST or None)

    if request.method == 'POST':
        if accesspoint_form.is_valid():
            accesspoint_form.save()
            sweetify.success(request, 'Cadastro Salvo', text='Informações \
                 do Access Point salvas com sucesso!', timer=3000)
            return redirect('pop_netmanager:accesspoints')

    context = {
        'accesspoint_form': accesspoint_form
    }

    return render(request, 'netmanager/accesspoint.html', context)


@login_required
def accesspoint_edit(request, pk):

    accesspoint = AccessPoint.objects.get(id=pk)
    accesspoint_form = AccessPointForm(
        request.POST or None, instance=accesspoint)

    if request.method == 'POST':
        if accesspoint_form.is_valid():
            accesspoint_form.save()
            sweetify.success(request, 'Cadastro Salvo', text='Informações \
                 do Access Point salvas com sucesso!', timer=3000)
            return redirect('pop_netmanager:accesspoints')

    context = {
        'accesspoint_form': accesspoint_form
    }

    return render(request, 'netmanager/accesspoint.html', context)


@login_required
def accesspoint_delete(request, pk):
    if id:
        AccessPoint.objects.filter(id=pk).delete()
        sweetify.success(request, 'Cadastro Excluído ',
                         text='Informações do Access Point excluídas com \
                                 sucesso.', timer=1500)
        return redirect('pop_netmanager:accesspoints')


@login_required
def onu_create(request):

    onu_form = OnuForm(request.POST or None)

    if request.method == 'POST':
        if onu_form.is_valid():
            onu_form.save()
            sweetify.success(request, 'Cadastro Salvo', text='Informações \
                 da ONU salvas com sucesso!', timer=3000)
            return redirect('pop_netmanager:onus')

    context = {
        'onu_form': onu_form
    }

    return render(request, 'netmanager/onu.html', context)


@login_required
def onu_edit(request, pk):

    onu = Onu.objects.get(id=pk)
    onu_form = OnuForm(request.POST or None, instance=onu)

    if request.method == 'POST':
        if onu_form.is_valid():
            onu_form.save()
            sweetify.success(request, 'Cadastro Salvo', text='Informações \
                 da ONU salvas com sucesso!', timer=3000)
            return redirect('pop_netmanager:onus')

    context = {
        'onu_form': onu_form
    }

    return render(request, 'netmanager/onu.html', context)


@login_required
def onu_delete(request, pk):
    if id:
        Onu.objects.filter(id=pk).delete()
        sweetify.success(request, 'Cadastro Excluído ',
                         text='Informações da ONU excluídas com \
                                 sucesso.', timer=1500)
        return redirect('pop_netmanager:onus')


@login_required
def switch_create(request):

    switch_form = SwitchForm(request.POST or None)

    if request.method == 'POST':
        if switch_form.is_valid():
            switch_form.save()
            sweetify.success(request, 'Cadastro Salvo', text='Informações \
                 do Switch salvas com sucesso!', timer=3000)
            return redirect('pop_netmanager:switches')

    context = {
        'switch_form': switch_form
    }

    return render(request, 'netmanager/switch.html', context)


@login_required
def switch_edit(request, pk):

    switch = Switch.objects.get(id=pk)
    switch_form = SwitchForm(request.POST or None, instance=switch)

    if request.method == 'POST':
        if switch_form.is_valid():
            switch_form.save()
            sweetify.success(request, 'Cadastro Salvo', text='Informações \
                 do Switch salvas com sucesso!', timer=3000)
            return redirect('pop_netmanager:switches')

    context = {
        'switch_form': switch_form
    }

    return render(request, 'netmanager/switch.html', context)


@login_required
def switch_delete(request, pk):
    if id:
        Switch.objects.filter(id=pk).delete()
        sweetify.success(request, 'Cadastro Excluído ',
                         text='Informações do Switch excluídas com \
                                 sucesso.', timer=1500)
        return redirect('pop_netmanager:switches')


class DeviceCreateView(SweetifySuccessMixin, BSModalCreateView):

    template_name = 'core/single_create_modal.html'
    form_class = DeviceForm
    success_message = 'Cadastro Salvo'
    sweetify_options = {'text': 'Informações da Reserva - \
                            IP Address salvas com sucesso.', 'timer': 2500}
    success_url = reverse_lazy('pop_netmanager:devices')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['parameters'] = modules.get('devices')
        return context


class DeviceUpdateView(SweetifySuccessMixin, BSModalUpdateView):

    template_name = 'core/single_create_modal.html'
    form_class = DeviceForm
    success_message = 'Cadastro Salvo'
    sweetify_options = {'text': 'Informações dos Dispositivos \
                            alteradas com sucesso.', 'timer': 2500
                        }
    success_url = reverse_lazy('pop_netmanager:devices')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['parameters'] = modules.get('devices')
        return context

    def get_queryset(self, **kwargs):
        return Device.objects.filter(pk=self.kwargs['pk'])


@login_required
def device_delete(request, pk):
    if id:
        Device.objects.filter(id=pk).delete()
        sweetify.success(request, 'Cadastro Excluído ',
                         text='Informações dos Dispositivos excluídas com \
                                 sucesso.', timer=1500)
        return redirect('pop_netmanager:devices')
