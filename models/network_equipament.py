# Model responsável pela gestão do Inventário da Rede Giga Metrópole
from django.db import models
from pop_erp.apps.pop_netmanager.models.client import Client


def compareDates(a, b):
    """Compara as datas com base apenas no dia do ano,
        hora, minuto e segundo, sem microsegundos.

    Parameters:
        a(DateField): Data 1
        b(DateField): Data 2

    Returns:
        True or False
    """
    conditions = [
        a.date() == b.date(),
        a.hour == b.hour,
        a.minute == b.minute,
        a.second == b.second
    ]
    if all(conditions):
        return True
    return False


class Network(models.Model):
    '''Responsável pela gestão das Redes'''
    hostname = models.CharField(verbose_name='Nome', max_length=50)
    abbreviation = models.CharField(verbose_name='Sigla', max_length=20)

    class Meta:
        verbose_name = 'Rede'
        verbose_name_plural = 'Redes'
        db_table = u'"pop_netmanager\".\"tb_networks"'

    def __str__(self):
        return self.abbreviation


class Port(models.Model):
    '''Responsável pela gestão das portas dos dispositivos'''
    number = models.IntegerField(verbose_name='Número da Porta')

    class Meta:
        abstract = True
        verbose_name = 'Porta'
        verbose_name_plural = 'Portas'

    def __str__(self):
        return self.number


