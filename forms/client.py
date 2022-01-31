from pop_erp.apps.pop_netmanager.models.client import Client
from bootstrap_modal_forms.forms import BSModalForm


class ClientForm(BSModalForm):
    class Meta:
        model = Client
        fields = ('id', 'description', 'name', 'code', 'place', 'entity')

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required': 'O campo {fieldname} é \
                obrigatório.'.format(
                fieldname=field.label)}
