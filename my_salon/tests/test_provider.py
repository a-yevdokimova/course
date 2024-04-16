from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestProviderModel(TransactionCase):
    """
    Test cases for the Provider model to ensure the integrity and requirements
    of the provider data.
    """

    def setUp(self):
        """
        Set up initial data for the tests.
        """
        super(TestProviderModel, self).setUp()
        self.Provider = self.env['provider']
        self.Product = self.env['product']
        # Create a product to use in the Many2many relationship
        self.product = self.Product.create({'name': 'Test Product'})

    def test_create_provider_with_required_fields(self):
        """
        Test provider is correctly created with all required fields.
        """
        provider = self.Provider.create({
            'name': 'Test Provider',
            'phone': '123456789',
            'address': '123 Test Lane',
            'product_ids': [(4, self.product.id)]
        })
        self.assertEqual(provider.name, 'Test Provider')
        self.assertEqual(provider.phone, '123456789')
        self.assertEqual(provider.address, '123 Test Lane')
        self.assertIn(self.product, provider.product_ids)

    def test_check_many2many_relationship(self):
        """
        Test the Many2many relationship with the product model.
        """
        provider = self.Provider.create({
            'name': 'Another Test Provider',
            'product_ids': [(4, self.product.id)]
        })
        self.assertTrue(provider.product_ids)
        self.assertIn(self.product, provider.product_ids)
