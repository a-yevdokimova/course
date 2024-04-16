from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestProductModel(TransactionCase):
    """
    Test cases for the Product model to ensure the integrity and requirements
    of product data.
    """

    def setUp(self):
        """
        Set up initial data for the tests.
        """
        super(TestProductModel, self).setUp()
        self.Product = self.env['product']
        self.Provider = self.env['provider']
        self.Currency = self.env['res.currency'].search([], limit=1)  # Assuming at least one currency exists
        # Create a provider to use in the Many2many relationship
        self.provider = self.Provider.create({'name': 'Sample Provider'})

    def test_create_product_with_required_fields(self):
        """
        Test that a product can be created with all required fields.
        """
        product = self.Product.create({
            'name': 'New Product',
            'price': 10.50,
            'currency_id': self.Currency.id
        })
        self.assertEqual(product.name, 'New Product')
        self.assertAlmostEqual(product.price, 10.50)
        self.assertEqual(product.currency_id, self.Currency)

    def test_check_many2many_relationship(self):
        """
        Test the Many2many relationship with the provider model.
        """
        product = self.Product.create({
            'name': 'Another Product',
            'provider_ids': [(4, self.provider.id)],
            'price': 15.00,
            'currency_id': self.Currency.id
        })
        self.assertTrue(product.provider_ids)
        self.assertIn(self.provider, product.provider_ids)

    def test_currency_relationship(self):
        """
        Test that the currency relationship is correctly set up for the product.
        """
        product = self.Product.create({
            'name': 'Currency Test Product',
            'price': 30.00,
            'currency_id': self.Currency.id
        })
        self.assertEqual(product.currency_id, self.Currency)
