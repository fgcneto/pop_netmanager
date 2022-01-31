from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
# from bootstrap_datepicker_plus import DatePickerInput
from pop_erp.apps.pop_netmanager.models.network_equipament import \
    Network,\
    Olt, \
    Cdi, \
    Ca1, \
    Vman, \
    Cvlan, \
    Svlan, \
    Firewall, \
    Vlan_management_ap, \
    Vlan_management_sw, \
    Vlan_management_onu, \
    Device, \
    Switch, \
    Line_profile, \
    Onu, \
    AccessPoint


class Line_profileForm(BSModalForm):
    class Meta:
        model = Line_profile
        fields = ('id', 'hostname')

    def __init__(self, *args, **kwargs):
        super(Line_profileForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required': 'O campo {fieldname} é \
                obrigatório.'.format(
                fieldname=field.label)}


class NetworkForm(BSModalForm):
    class Meta:
        model = Network
        fields = ('id', 'hostname', 'abbreviation')

    def __init__(self, *args, **kwargs):
        super(NetworkForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required': 'O campo {fieldname} é \
                obrigatório.'.format(
                fieldname=field.label)}


class OltForm(BSModalForm):
    class Meta:
        model = Olt
        fields = ('id', 'hostname', 'ports_number', 'network')

    def __init__(self, *args, **kwargs):
        super(OltForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required': 'O campo {fieldname} é \
                obrigatório.'.format(
                fieldname=field.label)}


class CdiForm(BSModalForm):
    class Meta:
        model = Cdi
        fields = ('id', 'hostname', 'olt_port', 'ports_number')

    def __init__(self, *args, **kwargs):
        super(CdiForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required': 'O campo {fieldname} é \
                obrigatório.'.format(
                fieldname=field.label)}


class Ca1Form(BSModalForm):
    class Meta:
        model = Ca1
        fields = ('id', 'hostname', 'cdi_port', 'ports_number')

    def __init__(self, *args, **kwargs):
        super(Ca1Form, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required': 'O campo {fieldname} é \
                obrigatório.'.format(
                fieldname=field.label)}


class VmanForm(BSModalForm):
    class Meta:
        model = Vman
        fields = ('id', 'hostname', 'vlan_id')

    def __init__(self, *args, **kwargs):
        super(VmanForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required': 'O campo {fieldname} é \
                obrigatório.'.format(
                fieldname=field.label)}


class CvlanForm(BSModalForm):
    class Meta:
        model = Cvlan
        fields = ('id', 'hostname', 'vlan_id')

    def __init__(self, *args, **kwargs):
        super(CvlanForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required': 'O campo {fieldname} é \
                obrigatório.'.format(
                fieldname=field.label)}


