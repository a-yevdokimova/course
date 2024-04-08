from odoo.tests.common import SavepointCase
from odoo.exceptions import ValidationError

class TestClientModel(SavepointCase):

    @classmethod
    def setUpClass(cls):
        super(TestClientModel, cls).setUpClass()
        cls.Client = cls.env['client']

    def test_check_child_age_valid(self):
        "Тестирование валидного возраста для детей"
        # Создание записи клиента с корректным возрастом для ребенка
        child_client = self.Client.create({
            'name': 'Child Client',
            'second_name': 'Test',
            'age': 10,  # Валидный возраст ребенка
            'is_child': True,
        })
        self.assertTrue(child_client, "Client record should be successfully created with valid age for child.")

    def test_check_child_age_invalid(self):
        "Тестирование невалидного возраста для детей"
        with self.assertRaises(ValidationError, msg="Should raise a ValidationError if a child client has an age of 0"):
            # Попытка создать запись клиента с некорректным возрастом ребенка
            self.Client.create({
                'name': 'Invalid Age Child',
                'second_name': 'Test',
                'age': 0,  # Невалидный возраст ребенка
                'is_child': True,
            })

    def test_child_age_auto_mark(self):
        "Тест автоматической установки is_child на основе возраста"
        # Создание записи клиента без явного указания is_child, но с возрастом <= 18
        auto_child_client = self.Client.create({
            'name': 'Auto Child',
            'second_name': 'Test',
            'age': 15,  # Возраст, при котором is_child должен автоматически установиться в True
        })
        self.assertTrue(auto_child_client.is_child, "Client should be automatically marked as child based on age.")