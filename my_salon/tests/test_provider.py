from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestProviderModel(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestProviderModel, self).setUp(*args, **kwargs)
        self.provider_model = self.env['provider']

    def test_name_required(self):
        "Тестирование обязательности поля name для модели Provider"
        with self.assertRaises(ValidationError, msg="Should raise a ValidationError or similar if the name field is missing"):
            # Попытка создать запись поставщика без указания обязательного поля name
            self.provider_model.create({
                # Поле name не указано
                'phone': '123456789',  # Указание других необязательных полей
                'address': 'Test Address',
            })
