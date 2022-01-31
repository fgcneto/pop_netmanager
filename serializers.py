from rest_framework import serializers
from .models.network_equipament import \
    Network, \
    Olt, \
    Cdi, \
    Ca1, \
    Olt_port, \
    Cdi_port, \
    Ca1_port, \
    Onu_port, \
    Switch_port, \
    Vman, \
    Cvlan, \
    Svlan, \
    Firewall, \
    Device, \
    Switch, \
    Onu, \
    Line_profile, \
    AccessPoint, \
    Vlan_management_ap, \
    Vlan_management_sw, \
    Vlan_management_onu
from .models.client import Client


class ClientSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Client
        fields = ('id', 'description', 'name', 'code', 'place', 'entity')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_message_field(self, obj):
        return obj.name


class NetworkSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Network
        fields = ('id', 'hostname', 'abbreviation')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_message_field(self, obj):
        return obj.hostname


class OltSerializer(serializers.ModelSerializer):

    network = NetworkSerializer()

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Olt
        fields = ('id', 'hostname', 'ports_number', 'network')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_message_field(self, obj):
        return obj.hostname


class Olt_portSerializer(serializers.ModelSerializer):

    olt = OltSerializer()

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Olt_port
        fields = ('id', 'olt', 'number')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_message_field(self, obj):
        return obj.number + " - " + obj.olt


class CdiSerializer(serializers.ModelSerializer):

    olt_port = Olt_portSerializer()

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Cdi
        fields = ('id', 'hostname', 'olt_port', 'ports_number')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_message_field(self, obj):
        return obj.hostname


class Cdi_portSerializer(serializers.ModelSerializer):

    cdi = CdiSerializer()

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Cdi_port
        fields = ('id', 'cdi', 'number')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_message_field(self, obj):
        return obj.number + " - " + obj.cdi


class Ca1Serializer(serializers.ModelSerializer):

    cdi_port = Cdi_portSerializer()

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Ca1
        fields = ('id', 'hostname', 'cdi_port', 'ports_number')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_message_field(self, obj):
        return obj.hostname


class Ca1_portSerializer(serializers.ModelSerializer):

    ca1 = Ca1Serializer()

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Ca1_port
        fields = ('id', 'ca1', 'number')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_message_field(self, obj):
        return obj.number + " - " + obj.ca1


class VmanSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Vman
        fields = ('id', 'hostname', 'vlan_id')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_message_field(self, obj):
        return obj.hostname


class CvlanSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Cvlan
        fields = ('id', 'hostname', 'vlan_id')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_message_field(self, obj):
        return obj.hostname


class FirewallSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Firewall
        fields = ('id', 'hostname', 'ipv4_publico', 'ipv6_publico',
                  'sub_rede', 'range_ip_start', 'range_ip_end', 'obs')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_message_field(self, obj):
        return obj.hostname


class Line_profileSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Line_profile
        fields = ('id', 'hostname')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_message_field(self, obj):
        return obj.hostname


class SvlanSerializer(serializers.ModelSerializer):

    firewall = FirewallSerializer()
    c_vlan = CvlanSerializer()
    v_man = VmanSerializer()
    client = ClientSerializer()

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Svlan
        fields = ('id', 'hostname', 'vlan_id', 'ipv4_publico',
                  'ipv6_publico', 'ipv4_privado', 'ipv6_privado',
                  'sub_rede_ipv4', 'sub_rede_ipv6', 'range_start_ipv4',
                  'range_end_ipv4', 'range_start_ipv6', 'range_end_ipv6',
                  'bw_up', 'bw_down', 'firewall', 'c_vlan',
                  'v_man', 'client')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_message_field(self, obj):
        return obj.hostname


class VlanapSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Vlan_management_ap
        fields = ('id', 'hostname', 'vlan_id', 'ipv4_address',
                  'ipv6_address', 'ipv4_gateway', 'ipv6_gateway')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_message_field(self, obj):
        return obj.hostname


class DeviceSerializer(serializers.ModelSerializer):

    s_vlan = SvlanSerializer()

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Device
        fields = ('id', 'hostname', 'ipv4_address', 'ipv6_address', 's_vlan')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_message_field(self, obj):
        return obj.hostname


class VlanswSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Vlan_management_sw
        fields = ('id', 'hostname', 'vlan_id', 'ipv4_address',
                  'ipv6_address', 'ipv4_gateway', 'ipv6_gateway')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_message_field(self, obj):
        return obj.hostname


class VlanonuSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Vlan_management_onu
        fields = ('id', 'hostname', 'vlan_id', 'ipv4_address',
                  'ipv6_address', 'ipv4_gateway', 'ipv6_gateway')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_message_field(self, obj):
        return obj.hostname


class OnuSerializer(serializers.ModelSerializer):

    s_vlan = SvlanSerializer(read_only=True, many=True)
    line_profile = Line_profileSerializer()
    ca1_port = Ca1_portSerializer()
    vlan_management_onu = VlanonuSerializer()

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Onu
        fields = ('id', 'onu_id', 'hostname', 'serial', 'ipv4_publico',
                  'ipv6_publico', 'bw_up', 'bw_down',
                  'user1', 'user2', 'password', 'ports_number',
                  'line_profile', 's_vlan', 'ca1_port',
                  'vlan_management_onu')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_message_field(self, obj):
        return obj.hostname


class Onu_portSerializer(serializers.ModelSerializer):

    onu = OnuSerializer()

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Onu_port
        fields = ('id', 'onu', 'number')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_message_field(self, obj):
        return obj.number + " - " + obj.onu


class SwitchSerializer(serializers.ModelSerializer):

    vlan_management_sw = VlanswSerializer()
    onu_port = Onu_portSerializer()

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Switch
        fields = ('id', 'hostname', 'serial', 'mac_address',
                  'ip_address', 'telnet', 'ssh',
                  'snmp', 'user1', 'user2', 'sntp_client',
                  'default_route', 'erlp', 'dhcp_snooping',
                  'port_poe', 'ports_number', 'onu_port',
                  'vlan_management_sw')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_message_field(self, obj):
        return obj.hostname


class Switch_portSerializer(serializers.ModelSerializer):

    switch = SwitchSerializer()
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Switch_port
        fields = ('id', 'enable', 'switch', 'number')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_message_field(self, obj):
        return obj.number + " - " + obj.switch


class AccessPointSerializer(serializers.ModelSerializer):

    switch_port = Switch_portSerializer()
    vlan_management_ap = VlanapSerializer()

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = AccessPoint
        fields = ('id', 'hostname', 'serial', 'mac_address',
                  'wlan_aluno', 'wlan_admin', 'switch_port',
                  'vlan_management_ap')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_message_field(self, obj):
        return obj.hostname
