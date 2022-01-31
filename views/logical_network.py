from django.shortcuts import render, redirect
from pop_erp.apps.core.list_descriptors import \
    search_list_descriptors_by_application
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from ..models.network_equipament import \
    Vman, \
    Cvlan, \
    Svlan, \
    Firewall, \
    Vlan_management_ap, \
    Vlan_management_sw, \
    Vlan_management_onu, \
    Line_profile
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView
from sweetify.views import SweetifySuccessMixin
from django.urls import reverse_lazy
from ..list_descriptors import modules
from ..forms.network import \
    VmanForm, \
    CvlanForm, \
    SvlanForm, \
    FirewallForm, \
    VlanapForm, \
    VlanswForm, \
    VlanonuForm, \
    Line_profileForm
import sweetify


@login_required
def firewall_create(request):

    firewall_form = FirewallForm(request.POST or None)

    if request.method == 'POST':
        if firewall_form.is_valid():
            firewall_form.save()
            sweetify.success(request, 'Cadastro Salvo', text='Informações \
                 do Firewall salvas com sucesso!', timer=3000)
            return redirect('pop_netmanager:firewalls')

    context = {
        'firewall_form': firewall_form
    }

    return render(request, 'netmanager/firewall.html', context)


@login_required
def firewall_edit(request, pk):

    firewall = Firewall.objects.get(id=pk)
    firewall_form = FirewallForm(request.POST or None, instance=firewall)

    if request.method == 'POST':
        if firewall_form.is_valid():
            firewall_form.save()
            sweetify.success(request, 'Cadastro Salvo', text='Informações \
                 do Firewall salvas com sucesso!', timer=3000)
            return redirect('pop_netmanager:firewalls')

    context = {
        'firewall_form': firewall_form
    }

    return render(request, 'netmanager/firewall.html', context)


@login_required
def firewall_delete(request, pk):
    if id:
        Firewall.objects.filter(id=pk).delete()
        sweetify.success(request, 'Cadastro Excluído ',
                         text='Informações do Firewall excluídas com \
                                 sucesso.', timer=1500)
        return redirect('pop_netmanager:firewalls')


@login_required
def vlanap_create(request):

    vlanap_form = VlanapForm(request.POST or None)

    if request.method == 'POST':
        if vlanap_form.is_valid():
            vlanap_form.save()
            sweetify.success(request, 'Cadastro Salvo', text='Informações \
                 da VLAN de Gerência-AP salvas com sucesso!', timer=3000)
            return redirect('pop_netmanager:vlanaps')

    context = {
        'vlanap_form': vlanap_form
    }

    return render(request, 'netmanager/vlan_management_ap.html', context)


@login_required
def vlanap_edit(request, pk):

    vlanap = Vlan_management_ap.objects.get(id=pk)
    vlanap_form = VlanapForm(request.POST or None, instance=vlanap)

    if request.method == 'POST':
        if vlanap_form.is_valid():
            vlanap_form.save()
            sweetify.success(request, 'Cadastro Salvo', text='Informações \
                 da VLAN Gerência-AP salvas com sucesso!', timer=3000)
            return redirect('pop_netmanager:vlanaps')

    context = {
        'vlanap_form': vlanap_form
    }

    return render(request, 'netmanager/vlan_management_ap.html', context)


@login_required
def vlanap_delete(request, pk):
    if id:
        Vlan_management_ap.objects.filter(id=pk).delete()
        sweetify.success(request, 'Cadastro Excluído ',
                         text='Informações da VLAN Gerência-AP excluídas com \
                                 sucesso.', timer=1500)
        return redirect('pop_netmanager:vlanaps')


@login_required
def vlansw_create(request):

    vlansw_form = VlanswForm(request.POST or None)

    if request.method == 'POST':
        if vlansw_form.is_valid():
            vlansw_form.save()
            sweetify.success(request, 'Cadastro Salvo', text='Informações \
                 da VLAN Gerência-SW salvas com sucesso!', timer=3000)
            return redirect('pop_netmanager:vlansws')

    context = {
        'vlansw_form': vlansw_form
    }

    return render(request, 'netmanager/vlan_management_sw.html', context)


