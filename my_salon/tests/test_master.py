from odoo.tests.common import TransactionCase


class TestMasterModel(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestMasterModel, self).setUp(*args, **kwargs)
        # Создание записей для тестирования
        self.master_model = self.env['master']
        self.test_master = self.master_model.create({
            'name': 'John',
            'second_name': 'Doe',
            'gender': 'male',
            'ref': 'MSTR0001'
        })

    def test_name_get(self):
        "Тестирование кастомизации отображаемого имени"
        # Получаем отображаемое имя созданной записи
        display_name_expected = 'MSTR0001 - John'
        display_names = self.test_master.name_get()

        # Проверяем, что возвращается только одна запись и что имя формируется правильно
        self.assertEqual(len(display_names), 1, "Should return exactly one name.")
        self.assertEqual(display_names[0][1], display_name_expected, "The display name is not correctly formatted.")
