from datetime import datetime
from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestAppointmentConstraints(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestAppointmentConstraints, self).setUp(*args, **kwargs)
        # Подготовка данных для тестирования
        self.client_id = self.env['client'].create({'name': 'Test', 'second_name': 'Client'}).id
        self.master_id = self.env['master'].create({'name': 'Test Master',  'second_name': 'Client'}).id
        self.service_id = self.env['my_service'].create({'name': 'Test Service', 'duration': 1}).id

    def test_check_time_range_valid(self):
        "Тестирование корректного временного интервала"
        start_time = datetime(2024, 4, 8, 10, 0, 0)  # Статическое значение времени начала
        end_time = datetime(2024, 4, 8, 11, 0, 0)  # Статическое значение времени окончания, валидный интервал
        appointment = self.env['appointment'].create({
            'client_id': self.client_id,
            'master_id': self.master_id,
            'service_id': self.service_id,
            'start_time': start_time,
            'end_time': end_time,
        })
        # Проверка создания записи без возникновения исключения
        self.assertTrue(appointment, "Appointment should be successfully created with a valid time range.")