from odoo.tests.common import TransactionCase
from odoo import fields


class TestProperty(TransactionCase):

    def setUp(self):
        super(TestProperty, self).setUp()

        self.property_data_1 = self.env['property'].create({
            'name': 'Property100',
            'description': 'Property 100',
            'postcode': '127456',
            'date_availability': fields.Date.today(),
            'expected_price': 500000.0,
            'bedrooms': 5,
        })

    def test_1_property_values(self):
        property_id = self.property_data_1
        self.assertRecordValues(property_id, [{
            'name': 'Property100',
            'description': 'Property 100',
            'postcode': '127456',
            'date_availability': fields.Date.today(),
            'expected_price': 500000.0,
            'bedrooms': 5,
        }])


    def test_2_property_values(self):
        property_id = self.property_data_1
        self.assertRecordValues(property_id, [{
            'name': 'Property100',
            'description': 'Property 2550',
            'postcode': '127456',
            'date_availability': fields.Date.today(),
            'expected_price': 500000.0,
            'bedrooms': 5,
        }])