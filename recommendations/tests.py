from django.test import TestCase

from products.models import Products
from boxes.models import Box
from orders.models import Order, OrderItem

from recommendations.services import (
    recommend_box,
    get_orientations,
    has_overlap,
)


class BoxRecommendationTests(TestCase):

    def setUp(self):

        # Create a sample product
        self.product = Products.objects.create(
            name="Laptop",
            length="30.00",
            width="20.00",
            height="5.00",
            weight="2.000"
        )

        # Create three shipping boxes
        self.small_box = Box.objects.create(
            name="Small Box",
            length="35.00",
            width="25.00",
            height="10.00",
            max_weight="3.000",
            cost="30.00"
        )

        self.medium_box = Box.objects.create(
            name="Medium Box",
            length="40.00",
            width="30.00",
            height="15.00",
            max_weight="10.000",
            cost="45.00"
        )

        self.large_box = Box.objects.create(
            name="Large Box",
            length="50.00",
            width="40.00",
            height="30.00",
            max_weight="20.000",
            cost="70.00"
        )

        # Create a sample order
        self.order = Order.objects.create(
            order_number="TEST-1001"
        )

        OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1
        )

    # TEST 1: Cheapest suitable box
    def test_cheapest_box_recommendation(self):

        result = recommend_box(self.order)

        self.assertEqual(
            result["recommended"]["box"].pk,
            self.small_box.pk
        )

        from decimal import Decimal

        self.assertEqual(
        result["total_weight"],
        Decimal("2.000")
        )

    # TEST 2: Weight capacity restriction
    def test_weight_capacity_restriction(self):

        heavy_product = Products.objects.create(
            name="Heavy Product",
            length="10.00",
            width="10.00",
            height="10.00",
            weight="4.000"
        )

        heavy_order = Order.objects.create(
            order_number="TEST-1002"
        )

        OrderItem.objects.create(
            order=heavy_order,
            product=heavy_product,
            quantity=1
        )

        result = recommend_box(heavy_order)

        self.assertEqual(
            result["recommended"]["box"].pk,
            self.medium_box.pk
        )

        self.assertFalse(result["all_results"][0]["feasible"])

    # TEST 3: Oversized product rejection
    def test_oversized_product_rejected(self):

        oversized_product = Products.objects.create(
            name="Oversized Product",
            length="100.00",
            width="100.00",
            height="100.00",
            weight="1.000"
        )

        oversized_order = Order.objects.create(
            order_number="TEST-1003"
        )

        OrderItem.objects.create(
            order=oversized_order,
            product=oversized_product,
            quantity=1
        )

        result = recommend_box(oversized_order)

        self.assertIsNone(
            result["recommended"]
        )

    # TEST 4: Empty order handling
    def test_empty_order(self):

        empty_order = Order.objects.create(
            order_number="TEST-1004"
        )

        with self.assertRaises(ValueError):
            recommend_box(empty_order)

    # TEST 5: Product rotation
    def test_product_rotation(self):

        orientations = get_orientations(
            (30, 20, 5)
        )

        self.assertEqual(
            len(orientations),
            6
        )

    # TEST 6: Overlapping products
    def test_product_overlap(self):

        item1 = (0, 0, 0, 10, 10, 10)

        item2 = (5, 5, 5, 10, 10, 10)

        self.assertTrue(
            has_overlap(item1, item2)
        )

    # TEST 7: Non-overlapping products
    def test_products_do_not_overlap(self):

        item1 = (0, 0, 0, 10, 10, 10)

        item2 = (10, 0, 0, 10, 10, 10)

        self.assertFalse(
            has_overlap(item1, item2)
        )