@login_required
def vlansw_edit(request, pk):

    vlansw = Vlan_management_sw.objects.get(id=pk)
    vlansw_form = VlanswForm(request.POST or None, instance=vlansw)

    if request.method == 'POST':
        if vlansw_form.is_valid():
            vlansw_form.save()
            sweetify.success(request, 'Cadastro Salvo', text='Informações \
                 da VLAN Gerência-SW salvas com sucesso!', timer=3000)
            return redirect('pop_netmanager:vlansws')

    context = {
        'vlansw_form': vlansw_form
    }

    return render(request, 'netmanager/vlan_management_sw.html', context)


@login_required
def vlansw_delete(request, pk):
    if id:
        Vlan_management_sw.objects.filter(id=pk).delete()
        sweetify.success(request, 'Cadastro Excluído ',
                         text='Informações da VLAN Gerência-SW excluídas com \
                                 sucesso.', timer=1500)
        return redirect('pop_netmanager:cvlans')


@login_required
def vlanonu_create(request):

    vlanonu_form = VlanonuForm(request.POST or None)

    if request.method == 'POST':
        if vlanonu_form.is_valid():
            vlanonu_form.save()
            sweetify.success(request, 'Cadastro Salvo', text='Informações \
                 da VLAN Gerência-ONU salvas com sucesso!', timer=3000)
            return redirect('pop_netmanager:vlanonus')

    context = {
        'vlanonu_form': vlanonu_form
    }

    return render(request, 'netmanager/vlan_management_onu.html', context)


@login_required
def vlanonu_edit(request, pk):

    vlanonu = Vlan_management_onu.objects.get(id=pk)
    vlanonu_form = VlanonuForm(request.POST or None, instance=vlanonu)

    if request.method == 'POST':
        if vlanonu_form.is_valid():
            vlanonu_form.save()
            sweetify.success(request, 'Cadastro Salvo', text='Informações \
                 da VLAN Gerência-ONU salvas com sucesso!', timer=3000)
            return redirect('pop_netmanager:vlanonus')

    context = {
        'vlanonu_form': vlanonu_form
    }

    return render(request, 'netmanager/vlan_management_onu.html', context)


@login_required
def vlanonu_delete(request, pk):
    if id:
        Vlan_management_onu.objects.filter(id=pk).delete()
        sweetify.success(request, 'Cadastro Excluído ',
                         text='Informações da VLAN Gerência-ONU excluídas com \
                                 sucesso.', timer=1500)
        return redirect('pop_netmanager:vlanonus')


@login_required
def svlan_create(request):

    svlan_form = SvlanForm(request.POST or None)

    if request.method == 'POST':
        if svlan_form.is_valid():
            svlan_form.save()
            sweetify.success(request, 'Cadastro Salvo', text='Informações \
                 da S-VLAN salvas com sucesso!', timer=3000)
            return redirect('pop_netmanager:svlans')

    context = {
        'svlan_form': svlan_form
    }

    return render(request, 'netmanager/svlan.html', context)


@login_required
def svlan_edit(request, pk):

    svlan = Svlan.objects.get(id=pk)
    svlan_form = SvlanForm(request.POST or None, instance=svlan)

    if request.method == 'POST':
        if svlan_form.is_valid():
            svlan_form.save()
            sweetify.success(request, 'Cadastro Salvo', text='Informações \
                 da S-VLAN salvas com sucesso!', timer=3000)
            return redirect('pop_netmanager:svlans')

    context = {
        'svlan_form': svlan_form
    }

    return render(request, 'netmanager/svlan.html', context)


@login_required
def svlan_delete(request, pk):
    if id:
        Svlan.objects.filter(id=pk).delete()
        sweetify.success(request, 'Cadastro Excluído ',
                         text='Informações da S-VLAN excluídas com \
                                 sucesso.', timer=1500)
        return redirect('pop_netmanager:svlans')


