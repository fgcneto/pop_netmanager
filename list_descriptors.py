# Descritor de listas da aplicação PoP-Network Manager
# ID a partir de 300 a 399

modules = {
    # Descritores da app pop_netmanager
    "redes": {
        # Identificacao do modulo
        'id': '300',
        # Nome do controlador do módulo
        'module': 'pop_netmanager:rede',
        # Título singular do módulo
        'singular_title': ' Rede ',
        # Título plural do módulo
        'title': 'Redes',
        # Descrição do módulo
        'description': 'Lista analítica das Redes em Operação \
        no PoP-RN',
        # Font-awesome mostrada na tela de listagem
        'font': 'sitemap',
        # Cadastro em Modal 0-false 1-true
        'ajax': '1'
    },

    "clientes": {
        # Identificacao do modulo
        'id': '301',
        # Nome do controlador do módulo
        'module': 'pop_netmanager:cliente',
        # Título singular do módulo
        'singular_title': ' Cliente ',
        # Título plural do módulo
        'title': 'Clientes',
        # Descrição do módulo
        'description': 'Lista analítica dos Clientes \
        do PoP-RN',
        # Font-awesome mostrada na tela de listagem
        'font': 'sitemap',
        # Cadastro em Modal 0-false 1-true
        'ajax': '1'
    },

    "olts": {
        # Identificacao do modulo
        'id': '302',
        # Nome do controlador do módulo
        'module': 'pop_netmanager:olt',
        # Título singular do módulo
        'singular_title': ' OLT ',
        # Título plural do módulo
        'title': 'OLTS',
        # Descrição do módulo
        'description': 'Lista analítica das OLTS \
        do PoP-RN',
        # Font-awesome mostrada na tela de listagem
        'font': 'sitemap',
        # Cadastro em Modal 0-false 1-true
        'ajax': '1'
    },
    "cdis": {
        # Identificacao do modulo
        'id': '303',
        # Nome do controlador do módulo
        'module': 'pop_netmanager:cdi',
        # Título singular do módulo
        'singular_title': ' CDI ',
        # Título plural do módulo
        'title': 'CDI',
        # Descrição do módulo
        'description': 'Lista analítica das CDI em Operação \
        no PoP-RN',
        # Font-awesome mostrada na tela de listagem
        'font': 'sitemap',
        # Cadastro em Modal: 0-false 1-true
        'ajax': '1'
    },
    "ca1s": {
        # Identificacao do modulo
        'id': '304',
        # Nome do controlador do módulo
        'module': 'pop_netmanager:ca1',
        # Título singular do módulo
        'singular_title': ' CA-1 ',
        # Título plural do módulo
        'title': 'CA-1',
        # Descrição do módulo
        'description': 'Lista analítica das CA-1 em Operação \
        no PoP-RN',
        # Font-awesome mostrada na tela de listagem
        'font': 'sitemap',
        # Cadastro em Modal: 0-false 1-true
        'ajax': '1'
    },
    "vmans": {
        # Identificacao do modulo
        'id': '305',
        # Nome do controlador do módulo
        'module': 'pop_netmanager:vman',
        # Título singular do módulo
        'singular_title': ' V-MAN ',
        # Título plural do módulo
        'title': 'V-MAN',
        # Descrição do módulo
        'description': 'Lista analítica das V-MAN em Operação \
        no PoP-RN',
        # Font-awesome mostrada na tela de listagem
        'font': 'sitemap',
        # Cadastro em Modal: 0-false 1-true
        'ajax': '1'
    },
    "cvlans": {
        # Identificacao do modulo
        'id': '306',
        # Nome do controlador do módulo
        'module': 'pop_netmanager:cvlan',
        # Título singular do módulo
        'singular_title': ' C-VLAN ',
        # Título plural do módulo
        'title': 'C-VLAN',
        # Descrição do módulo
        'description': 'Lista analítica das C-VLAN em Operação \
        no PoP-RN',
        # Font-awesome mostrada na tela de listagem
        'font': 'sitemap',
        # Cadastro em Modal: 0-false 1-true
        'ajax': '1'
    },
    "firewalls": {
        # Identificacao do modulo
        'id': '307',
        # Nome do controlador do módulo
        'module': 'pop_netmanager:firewall',
        # Título singular do módulo
        'singular_title': 'FIREWALL',
        # Título plural do módulo
        'title': 'FIREWALL',
        # Descrição do módulo
        'description': 'Lista analítica dos Firewalls em Operação \
        no PoP-RN',
        # Font-awesome mostrada na tela de listagem
        'font': 'sitemap',
        # Cadastro em Modal: 0-false 1-true
        'ajax': '0'
    },
    "vlanaps": {
        # Identificacao do modulo
        'id': '308',
        # Nome do controlador do módulo
        'module': 'pop_netmanager:vlanap',
        # Título singular do módulo
        'singular_title': 'VLAN GERÊNCIA-AP',
        # Título plural do módulo
        'title': 'VLAN GERÊNCIA-AP',
        # Descrição do módulo
        'description': 'Lista analítica das V-LANS de Gerência dos Access Points em Operação \
        no PoP-RN',
        # Font-awesome mostrada na tela de listagem
        'font': 'sitemap',
        # Cadastro em Modal: 0-false 1-true
        'ajax': '0'
    },
    "vlansws": {
        # Identificacao do modulo
        'id': '309',
        # Nome do controlador do módulo
        'module': 'pop_netmanager:vlansw',
        # Título singular do módulo
        'singular_title': 'VLAN GERÊNCIA-SW',
        # Título plural do módulo
        'title': 'VLAN GERÊNCIA-SW',
        # Descrição do módulo
        'description': 'Lista analítica das V-LANS de Gerência dos Swicthes em Operação \
        no PoP-RN',
        # Font-awesome mostrada na tela de listagem
        'font': 'sitemap',
        # Cadastro em Modal: 0-false 1-true
        'ajax': '0'
    },
    "vlanonus": {
        # Identificacao do modulo
        'id': '310',
        # Nome do controlador do módulo
        'module': 'pop_netmanager:vlanonu',
        # Título singular do módulo
        'singular_title': 'VLAN GERÊNCIA-ONU',
        # Título plural do módulo
        'title': 'VLAN GERÊNCIA-ONU',
        # Descrição do módulo
        'description': 'Lista analítica das V-LANS de Gerência das ONU em Operação \
        no PoP-RN',
        # Font-awesome mostrada na tela de listagem
        'font': 'sitemap',
        # Cadastro em Modal: 0-false 1-true
        'ajax': '0'
    },
    "svlans": {
        # Identificacao do modulo
        'id': '311',
        # Nome do controlador do módulo
        'module': 'pop_netmanager:svlan',
        # Título singular do módulo
        'singular_title': 'S-VLAN',
        # Título plural do módulo
        'title': 'S-VLAN',
        # Descrição do módulo
        'description': 'Lista analítica das S-VLANS em Operação \
        no PoP-RN',
        # Font-awesome mostrada na tela de listagem
        'font': 'sitemap',
        # Cadastro em Modal: 0-false 1-true
        'ajax': '0'
    },
    "devices": {
        # Identificacao do modulo
        'id': '312',
        # Nome do controlador do módulo
        'module': 'pop_netmanager:device',
        # Título singular do módulo
        'singular_title': 'Dispositivo',
        # Título plural do módulo
        'title': 'Dispositivos',
        # Descrição do módulo
        'description': 'Lista analítica das Reservas dos Endereços IP \
        para os Dispositivos da S-VLAN',
        # Font-awesome mostrada na tela de listagem
        'font': 'sitemap',
        # Cadastro em Modal: 0-false 1-true
        'ajax': '1'
    },
    "lines_profile": {
        # Identificacao do modulo
        'id': '313',
        # Nome do controlador do módulo
        'module': 'pop_netmanager:line_profile',
        # Título singular do módulo
        'singular_title': 'Line Profile',
        # Título plural do módulo
        'title': 'Lines Profile',
        # Descrição do módulo
        'description': 'Lista analítica das Line Profile em Operação \
            no POP-RN',
        # Font-awesome mostrada na tela de listagem
        'font': 'sitemap',
        # Cadastro em Modal: 0-false 1-true
        'ajax': '1'
    },
    "switches": {
        # Identificacao do modulo
        'id': '314',
        # Nome do controlador do módulo
        'module': 'pop_netmanager:switch',
        # Título singular do módulo
        'singular_title': 'Switch',
        # Título plural do módulo
        'title': 'Switches',
        # Descrição do módulo
        'description': 'Lista analítica das Switches em Operação no POP-RN',
        # Font-awesome mostrada na tela de listagem
        'font': 'sitemap',
        # Cadastro em Modal: 0-false 1-true
        'ajax': '0'
    },
    "onus": {
        # Identificacao do modulo
        'id': '315',
        # Nome do controlador do módulo
        'module': 'pop_netmanager:onu',
        # Título singular do módulo
        'singular_title': 'ONU',
        # Título plural do módulo
        'title': 'ONU',
        # Descrição do módulo
        'description': 'Lista analítica das Swichtes em Operação no POP-RN',
        # Font-awesome mostrada na tela de listagem
        'font': 'sitemap',
        # Cadastro em Modal: 0-false 1-true
        'ajax': '0'
    },
    "accesspoints": {
        # Identificacao do modulo
        'id': '316',
        # Nome do controlador do módulo
        'module': 'pop_netmanager:accesspoint',
        # Título singular do módulo
        'singular_title': 'Access Point',
        # Título plural do módulo
        'title': 'Access Point',
        # Descrição do módulo
        'description': 'Lista analítica dos Access Points \
            em Operação no POP-RN',
        # Font-awesome mostrada na tela de listagem
        'font': 'sitemap',
        # Cadastro em Modal: 0-false 1-true
        'ajax': '0'
    },
}

apiroute = {
    "netmanager": {
        'route': '../netmanager/api/',
    }

}


class List_descriptors:

    def __init__(self, application, module):
        self.application = application
        self.module = module

    def get_module(self):
        return modules.get(self.module)

    def get_apiroute(self):
        return apiroute.get(self.application)
