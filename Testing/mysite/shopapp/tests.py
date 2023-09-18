from django.contrib.auth.models import User, Permission
from django.test import TestCase
from django.urls import reverse

from .models import Order


class OrderDetailViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create(username='test', password='qwerty')
        permission_order = Permission.objects.get(codename='view_order')
        cls.user.user_permissions.add(permission_order)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)
        self.order = Order.objects.create(
            delivery_address='ul Mira, d 34',
            promocode='SALE_123',
            user=self.user)

    def tearDown(self) -> None:
        self.order.delete()

    def test_order_detail_view(self):
        response = self.client.get(reverse(
            'shopapp:order_details',
            kwargs={'pk': self.order.pk})
        )
        self.assertContains(response, self.order.delivery_address)
        self.assertContains(response, self.order.promocode)


class OrdersExportViewTestCase(TestCase):
    fixtures = [
        'users-fixture.json',
        'products-fixture.json',
        'orders-fixture.json',
    ]

    @classmethod
    def setUpClass(cls):
        super(OrdersExportViewTestCase, cls).setUpClass()
        cls.user = User.objects.create(
            username='test-user',
            password='qwerty',
            is_staff=True,
        )

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_order_export(self):
        response = self.client.get(reverse('shopapp:order-export'))
        self.assertEquals(response.status_code, 200)

        orders = Order.objects.order_by('pk').all()

        expected_data = [
            {
                "pk": order.pk,
                "delivery_address": order.delivery_address,
                "promocode": order.promocode,
                "user": order.user.id,
                "products": [
                    [
                        product.id,
                        product.name
                    ]
                    for product in order.products.all()
                ],
            }
            for order in orders
        ]

        order_data = response.json()

        self.assertEqual(order_data['orders'], expected_data)
