from django.conf.urls import url, include
from rest_framework import routers
from pop_erp.apps.pop_netmanager import views
from django.urls import path


router1 = routers.DefaultRouter()
router1.register(r'rede', views.NetworkViewSet)
router1.register(r'cliente', views.ClientViewSet)
router1.register(r'olt', views.OltViewSet)
router1.register(r'cdi', views.CdiViewSet)
router1.register(r'ca1', views.Ca1ViewSet)
router1.register(r'vman', views.VmanViewSet)
router1.register(r'cvlan', views.CvlanViewSet)
router1.register(r'firewall', views.FirewallViewSet)
router1.register(r'vlanap', views.VlanapViewSet)
router1.register(r'vlansw', views.VlanswViewSet)
router1.register(r'vlanonu', views.VlanonuViewSet)
router1.register(r'svlan', views.SvlanViewSet)
router1.register(r'device', views.DeviceViewSet)
router1.register(r'switch', views.SwitchViewSet)
router1.register(r'line_profile', views.Line_profileViewSet)
router1.register(r'onu', views.OnuViewSet)
router1.register(r'accesspoint', views.AccessPointViewSet)

app_name = 'pop_netmanager'

urlpatterns = [

    url('^api/', include(router1.urls)),
    url(r'^$', views.index, name='index'),
    url('redes', views.listar, name='redes'),
    url('clientes', views.listar, name='clientes'),
    url('olts', views.listar, name='olts'),
    url('cdis', views.listar, name='cdis'),
    url('ca1s', views.listar, name='ca1s'),
    url('vmans', views.listar, name='vmans'),
    url('cvlans', views.listar, name='cvlans'),
    url('firewalls', views.listar, name='firewalls'),
    url('vlanaps', views.listar, name='vlanaps'),
    url('vlansws', views.listar, name='vlansws'),
    url('vlanonus', views.listar, name='vlanonus'),
    url('svlans', views.listar, name='svlans'),
    url('devices', views.listar, name='devices'),
    url('switches', views.listar, name='switches'),
    url('lines_profile', views.listar, name='lines_profile'),
    url('onus', views.listar, name='onus'),
    url('accesspoints', views.listar, name='accesspoints'),


    url('line_profile/add',
        views.logical_network.Line_profileCreateView.as_view(),
        name='line_profile'),
    path('line_profile/edit/<int:pk>',
         views.logical_network.Line_profileUpdateView.as_view(),
         name='line_profile_edit'),
    path('line_profile/delete/<int:pk>',
         views.logical_network.line_profile_delete,
         name='line_profile-delete'),

    url('cliente/add', views.client.ClientCreateView.as_view(),
        name='cliente'),
    path('cliente/edit/<int:pk>', views.client.ClientUpdateView.as_view(),
         name='cliente_edit'),

    url('rede/add',
        views.physical_network.NetworkCreateView.as_view(),
        name='rede'),
    path('rede/edit/<int:pk>',
         views.physical_network.NetworkUpdateView.as_view(),
         name='rede_edit'),
    path('rede/delete/<int:pk>',
         views.physical_network.network_delete,
         name='rede-delete'),

    url('olt/add',
        views.physical_network.OltCreateView.as_view(),
        name='olt'),
    path('olt/edit/<int:pk>',
         views.physical_network.OltUpdateView.as_view(),
         name='olt_edit'),
    path('olt/delete/<int:pk>',
         views.physical_network.olt_delete,
         name='olt-delete'),

    url('cdi/add',
        views.physical_network.CdiCreateView.as_view(),
        name='cdi'),
    path('cdi/edit/<int:pk>',
         views.physical_network.CdiUpdateView.as_view(),
         name='cdi_edit'),
    path('cdi/delete/<int:pk>',
         views.physical_network.cdi_delete,
         name='cdi-delete'),

    url('ca1/add',
        views.physical_network.Ca1CreateView.as_view(),
        name='ca1'),
    path('ca1/edit/<int:pk>',
         views.physical_network.Ca1UpdateView.as_view(),
         name='ca1_edit'),
    path('ca1/delete/<int:pk>',
         views.physical_network.ca1_delete,
         name='ca1-delete'),

    url('vman/add',
        views.logical_network.VmanCreateView.as_view(),
        name='vman'),
    path('vman/edit/<int:pk>',
         views.logical_network.VmanUpdateView.as_view(),
         name='vman_edit'),
    path('vman/delete/<int:pk>',
         views.logical_network.vman_delete,
         name='vman-delete'),

    url('cvlan/add',
        views.logical_network.CvlanCreateView.as_view(),
        name='cvlan'),
    path('cvlan/edit/<int:pk>',
         views.logical_network.CvlanUpdateView.as_view(),
         name='cvlan_edit'),
    path('cvlan/delete/<int:pk>',
         views.logical_network.cvlan_delete,
         name='cvlan-delete'),

    url('firewall/add',
        views.logical_network.firewall_create,
        name='firewall'),
    path('firewall/edit/<int:pk>',
         views.logical_network.firewall_edit,
         name='firewall-edit'),
    path('firewall/delete/<int:pk>',
         views.logical_network.firewall_delete,
         name='firewall-delete'),

    url('vlanap/add',
        views.logical_network.vlanap_create,
        name='vlanap'),
    path('vlanap/edit/<int:pk>',
         views.logical_network.vlanap_edit,
         name='vlanap_edit'),
    path('vlanap/delete/<int:pk>',
         views.logical_network.vlanap_delete,
         name='vlanap-delete'),

    url('vlansw/add',
        views.logical_network.vlansw_create,
        name='vlansw'),
    path('vlansw/edit/<int:pk>',
         views.logical_network.vlansw_edit,
         name='vlansw_edit'),
    path('vlansw/delete/<int:pk>',
         views.logical_network.vlansw_delete,
         name='vlansw-delete'),

    url('vlanonu/add',
        views.logical_network.vlanonu_create,
        name='vlanonu'),
    path('vlanonu/edit/<int:pk>',
         views.logical_network.vlanonu_edit,
         name='vlanonu_edit'),
    path('vlanonu/delete/<int:pk>',
         views.logical_network.vlanonu_delete,
         name='vlanonu-delete'),

    url('svlan/add',
        views.logical_network.svlan_create,
        name='svlan'),
    path('svlan/edit/<int:pk>',
         views.logical_network.svlan_edit,
         name='svlan_edit'),
    path('svlan/delete/<int:pk>',
         views.logical_network.svlan_delete,
         name='svlan-delete'),

    url('device/add',
        views.physical_network.DeviceCreateView.as_view(),
        name='device'),
    path('device/edit/<int:pk>',
         views.physical_network.DeviceUpdateView.as_view(),
         name='device_edit'),
    path('device/delete/<int:pk>',
         views.physical_network.device_delete,
         name='device-delete'),

    url('switch/add',
        views.physical_network.switch_create,
        name='switch'),
    path('switch/edit/<int:pk>',
         views.physical_network.switch_edit,
         name='switch_edit'),
    path('switch/delete/<int:pk>',
         views.physical_network.switch_delete,
         name='switch-delete'),

    url('onu/add',
        views.physical_network.onu_create,
        name='onu'),
    path('onu/edit/<int:pk>',
         views.physical_network.onu_edit,
         name='onu_edit'),
    path('onu/delete/<int:pk>',
         views.physical_network.onu_delete,
         name='onu-delete'),

    url('accesspoint/add',
        views.physical_network.accesspoint_create,
        name='accesspoint'),
    path('accesspoint/edit/<int:pk>',
         views.physical_network.accesspoint_edit,
         name='accesspoint_edit'),
    path('accesspoint/delete/<int:pk>',
         views.physical_network.accesspoint_delete,
         name='accesspoint-delete'),
]
