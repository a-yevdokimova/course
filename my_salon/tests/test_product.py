from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestProductModel(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestProductModel, self).setUp(*args, **kwargs)
        self.product_model = self.env['product']

    def test_name_required(self):
        "Тестирование обязательности поля name"
        with self.assertRaises(ValidationError, msg="Should raise a ValidationError if the name field is missing"):
            # Попытка создать продукт без указания обязательного поля name
            self.product_model.create({
                # Не указываем name
                'price': 10.0,  # Указываем цену для имитации заполнения других полей
            })