class Olt(models.Model):
    '''Responsável por gerenciar as OLT'S'''
    hostname = models.CharField(verbose_name='OLT', max_length=15)
    ports_number = models.IntegerField(verbose_name='No de Portas')
    created_at = models.DateTimeField(
        verbose_name='Criado em:', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Modificado em:', auto_now=True)
    network = models.ForeignKey(
        Network, on_delete=models.PROTECT, related_name='network_olt')

    def creationPorts(self):
        # Cria automaticamente as portas da OLT
        for i in range(1, self.ports_number + 1):
            p = Olt_port(number=i, olt=self)
            p.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # se o objeto for criado pela primeira vez,
        # inves de ser atualizado
        # a func save criará as portas dele,
        # comparando as datas de criaçao e atualizaçao
        if compareDates(self.created_at, self.updated_at):
            self.creationPorts()

    class Meta:
        verbose_name = 'OLT'
        verbose_name_plural = 'OLTS'
        db_table = u'"pop_netmanager\".\"tb_olts"'

    def __str__(self):
        return self.hostname + " - Rede: " + str(self.network)


class Olt_port(Port):
    '''Responsável pela gestão das portas da OLT'''
    olt = models.ForeignKey(
        Olt, on_delete=models.CASCADE, related_name='olt_port')

    class Meta:
        verbose_name = 'Porta da OLT'
        verbose_name_plural = 'Portas da OLT'
        db_table = u'"pop_netmanager\".\"tb_olt_ports"'

    def __str__(self):
        return " Porta: " + str(self.number) + " - " + str(self.olt)


class Cdi(models.Model):
    '''Responsável por gerenciar as CDI da OLT'''
    hostname = models.CharField(verbose_name='CDI', max_length=50)
    olt_port = models.OneToOneField(
        Olt_port, on_delete=models.CASCADE, related_name='olt_port_cdi')
    ports_number = models.IntegerField(verbose_name='No de Portas')
    created_at = models.DateTimeField(
        verbose_name='Criado em:', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Modificado em:', auto_now=True)

    def creationPorts(self):
        # Cria automaticamente as portas da Cdi
        for i in range(1, self.ports_number + 1):
            p = Cdi_port(number=i, cdi=self)
            p.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Cria as portas da Cdi
        if compareDates(self.created_at, self.updated_at):
            self.creationPorts()

    class Meta:
        verbose_name = 'CDI'
        verbose_name_plural = 'CDI'
        db_table = u'"pop_netmanager\".\"tb_cdis"'

    def __str__(self):
        return str(self.hostname) + " - " + str(self.olt_port)


class Cdi_port(Port):
    '''Responsável pela gestão das portas da CDI'''
    cdi = models.ForeignKey(
        Cdi, on_delete=models.CASCADE, related_name='cdi_port')

    class Meta:
        verbose_name = 'Porta da CDI'
        verbose_name_plural = 'Portas da CDI'
        db_table = u'"pop_netmanager\".\"tb_cdi_ports"'

    def __str__(self):
        return "Porta: " + str(self.number) + " - " + str(self.cdi)


class Ca1(models.Model):
    '''Responsável pela gestão das CA-1'''
    hostname = models.CharField(verbose_name='CA-1', max_length=50)
    cdi_port = models.OneToOneField(
        Cdi_port, on_delete=models.CASCADE, related_name='cdi_port_ca1')
    ports_number = models.IntegerField(verbose_name='No de Portas')
    created_at = models.DateTimeField(
        verbose_name='Criado em:', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Modificado em:', auto_now=True)

    def creationPorts(self):
        # Cria automaticamente as portas da CA-1
        for i in range(1, self.ports_number + 1):
            p = Ca1_port(number=i, ca1=self)
            p.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if compareDates(self.created_at, self.updated_at):
            self.creationPorts()

    class Meta:
        verbose_name = 'CA-1'
        verbose_name_plural = 'CA-1'
        db_table = u'"pop_netmanager\".\"tb_ca1s"'

    def __str__(self):
        return str(self.hostname) + " | " + str(self.cdi_port)


class Ca1_port(Port):
    '''Responsável pela gestão das portas da Ca-1'''
    ca1 = models.ForeignKey(
        Ca1, on_delete=models.CASCADE, related_name='ca1_port')

    class Meta:
        verbose_name = 'Porta da CA-1'
        verbose_name_plural = 'Portas da CA-1'
        db_table = u'"pop_netmanager\".\"tb_ca1_ports"'

    def __str__(self):
        return "Port: " + str(self.number) + " - " + str(self.ca1)


class Firewall(models.Model):
    '''Responsável pela Gestão do Firewalls nas Escolas'''
    hostname = models.CharField(verbose_name='Hostname-AP', max_length=100)
    ipv4_publico = models.GenericIPAddressField(
        verbose_name='IPV4 - Público', max_length=12, null=True, blank=True)
    ipv6_publico = models.GenericIPAddressField(
        verbose_name='IPV6 - Público', max_length=32, null=True, blank=True)
    sub_rede = models.GenericIPAddressField(
        verbose_name='SUB-REDE', max_length=12)
    range_ip_start = models.GenericIPAddressField(
        verbose_name='RANGE - INÍCIO', max_length=12)
    range_ip_end = models.GenericIPAddressField(
        verbose_name='RANGE - FINAL', max_length=12)
    obs = models.TextField(verbose_name='Observações:', blank=True)

    class Meta:
        db_table = u'"pop_netmanager\".\"tb_firewalls"'

    def __str__(self):
        return self.hostname


class Line_profile(models.Model):
    '''Responsável pela Gestão das Line-Profile'''
    hostname = models.CharField(verbose_name='Line Profile', max_length=50)

    class Meta:
        verbose_name = 'Line Profile'
        verbose_name_plural = 'Lines Profile'
        db_table = u'"pop_netmanager\".\"tb_lines_profile"'

    def __str__(self):
        return str(self.hostname)


class Vlan(models.Model):
    '''Responsável pela Gestão das VLAN'''
    hostname = models.CharField(verbose_name='Nome', max_length=50)
    vlan_id = models.CharField(verbose_name='ID', max_length=4, unique=True)

    class Meta:
        verbose_name = 'VLAN'
        verbose_name_plural = 'VLANS'
        db_table = u'"pop_netmanager\".\"tb_vlans"'

    def __str__(self):
        return str(self.hostname) + " ID: " + str(self.vlan_id)


class Vman(Vlan):
    '''Classe responsável pela gestão da VMAN'''

    class Meta:
        verbose_name = 'V-MAN'
        verbose_name_plural = 'V-MAN'
        db_table = u'"pop_netmanager\".\"tb_vmans"'


class Cvlan(Vlan):
    '''Classe responsável pela gestão das C-VLANS'''

    class Meta:
        verbose_name = 'C-VLAN'
        verbose_name_plural = 'C-VLAN'
        db_table = u'"pop_netmanager\".\"tb_cvlans"'


class Vlan_management(Vlan):
    '''Classe responsável pela gestão das VLANs de Gerência'''
    ipv4_address = models.GenericIPAddressField(
        verbose_name='Address - IPV4', max_length=12, null=True, blank=True)
    ipv6_address = models.GenericIPAddressField(
        verbose_name='Address - IPV6', max_length=32, null=True, blank=True)
    ipv4_gateway = models.GenericIPAddressField(
        verbose_name='Gateway IPV4', max_length=12, null=True, blank=True)
    ipv6_gateway = models.GenericIPAddressField(
        verbose_name='Gateway IPV6', max_length=32, null=True, blank=True)

    class Meta:
        abstract = True


class Vlan_management_ap(Vlan_management):
    '''Classe responsável pela gestão das VLANs de Gerência AP'''

    class Meta:
        verbose_name = 'VLAN - GERÊNCIA AP'
        verbose_name_plural = 'VLANS - GERÊNCIA AP'
        db_table = u'"pop_netmanager\".\"tb_vlan_management_ap"'


class Vlan_management_sw(Vlan_management):
    '''Classe responsável pela gestão das VLANs de Gerência SW'''

    class Meta:
        verbose_name = 'VLAN - GERÊNCIA SW'
        verbose_name_plural = 'VLANS - GERÊNCIA SW'
        db_table = u'"pop_netmanager\".\"tb_vlan_management_sw"'


class Vlan_management_onu(Vlan_management):
    '''Classe responsável pela gestão das VLANs de Gerência ONU'''

    class Meta:
        verbose_name = 'VLAN - GERÊNCIA ONU'
        verbose_name_plural = 'VLANS - GERÊNCIA ONU'
        db_table = u'"pop_netmanager\".\"tb_vlan_management_onu"'


class Svlan(Vlan):
    '''Classe responsável pela gestão das S-VLANS'''
    ipv4_publico = models.GenericIPAddressField(
        verbose_name='IPV4 - PÚBLICO',
        max_length=12, null=True, blank=True)
    ipv6_publico = models.GenericIPAddressField(
        verbose_name='IPV6 - PÚBLICO',
        max_length=32, null=True, blank=True)
    ipv4_privado = models.GenericIPAddressField(
        verbose_name='IPV4 - PRIVADO',
        max_length=12, null=True, blank=True)
    ipv6_privado = models.GenericIPAddressField(
        verbose_name='IPV6 - PRIVADO',
        max_length=32, null=True, blank=True)
    sub_rede_ipv4 = models.GenericIPAddressField(
        verbose_name='SUB-REDE IPV4',
        max_length=12, null=True, blank=True)
    sub_rede_ipv6 = models.GenericIPAddressField(
        verbose_name='SUB-REDE IPV6',
        max_length=32, null=True, blank=True)
    range_start_ipv4 = models.GenericIPAddressField(
        verbose_name='RANGE INÍCIO - IPV4',
        max_length=12, null=True, blank=True)
    range_end_ipv4 = models.GenericIPAddressField(
        verbose_name='RANGE FINAL - IPV4',
        max_length=12, null=True, blank=True)
    range_start_ipv6 = models.GenericIPAddressField(
        verbose_name='RANGE INÍCIO - IPV6',
        max_length=32, null=True, blank=True)
    range_end_ipv6 = models.GenericIPAddressField(
        verbose_name='RANGE FINAL - IPV6',
        max_length=32, null=True, blank=True)
    bw_up = models.CharField(
        verbose_name='BW-UP',
        max_length=15, null=True, blank=True)
    bw_down = models.CharField(
        verbose_name='BW-DW',
        max_length=15, null=True, blank=True)
    firewall = models.ForeignKey(
        Firewall, on_delete=models.SET_NULL,
        related_name='firewall_svlan',
        null=True, blank=True)
    c_vlan = models.ForeignKey(
        Cvlan, on_delete=models.SET_NULL,
        related_name='cvlan_svlan',
        null=True, blank=True)
    v_man = models.ForeignKey(
        Vman, on_delete=models.SET_NULL,
        related_name='vman_svlan',
        null=True, blank=True)
    client = models.ForeignKey(
        Client, verbose_name='Cliente',
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'S-VLAN'
        verbose_name_plural = 'S-VLAN'
        db_table = u'"pop_netmanager\".\"tb_svlans"'

    def __str__(self):
        return self.hostname + " ID:" + self.vlan_id


class Device(models.Model):
    '''Responsável pela gestão das reservas de endereços ip na S-VLAN'''
    hostname = models.CharField(verbose_name='Dispositivo', max_length=100)
    ipv4_address = models.GenericIPAddressField(
        verbose_name='Address - IPV4', max_length=12, null=True, blank=True)
    ipv6_address = models.GenericIPAddressField(
        verbose_name='Address - IPV6', max_length=32, null=True, blank=True)
    s_vlan = models.ForeignKey(
        Svlan, on_delete=models.CASCADE, related_name='svlan_devices')

    class Meta:
        verbose_name = 'Dispositivo'
        verbose_name_plural = 'Dispositivos'
        db_table = u'"pop_netmanager\".\"tb_svlan_devices"'

    def __str__(self):
        return "Dispositivo: " + str(self.hostname) + \
            " | Reserva : " + str(self.s_vlan)


class Onu(models.Model):
    '''Responsável pela gestão da ONU - MODEM'''
    onu_id = models.CharField(verbose_name='ONU - ID', max_length=4)
    hostname = models.CharField(verbose_name='Hostname-ONU', max_length=100)
    serial = models.CharField(verbose_name='Serial', max_length=50)
    ipv4_publico = models.GenericIPAddressField(
        verbose_name='IPV4 - Público', max_length=12, null=True, blank=True)
    ipv6_publico = models.GenericIPAddressField(
        verbose_name='IPV6 - Público', max_length=32, null=True, blank=True)
    bw_up = models.CharField(verbose_name='BW-UP', max_length=15)
    bw_down = models.CharField(verbose_name='BW-DW', max_length=15)
    user1 = models.CharField(verbose_name='USER 1', max_length=10)
    user2 = models.CharField(verbose_name='USER 2', max_length=10)
    password = models.CharField(verbose_name='Password', max_length=25)
    ports_number = models.IntegerField(
        verbose_name='No de Portas')
    created_at = models.DateTimeField(
        verbose_name='Criado em:',
        auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Modificado em:',
        auto_now=True)
    line_profile = models.ForeignKey(
        Line_profile,
        verbose_name='line profile',
        on_delete=models.CASCADE)
    s_vlan = models.ManyToManyField(
        Svlan,
        db_table=u'"pop_netmanager\".\"tb_onu_svlans"',
        verbose_name=('Svlan(s)'))
    # s_vlan = models.ManyToManyField(Svlan)
    ca1_port = models.OneToOneField(
        Ca1_port,
        verbose_name='Porta da CA-1',
        on_delete=models.CASCADE,
        related_name='ca1_port_onu')
    vlan_management_onu = models.ForeignKey(
        Vlan_management_onu,
        verbose_name='V-LAN GERÊNCIA',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='vlan_management_onu')

    def creationPorts(self):
        # Cria automaticamente as portas da ONU
        for i in range(1, self.ports_number + 1):
            p = Onu_port(number=i, onu=self)
            p.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Criação das portas da ONU
        if compareDates(self.created_at, self.updated_at):
            self.creationPorts()

    class Meta:
        verbose_name = 'ONU - Modem'
        verbose_name_plural = 'ONU - Modens'
        db_table = u'"pop_netmanager\".\"tb_onus"'

    def __str__(self):
        return str(self.hostname) + " - ID: " + str(self.onu_id)


class Onu_port(Port):
    '''Responsável pela gestão das portas da ONU'''
    onu = models.ForeignKey(
        Onu, on_delete=models.CASCADE, related_name='onu_port')

    class Meta:
        verbose_name = 'Porta da ONU'
        verbose_name_plural = 'Portas da ONU'
        db_table = u'"pop_netmanager\".\"tb_onu_ports"'

    def __str__(self):
        return "Porta: " + str(self.number) + " - " + str(self.onu)


class Switch(models.Model):
    '''Responsável pela Gestão dos Switches nos Clientes do POP-RN'''
    hostname = models.CharField(verbose_name='Hostname-SW', max_length=100)
    serial = models.CharField(verbose_name='S/N', max_length=50)
    mac_address = models.CharField(verbose_name='Endereço MAC', max_length=12)
    ip_address = models.GenericIPAddressField(
        verbose_name='Endereço IP', max_length=12)
    telnet = models.BooleanField(verbose_name='TELNET')
    ssh = models.BooleanField(verbose_name='SSH')
    snmp = models.BooleanField(verbose_name='SNMP')
    user1 = models.CharField(verbose_name='USER 1', max_length=10)
    user2 = models.CharField(verbose_name='USER 2', max_length=10)
    sntp_client = models.BooleanField(verbose_name='SNTP Client')
    default_route = models.GenericIPAddressField(
        verbose_name='Rota Default', max_length=12)
    erlp = models.BooleanField(verbose_name='ERLP')
    dhcp_snooping = models.BooleanField(verbose_name='DHCP SNOOPING')
    port_poe = models.CharField(
        verbose_name='Porta PoE',
        max_length=5, blank=True, null=True)
    ports_number = models.IntegerField(
        verbose_name='No de Portas')
    created_at = models.DateTimeField(
        verbose_name='Criado em:',
        auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Modificado em:',
        auto_now=True)
    onu_port = models.OneToOneField(
        Onu_port, verbose_name='Porta - ONU',
        on_delete=models.SET_NULL,
        null=True, blank=True, related_name='onu_port_switches')
    vlan_management_sw = models.ForeignKey(
        Vlan_management_sw,
        verbose_name='V-LAN GERÊNCIA',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='vlan_management_switch')

    class Meta:
        verbose_name = 'Switch'
        verbose_name_plural = 'Switches'
        ordering = ['hostname']
        db_table = u'"pop_netmanager\".\"tb_switches"'

    def __str__(self):
        return str(self.hostname) + " | " + str(self.onu_port)

    def creationPorts(self):
        # Cria automaticamente as portas do Switch
        for i in range(1, self.ports_number + 1):
            p = Switch_port(number=i, switch=self)
            p.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Criação das portas associadas ao Switch, apenas na criação do Switch
        if compareDates(self.created_at, self.updated_at):
            self.creationPorts()
        if compareDates(self.created_at, self.updated_at):
            vlan_switch = Vlan_switch(
                switch=self, vlan=self.vlan_management_sw)
            vlan_switch.save()


class Switch_port(Port):
    '''Responsável pela gestão das portas dos Switches'''
    # disable = False / enable = True
    enable = models.BooleanField(
        verbose_name='Habilitado', default=False, null=True, blank=True)
    switch = models.ForeignKey(
        Switch, on_delete=models.CASCADE,
        related_name='switch_ports', null=True, blank=True)

    class Meta:
        verbose_name = 'Porta do Switch'
        verbose_name_plural = 'Portas do Switch'
        db_table = u'"pop_netmanager\".\"tb_switch_ports"'

    def __str__(self):
        return "Porta: " + str(self.number) + " | SWITCH: " + str(self.switch)


class Vlan_port(Port):
    '''Resposável pela gestão da configuração
        das portas da Vlan de Gerência no Switch'''
    # Tagged = True / Untagged = False
    status = models.BooleanField(
        verbose_name='Tagged',
        default=False, null=True, blank=True)
    switch = models.ForeignKey(
        Switch, on_delete=models.CASCADE,
        related_name='vlan_switches')
    vlan = models.ForeignKey(
        Vlan, on_delete=models.CASCADE,
        related_name='vlan_ports')

    class Meta:
        verbose_name = 'Porta da Vlan'
        verbose_name_plural = 'Portas da Vlan'
        db_table = u'"pop_netmanager\".\"tb_vlan_ports"'

    def __str__(self):
        return "Porta: " + str(self.number) +\
            " | VLAN: " + str(self.vlan) + " | SWITCH: " + str(self.switch)


class Vlan_switch(models.Model):
    '''Gestão das portas da VLAN no Switch'''
    switch = models.ForeignKey(
        Switch, on_delete=models.CASCADE,
        related_name='vlan_switch')
    vlan = models.ForeignKey(
        Vlan, on_delete=models.CASCADE,
        related_name='switch_vlan')
    created_at = models.DateTimeField(
        verbose_name='Criado em:', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Modificado em:', auto_now=True)

    def creationPorts(self):
        # Cria automaticamente as portas da Vlan associadas ao Switch
        ports_number = self.switch.switch_ports.all().count()
        for i in range(1, ports_number + 1):
            p = Vlan_port(number=i, vlan=self.vlan, switch=self.switch)
            p.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.creationPorts()

    class Meta:
        verbose_name = 'VLAN - Switch'
        verbose_name_plural = 'VLANS - Switch'
        db_table = u'"pop_netmanager\".\"tb_vlan_switches"'

    def __str__(self):
        return "VLAN: " + str(self.vlan) + " | Switch: " + str(self.switch)


class AccessPoint(models.Model):
    '''Responsável pela Gestão do Access Points nas Escolas'''
    hostname = models.CharField(verbose_name='Hostname-AP', max_length=50)
    serial = models.CharField(verbose_name='S/N', max_length=50)
    mac_address = models.CharField(verbose_name='Endereço MAC', max_length=12)
    wlan_aluno = models.CharField(verbose_name='Wlan Aluno', max_length=50)
    wlan_admin = models.CharField(verbose_name='Wlan Admin', max_length=50)
    switch_port = models.OneToOneField(
        Switch_port,
        on_delete=models.CASCADE)
    vlan_management_ap = models.ForeignKey(
        Vlan_management_ap,
        verbose_name='GERÊNCIA-AP',
        on_delete=models.SET_NULL, null=True, blank=True,
        related_name='vlan_management_ap')

    class Meta:
        verbose_name = 'Access Point'
        verbose_name_plural = 'Access Points'
        db_table = u'"pop_netmanager\".\"tb_accesspoints"'

    def __str__(self):
        return str(self.hostname) + \
            " | Switch: " + str(self.switch_port.switch)
