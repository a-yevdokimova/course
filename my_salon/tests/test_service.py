from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestServiceModel(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestServiceModel, self).setUp(*args, **kwargs)
        self.service_model = self.env['my_service']

    def test_duration_required(self):
        "Проверка, что поле duration является обязательным"
        with self.assertRaises(ValidationError, msg="Creating a service without a duration should raise a ValidationError"):
            # Попытка создать запись без указания обязательного поля duration
            self.service_model.create({
                'name': 'Test Service Without Duration',
                # Не указываем duration
            })

    def test_create_service_with_duration(self):
        "Проверка успешного создания сервиса с указанием duration"
        service = self.service_model.create({
            'name': 'Test Service',
            'duration': 1.5,  # Указываем длительность в часах
        })
        self.assertTrue(service, "The service should have been successfully created.")
        self.assertEqual(service.duration, 1.5, "The duration of the service should be correctly set.")
