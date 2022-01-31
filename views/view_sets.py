from ..serializers import \
    NetworkSerializer, \
    ClientSerializer, \
    OltSerializer, \
    CdiSerializer, \
    Ca1Serializer, \
    VmanSerializer, \
    CvlanSerializer, \
    SvlanSerializer, \
    FirewallSerializer, \
    VlanapSerializer, \
    VlanswSerializer, \
    VlanonuSerializer, \
    DeviceSerializer,   \
    SwitchSerializer, \
    Line_profileSerializer, \
    OnuSerializer, \
    AccessPointSerializer
from ..models.network_equipament import \
    Network, \
    Olt, \
    Cdi, \
    Ca1, \
    Vman, \
    Cvlan, \
    Svlan, \
    Firewall, \
    Switch, \
    Vlan_management_ap, \
    Vlan_management_sw, \
    Vlan_management_onu, \
    Device, \
    Line_profile, \
    Onu, \
    AccessPoint
from ..models.client import Client
from rest_framework import viewsets


class AccessPointViewSet(viewsets.ModelViewSet):

    queryset = AccessPoint.objects.all()
    serializer_class = AccessPointSerializer


class OnuViewSet(viewsets.ModelViewSet):

    queryset = Onu.objects.all()
    serializer_class = OnuSerializer


class Line_profileViewSet(viewsets.ModelViewSet):

    queryset = Line_profile.objects.all()
    serializer_class = Line_profileSerializer


class SwitchViewSet(viewsets.ModelViewSet):

    queryset = Switch.objects.all()
    serializer_class = SwitchSerializer


class SvlanViewSet(viewsets.ModelViewSet):

    queryset = Svlan.objects.all()
    serializer_class = SvlanSerializer


class VlanapViewSet(viewsets.ModelViewSet):

    queryset = Vlan_management_ap.objects.all()
    serializer_class = VlanapSerializer


class VlanswViewSet(viewsets.ModelViewSet):

    queryset = Vlan_management_sw.objects.all()
    serializer_class = VlanswSerializer


class VlanonuViewSet(viewsets.ModelViewSet):

    queryset = Vlan_management_onu.objects.all()
    serializer_class = VlanonuSerializer


class FirewallViewSet(viewsets.ModelViewSet):

    queryset = Firewall.objects.all()
    serializer_class = FirewallSerializer


class ClientViewSet(viewsets.ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class NetworkViewSet(viewsets.ModelViewSet):

    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


class OltViewSet(viewsets.ModelViewSet):

    queryset = Olt.objects.all()
    serializer_class = OltSerializer


class CdiViewSet(viewsets.ModelViewSet):

    queryset = Cdi.objects.all()
    serializer_class = CdiSerializer


class Ca1ViewSet(viewsets.ModelViewSet):

    queryset = Ca1.objects.all()
    serializer_class = Ca1Serializer


class VmanViewSet(viewsets.ModelViewSet):

    queryset = Vman.objects.all()
    serializer_class = VmanSerializer


class CvlanViewSet(viewsets.ModelViewSet):

    queryset = Cvlan.objects.all()
    serializer_class = CvlanSerializer


class DeviceViewSet(viewsets.ModelViewSet):

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
