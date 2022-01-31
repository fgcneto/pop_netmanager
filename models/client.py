'''Responsável pelo gestão dos Clientes e seus respectivos contatos'''
from django.db import models
from pop_erp.apps.pop_inventario.models.transfer import Locale


class Client(Locale):
    '''Classe responsável pela gestão dos Clientes'''
    name = models.CharField(verbose_name='Nome', max_length=150)
    code = models.CharField(verbose_name='Código', max_length=10)
    PLACE_CHOICES = [
        ("0", "Macaíba"),
        ("1", "Parnamirim"),
        ("2", "Natal"),
        ("3", "São Gonçalo do Amarante"),
    ]
    place = models.CharField(verbose_name='Local',
                             max_length=1, choices=PLACE_CHOICES)
    ENTITY_CHOICES = [
        ("0", "Municipal"),
        ("1", "Estadual"),
        ("3", "Federal")
    ]
    entity = models.CharField(verbose_name='Entidade',
                              max_length=1, choices=ENTITY_CHOICES)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = u'"pop_netmanager\".\"tb_clients"'

    def __str__(self):
        return self.name


class Contact(models.Model):
    '''Classe responsável pela gestão dos contatos dos Clientes'''
    name = models.CharField(verbose_name='Nome', max_length=150)
    email = models.EmailField(verbose_name='E-mail', max_length=100)
    client = models.ForeignKey(
        Client, verbose_name='Cliente', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        db_table = u'"pop_netmanager\".\"tb_contacts"'

    def __str__(self):
        return "Nome: " + str(self.name) + " | Cliente: " + str(self.client)
