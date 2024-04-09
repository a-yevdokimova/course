from odoo.tests.common import TransactionCase


class TestStockPickingExtension(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestStockPickingExtension, self).setUp(*args, **kwargs)
        self.stock_picking_model = self.env['stock.picking']

    def test_provider_id_field_presence(self):
        "Проверка наличия поля provider_id в модели StockPicking"
        # Получаем список всех полей модели stock.picking
        fields_list = self.stock_picking_model.fields_get()

        # Проверяем, что в этом списке присутствует поле provider_id
        self.assertIn('provider_id', fields_list,
                      "The field 'provider_id' should be present in the StockPicking model.")