class Line_profileCreateView(SweetifySuccessMixin, BSModalCreateView):

    template_name = 'core/single_create_modal.html'
    form_class = Line_profileForm
    success_message = 'Cadastro Salvo'
    sweetify_options = {'text': 'Informações da Line Profile \
                        salvas com sucesso.', 'timer': 2500}
    success_url = reverse_lazy('pop_netmanager:lines_profile')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['parameters'] = modules.get('lines_profile')
        return context


class Line_profileUpdateView(SweetifySuccessMixin, BSModalUpdateView):

    template_name = 'core/single_create_modal.html'
    form_class = Line_profileForm
    success_message = 'Cadastro Salvo'
    sweetify_options = {'text': 'Informações da Line Profile \
                        alteradas com sucesso.', 'timer': 2500}
    success_url = reverse_lazy('pop_netmanager:lines_profile')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['parameters'] = modules.get('lines_profile')
        return context

    def get_queryset(self, **kwargs):
        return Line_profile.objects.filter(pk=self.kwargs['pk'])


@login_required
def line_profile_delete(request, pk):
    if id:
        Line_profile.objects.filter(id=pk).delete()
        sweetify.success(request, 'Cadastro Excluído ',
                         text='Informações da Line Profile excluídas com \
                                 sucesso.', timer=1500)
        return redirect('pop_netmanager:lines_profile')


class VmanCreateView(SweetifySuccessMixin, BSModalCreateView):

    template_name = 'core/single_create_modal.html'
    form_class = VmanForm
    success_message = 'Cadastro Salvo'
    sweetify_options = {'text': 'Informações da V-MAN salvas com sucesso.',
                        'timer': 2500
                        }
    success_url = reverse_lazy('pop_netmanager:vmans')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['parameters'] = modules.get('vmans')
        return context


class VmanUpdateView(SweetifySuccessMixin, BSModalUpdateView):

    template_name = 'core/single_create_modal.html'
    form_class = VmanForm
    success_message = 'Cadastro Salvo'
    sweetify_options = {'text': 'Informações da V-MAN alteradas com sucesso.',
                        'timer': 2500
                        }
    success_url = reverse_lazy('pop_netmanager:vmans')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['parameters'] = modules.get('vmans')
        return context

    def get_queryset(self, **kwargs):
        return Vman.objects.filter(pk=self.kwargs['pk'])


@login_required
def vman_delete(request, pk):
    if id:
        Vman.objects.filter(id=pk).delete()
        sweetify.success(request, 'Cadastro Excluído ',
                         text='Informações da V-MAN excluídas com \
                                 sucesso.', timer=1500)
        return redirect('pop_netmanager:vmans')


class CvlanCreateView(SweetifySuccessMixin, BSModalCreateView):

    template_name = 'core/single_create_modal.html'
    form_class = CvlanForm
    success_message = 'Cadastro Salvo'
    sweetify_options = {'text': 'Informações da C-VLAN salvas com sucesso.',
                        'timer': 2500
                        }
    success_url = reverse_lazy('pop_netmanager:cvlans')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['parameters'] = modules.get('cvlans')
        return context


class CvlanUpdateView(SweetifySuccessMixin, BSModalUpdateView):

    template_name = 'core/single_create_modal.html'
    form_class = CvlanForm
    success_message = 'Cadastro Salvo'
    sweetify_options = {'text': 'Informações da C-VLAN alteradas com sucesso.',
                        'timer': 2500
                        }
    success_url = reverse_lazy('pop_netmanager:cvlans')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['parameters'] = modules.get('cvlans')
        return context

    def get_queryset(self, **kwargs):
        return Cvlan.objects.filter(pk=self.kwargs['pk'])


@login_required
def cvlan_delete(request, pk):
    if id:
        Cvlan.objects.filter(id=pk).delete()
        sweetify.success(request, 'Cadastro Excluído ',
                         text='Informações da C-VLAN excluídas com \
                                 sucesso.', timer=1500)
        return redirect('pop_netmanager:cvlans')
