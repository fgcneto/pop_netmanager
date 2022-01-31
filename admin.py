from pop_erp.apps.pop_netmanager.models.client import Client, Contact
from django.contrib import admin
from pop_erp.apps.pop_netmanager.models.network_equipament import (
    Switch_port, Vlan_port, AccessPoint, Firewall, Switch,
    Olt, Olt_port, Cdi, Cdi_port, Ca1, Ca1_port, Onu, Vman,
    Vlan_management_ap, Vlan_management_sw, Vlan_management_onu,
    Svlan, Cvlan, Vlan_switch,
    Line_profile, Network, Device)


# Register your models here.
admin.site.register(Firewall, admin.ModelAdmin)
admin.site.register(Network, admin.ModelAdmin)
admin.site.register(AccessPoint, admin.ModelAdmin)
admin.site.register(Switch, admin.ModelAdmin)
admin.site.register(Client, admin.ModelAdmin)
admin.site.register(Contact, admin.ModelAdmin)
admin.site.register(Device, admin.ModelAdmin)
admin.site.register(Vlan_management_ap, admin.ModelAdmin)
admin.site.register(Vlan_management_sw, admin.ModelAdmin)
admin.site.register(Vlan_management_onu, admin.ModelAdmin)
admin.site.register(Svlan, admin.ModelAdmin)
admin.site.register(Cvlan, admin.ModelAdmin)
admin.site.register(Vman, admin.ModelAdmin)
admin.site.register(Olt, admin.ModelAdmin)
admin.site.register(Olt_port, admin.ModelAdmin)
admin.site.register(Cdi, admin.ModelAdmin)
admin.site.register(Cdi_port, admin.ModelAdmin)
admin.site.register(Ca1, admin.ModelAdmin)
admin.site.register(Ca1_port, admin.ModelAdmin)
admin.site.register(Switch_port, admin.ModelAdmin)
admin.site.register(Vlan_port, admin.ModelAdmin)
admin.site.register(Vlan_switch, admin.ModelAdmin)
admin.site.register(Onu, admin.ModelAdmin)
admin.site.register(Line_profile, admin.ModelAdmin)
