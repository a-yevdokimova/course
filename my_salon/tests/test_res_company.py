from odoo.tests.common import TransactionCase

class TestResCompanySocialMedia(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestResCompanySocialMedia, self).setUp(*args, **kwargs)

        # Создаем или ищем существующую тестовую компанию
        self.test_company = self.env['res.company'].search([], limit=1)
        if not self.test_company:
            self.test_company = self.env['res.company'].create({'name': 'Test Company'})

    def test_social_media_fields(self):
        """Тестирование полей социальных сетей"""

        # Задаем значения полей
        self.test_company.instagram = 'testinstagram'
        self.test_company.telegram = 'testtelegram'

        # Проверяем, что поля были корректно заданы
        self.assertEqual(self.test_company.instagram, 'testinstagram', "Instagram handle was not set correctly.")
        self.assertEqual(self.test_company.telegram, 'testtelegram', "Telegram handle was not set correctly.")

        # Обновляем значения полей
        self.test_company.write({
            'instagram': 'updatedinstagram',
            'telegram': 'updatedtelegram',
        })

        # Проверяем, что поля были корректно обновлены
        self.assertEqual(self.test_company.instagram, 'updatedinstagram', "Instagram handle was not updated correctly.")
        self.assertEqual(self.test_company.telegram, 'updatedtelegram', "Telegram handle was not updated correctly.")