class FirewallForm(ModelForm):
    class Meta:
        model = Firewall
        fields = (
            'hostname',
            'ipv4_publico',
            'ipv6_publico',
            'sub_rede',
            'range_ip_start',
            'range_ip_end',
            'obs',
        )

        labels = {
            'hostname': _('Hostname'),
            'ipv4_publico': _('IPV4 - Público'),
            'ipv6_publico': _('IPV6 - Público'),
            'sub_rede': _('SUB-REDE'),
            'range_ip_start': _('Range IP - Início'),
            'range_ip_end': _('Range IP - Final'),
            'obs': _('Observações'),
        }

        widgets = {
            'hostname': forms.TextInput(
                attrs={'id': 'color', 'class': 'form-control'}),
            'ipv4_publico': forms.TextInput(
                attrs={'id': 'ipv4_publico', 'autofocus': True,
                       'class': 'form-control'}),
            'ipv6_publico': forms.TextInput(
                attrs={'id': 'ipv4_publico', 'autofocus': True,
                       'class': 'form-control'}),
            'sub_rede': forms.TextInput(
                attrs={'id': 'sub_rede', 'autofocus': True,
                       'class': 'form-control'}),
            'range_ip_start': forms.TextInput(
                attrs={'id': 'range_ip_start', 'autofocus': True,
                       'class': 'form-control'}),
            'range_ip_end': forms.TextInput(
                attrs={'id': 'range_ip_end', 'autofocus': True,
                       'class': 'form-control'}),
            'obs': forms.Textarea(
                attrs={'id': 'color', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(FirewallForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = \
                {'required': 'O(A) {fieldname} é obrigatório.'.
                    format(fieldname=field.label)}


class VlanapForm(ModelForm):
    class Meta:
        model = Vlan_management_ap
        fields = (
            'id',
            'hostname',
            'vlan_id',
            'ipv4_address',
            'ipv6_address',
            'ipv4_gateway',
            'ipv6_gateway'
        )

        labels = {
            'hostname': _('Hostname'),
            'vlan_id': _('V-LAN - ID'),
            'ipv4_address': _('Address - IPV4'),
            'ipv6_address': _('Address - IPV6'),
            'ipv4_gateway': _('Gateway - IPV4'),
            'ipv6_gateway': _('Gateway - IPV6'),
        }

        widgets = {
            'hostname': forms.TextInput(
                attrs={'id': 'color', 'class': 'form-control'}),
            'vlan_id': forms.TextInput(
                attrs={'id': 'vlan_id', 'class': 'form-control'}),
            'ipv4_address': forms.TextInput(
                attrs={'id': 'ipv4_address', 'autofocus': True,
                       'class': 'form-control', 'protocol': 'ipv4'}),
            'ipv6_address': forms.TextInput(
                attrs={'id': 'ipv6_address', 'autofocus': True,
                       'class': 'form-control', 'protocol': 'ipv6'}),
            'ipv4_gateway': forms.TextInput(
                attrs={'id': 'ipv4_gateway', 'autofocus': True,
                       'class': 'form-control', 'protocol': 'ipv4'}),
            'ipv6_gateway': forms.TextInput(
                attrs={'id': 'ipv6_gateway', 'autofocus': True,
                       'class': 'form-control', 'protocol': 'ipv6'}),
        }

    def __init__(self, *args, **kwargs):
        super(VlanapForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = \
                {'required': 'O(A) {fieldname} é obrigatório.'.
                    format(fieldname=field.label)}


class VlanswForm(ModelForm):
    class Meta:
        model = Vlan_management_sw
        fields = (
            'id',
            'hostname',
            'vlan_id',
            'ipv4_address',
            'ipv6_address',
            'ipv4_gateway',
            'ipv6_gateway'
        )

        labels = {
            'hostname': _('Hostname'),
            'vlan_id': _('V-LAN - ID'),
            'ipv4_address': _('Address - IPV4'),
            'ipv6_address': _('Address - IPV6'),
            'ipv4_gateway': _('Gateway - IPV4'),
            'ipv6_gateway': _('Gateway - IPV6'),
        }

        widgets = {
            'hostname': forms.TextInput(
                attrs={'id': 'color', 'class': 'form-control'}),
            'vlan_id': forms.TextInput(
                attrs={'id': 'vlan_id', 'class': 'form-control'}),
            'ipv4_address': forms.TextInput(
                attrs={'id': 'ipv4_address', 'autofocus': True,
                       'class': 'form-control', 'protocol': 'ipv4'}),
            'ipv6_address': forms.TextInput(
                attrs={'id': 'ipv6_address', 'autofocus': True,
                       'class': 'form-control', 'protocol': 'ipv6'}),
            'ipv4_gateway': forms.TextInput(
                attrs={'id': 'ipv4_gateway', 'autofocus': True,
                       'class': 'form-control', 'protocol': 'ipv4'}),
            'ipv6_gateway': forms.TextInput(
                attrs={'id': 'ipv6_gateway', 'autofocus': True,
                       'class': 'form-control', 'protocol': 'ipv6'}),
        }

    def __init__(self, *args, **kwargs):
        super(VlanswForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = \
                {'required': 'O(A) {fieldname} é obrigatório.'.
                    format(fieldname=field.label)}


class VlanonuForm(ModelForm):
    class Meta:
        model = Vlan_management_onu
        fields = (
            'id',
            'hostname',
            'vlan_id',
            'ipv4_address',
            'ipv6_address',
            'ipv4_gateway',
            'ipv6_gateway'
        )

        labels = {
            'hostname': _('Hostname'),
            'vlan_id': _('V-LAN - ID'),
            'ipv4_address': _('Address - IPV4'),
            'ipv6_address': _('Address - IPV6'),
            'ipv4_gateway': _('Gateway - IPV4'),
            'ipv6_gateway': _('Gateway - IPV6'),
        }

        widgets = {
            'hostname': forms.TextInput(
                attrs={'id': 'color', 'class': 'form-control'}),
            'vlan_id': forms.TextInput(
                attrs={'id': 'vlan_id', 'class': 'form-control'}),
            'ipv4_address': forms.TextInput(
                attrs={'id': 'ipv4_address', 'autofocus': True,
                       'class': 'form-control', 'protocol': 'ipv4'}),
            'ipv6_address': forms.TextInput(
                attrs={'id': 'ipv6_address', 'autofocus': True,
                       'class': 'form-control', 'protocol': 'ipv6'}),
            'ipv4_gateway': forms.TextInput(
                attrs={'id': 'ipv4_gateway', 'autofocus': True,
                       'class': 'form-control', 'protocol': 'ipv4'}),
            'ipv6_gateway': forms.TextInput(
                attrs={'id': 'ipv6_gateway', 'autofocus': True,
                       'class': 'form-control', 'protocol': 'ipv6'}),
        }

    def __init__(self, *args, **kwargs):
        super(VlanonuForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = \
                {'required': 'O(A) {fieldname} é obrigatório.'.
                    format(fieldname=field.label)}


class DeviceForm(BSModalForm):
    class Meta:
        model = Device
        fields = ('id', 'hostname', 'ipv4_address', 'ipv6_address', 's_vlan',)

    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required': 'O campo {fieldname} é \
                obrigatório.'.format(
                fieldname=field.label)}


class SwitchForm(ModelForm):
    class Meta:
        model = Switch
        fields = ('id', 'hostname', 'serial', 'mac_address',
                  'ip_address', 'telnet', 'ssh',
                  'snmp', 'user1', 'user2', 'sntp_client',
                  'default_route', 'erlp', 'dhcp_snooping',
                  'port_poe', 'ports_number', 'onu_port',
                  'vlan_management_sw')

        labels = {
            'hostname': _('Hostname'),
            'serial': _('Serial'),
            'mac_address': _('MAC Address'),
            'ip_address': _('IP Address'),
            'telnet': _('Telnet'),
            'ssh': _('SSH'),
            'snmp': _('SNMP'),
            'user1': _('User 1'),
            'user2': _('User 2'),
            'sntp_client': _('Cliente - SNTP'),
            'default_route': _('Rota Default'),
            'erlp': _('ERLP'),
            'dhcp_snooping': _('DHCP Snooping'),
            'port_poe': _('Porta - POE'),
            'ports_number': _('Número de portas'),
            'onu_port': _('Porta da ONU'),
            'vlan_management_sw': _('V-LAN de Gerência')
        }

        widgets = {
            'hostname': forms.TextInput(
                attrs={'id': 'color', 'class': 'form-control'}),
            'serial': forms.TextInput(
                attrs={'id': 'serial', 'class': 'form-control'}),
            'mac_address': forms.TextInput(
                attrs={'id': 'mac_address', 'autofocus': True,
                       'class': 'form-control'}),
            'ip_address': forms.TextInput(
                attrs={'id': 'ip_address', 'autofocus': True,
                       'class': 'form-control'}),
            'telnet': forms.CheckboxInput(
                attrs={'id': 'telnet'}),
            'ssh': forms.CheckboxInput(
                attrs={'id': 'ssh'}),
            'snmp': forms.CheckboxInput(
                attrs={'id': 'snmp'}),
            'user1': forms.TextInput(
                attrs={'id': 'user1', 'autofocus': True,
                       'class': 'form-control'}),
            'user2': forms.TextInput(
                attrs={'id': 'user2', 'autofocus': True,
                       'class': 'form-control'}),
            'sntp_client': forms.CheckboxInput(
                attrs={'id': 'sntp_client'}),
            'default_route': forms.TextInput(
                attrs={'id': 'default_route', 'autofocus': True,
                       'class': 'form-control'}),
            'erlp': forms.CheckboxInput(
                attrs={'id': 'erlp'}),
            'dhcp_snooping': forms.CheckboxInput(
                attrs={'id': 'dhcp_snooping'}),
            'port_poe': forms.TextInput(
                attrs={'id': 'port_poe', 'autofocus': True,
                       'class': 'form-control'}),
            'ports_number': forms.NumberInput(
                attrs={'id': 'ports_number', 'autofocus': True,
                       'class': 'form-control'}),
            'onu_port': forms.Select(
                attrs={'id': 'onu_port', 'autofocus': True,
                       'class': 'form-control'}),
            'vlan_management_sw': forms.Select(
                attrs={'id': 'vlan_management_sw', 'autofocus': True,
                       'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(SwitchForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = \
                {'required': 'O(A) {fieldname} é obrigatório.'.
                    format(fieldname=field.label)}


class SvlanForm(ModelForm):
    class Meta:
        model = Svlan
        fields = (
            'id', 'hostname', 'vlan_id',
            'ipv4_publico', 'ipv6_publico',
            'ipv4_privado', 'ipv6_privado',
            'sub_rede_ipv4', 'sub_rede_ipv6',
            'range_start_ipv4', 'range_end_ipv4',
            'range_start_ipv6', 'range_end_ipv6',
            'bw_up', 'bw_down', 'firewall',
            'c_vlan', 'v_man', 'client'
        )

        labels = {
            'hostname': _('Hostname'),
            'vlan_id': _('V-LAN - ID'),
            'ipv4_publico': _('IPV4 - Público'),
            'ipv6_publico': _('IPV6 - Público'),
            'ipv4_privado': _('IPV4 - Privado'),
            'ipv6_privado': _('IPV6 - Privado'),
            'sub_rede_ipv4': _('IPV4'),
            'sub_rede_ipv6': _('IPV6'),
            'range_start_ipv4': _('IPV4 - Início'),
            'range_end_ipv4': _('IPV4 - Final'),
            'range_start_ipv6': _('IPV6 - Início'),
            'range_end_ipv6': _('IPV6 - Final'),
            'bw_up': _('UP'),
            'bw_down': _('DW'),
            'firewall': _('Firewall'),
            'c_vlan': _('C-VLAN'),
            'v_man': _('V-MAN'),
            'client': _('Cliente'),
        }

        widgets = {
            'hostname': forms.TextInput(
                attrs={'id': 'hostname', 'class': 'form-control'}),
            'vlan_id': forms.TextInput(
                attrs={'id': 'vlan_id', 'class': 'form-control'}),
            'ipv4_publico': forms.TextInput(
                attrs={'id': 'ipv4_publico', 'autofocus': True,
                       'class': 'form-control'}),
            'ipv6_publico': forms.TextInput(
                attrs={'id': 'ipv6_publico', 'autofocus': True,
                       'class': 'form-control'}),
            'ipv4_privado': forms.TextInput(
                attrs={'id': 'ipv4_privado', 'autofocus': True,
                       'class': 'form-control'}),
            'ipv6_privado': forms.TextInput(
                attrs={'id': 'ipv6_privado', 'autofocus': True,
                       'class': 'form-control'}),
            'sub_rede_ipv4': forms.TextInput(
                attrs={'id': 'sub_rede_ipv4', 'autofocus': True,
                       'class': 'form-control'}),
            'sub_rede_ipv6': forms.TextInput(
                attrs={'id': 'sub_rede_ipv6', 'autofocus': True,
                       'class': 'form-control'}),
            'range_start_ipv4': forms.TextInput(
                attrs={'id': 'range_start_ipv4', 'autofocus': True,
                       'class': 'form-control'}),
            'range_end_ipv4': forms.TextInput(
                attrs={'id': 'range_end_ipv4', 'autofocus': True,
                       'class': 'form-control'}),
            'range_start_ipv6': forms.TextInput(
                attrs={'id': 'range_start_ipv6', 'autofocus': True,
                       'class': 'form-control'}),
            'range_end_ipv6': forms.TextInput(
                attrs={'id': 'range_end_ipv6', 'autofocus': True,
                       'class': 'form-control'}),
            'bw_up': forms.TextInput(
                attrs={'id': 'bw_up', 'autofocus': True,
                       'class': 'form-control'}),
            'bw_down': forms.TextInput(
                attrs={'id': 'bw_down', 'autofocus': True,
                       'class': 'form-control'}),
            'firewall': forms.Select(
                attrs={'id': 'firewall', 'autofocus': True,
                       'class': 'form-control'}),
            'c_vlan': forms.Select(
                attrs={'id': 'c_vlan', 'autofocus': True,
                       'class': 'form-control'}),
            'v_man': forms.Select(
                attrs={'id': 'v_man', 'autofocus': True,
                       'class': 'form-control'}),
            'client': forms.Select(
                attrs={'id': 'client', 'autofocus': True,
                       'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(SvlanForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = \
                {'required': 'O(A) {fieldname} é obrigatório.'.
                    format(fieldname=field.label)}


class OnuForm(ModelForm):
    class Meta:
        model = Onu
        fields = (
            'id', 'hostname', 'onu_id', 'serial',
            'ipv4_publico', 'ipv6_publico',
            'user1', 'user2', 'password',
            'ports_number', 'line_profile',
            'bw_up', 'bw_down', 's_vlan',
            'ca1_port', 'vlan_management_onu'
        )

        labels = {
            'hostname': _('Hostname'),
            'onu_id': _('ONU - ID'),
            'serial': _('Serial'),
            'ipv4_publico': _('IPV4 - Público'),
            'ipv6_publico': _('IPV6 - Público'),
            'user1': _('USER 1'),
            'user2': _('USER 2'),
            'password': _('Password'),
            'ports_number': _('Número de Portas'),
            'line_profile': _('Line Profile'),
            'bw_up': _('UP'),
            'bw_down': _('DW'),
            's_vlan': _('S-VLAN'),
            'ca1_port': _('Parta da CA-1'),
            'vlan_management_onu': _('Gerência ONU'),
        }

        widgets = {
            'hostname': forms.TextInput(
                attrs={'id': 'color', 'class': 'form-control'}),
            'onu_id': forms.TextInput(
                attrs={'id': 'onu_id', 'class': 'form-control'}),
            'serial': forms.TextInput(
                attrs={'id': 'serial', 'class': 'form-control'}),
            'ipv4_publico': forms.TextInput(
                attrs={'id': 'ipv4_publico', 'autofocus': True,
                       'class': 'form-control'}),
            'ipv6_publico': forms.TextInput(
                attrs={'id': 'ipv6_publico', 'autofocus': True,
                       'class': 'form-control'}),
            'user1': forms.TextInput(
                attrs={'id': 'user1', 'autofocus': True,
                       'class': 'form-control'}),
            'user2': forms.TextInput(
                attrs={'id': 'user2', 'autofocus': True,
                       'class': 'form-control'}),
            'password': forms.TextInput(
                attrs={'id': 'password', 'autofocus': True,
                       'class': 'form-control'}),
            'ports_number': forms.NumberInput(
                attrs={'id': 'ports_number', 'autofocus': True,
                       'class': 'form-control'}),
            'line_profile': forms.Select(
                attrs={'id': 'line_profile', 'autofocus': True,
                       'class': 'form-control'}),
            'bw_up': forms.TextInput(
                attrs={'id': 'bw_up', 'autofocus': True,
                       'class': 'form-control'}),
            'bw_down': forms.TextInput(
                attrs={'id': 'bw_down', 'autofocus': True,
                       'class': 'form-control'}),
            's_vlan': forms.SelectMultiple(
                attrs={'id': 's_vlan', 'autofocus': True,
                       'class': 'form-control'}),
            'ca1_port': forms.Select(
                attrs={'id': 'ca1_port', 'autofocus': True,
                       'class': 'form-control'}),
            'vlan_management_onu': forms.Select(
                attrs={'id': 'vlan_management_onu', 'autofocus': True,
                       'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(OnuForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = \
                {'required': 'O(A) {fieldname} é obrigatório.'.
                    format(fieldname=field.label)}


class AccessPointForm(ModelForm):
    class Meta:
        model = AccessPoint
        fields = ('id', 'hostname', 'serial', 'mac_address',
                  'wlan_aluno', 'wlan_admin', 'switch_port',
                  'vlan_management_ap')

        labels = {
            'hostname': _('Hostname'),
            'serial': _('Serial'),
            'mac_address': _('MAC Address'),
            'wlan_aluno': _('WLAN Aluno'),
            'wlan_admin': _('WLAN Admin'),
            'switch_port': _('Porta do Switch'),
            'vlan_management_ap': _('Gerência ap'),
        }

        widgets = {
            'hostname': forms.TextInput(
                attrs={'id': 'color', 'class': 'form-control'}),
            'serial': forms.TextInput(
                attrs={'id': 'serial', 'class': 'form-control'}),
            'mac_address': forms.TextInput(
                attrs={'id': 'mac_address', 'autofocus': True,
                       'class': 'form-control'}),
            'wlan_aluno': forms.TextInput(
                attrs={'id': 'wlan_aluno', 'autofocus': True,
                       'class': 'form-control'}),
            'wlan_admin': forms.TextInput(
                attrs={'id': 'wlan_admin', 'autofocus': True,
                       'class': 'form-control'}),
            'switch_port': forms.Select(
                attrs={'id': 'switch_port', 'autofocus': True,
                       'class': 'form-control'}),
            'vlan_management_ap': forms.Select(
                attrs={'id': 'vlan_management_ap', 'autofocus': True,
                       'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(AccessPointForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = \
                {'required': 'O(A) {fieldname} é obrigatório.'.
                    format(fieldname=field.label)}
