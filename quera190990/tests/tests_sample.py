from django.test import TestCase

from store import queries


class TestTasks(TestCase):
    fixtures = ('store',)

    def test_sum_of_income(self):
        solution = 61160
        answer = queries.sum_of_income("2023-07-01", "2023-07-30")
        self.assertEqual(solution, answer)

    def test_young_employees(self):
        self.assertEqual(len(queries.young_employees('Custodian')), 1)
        self.assertEqual(len(queries.young_employees('Cashier')), 2)
        self.assertEqual(len(queries.young_employees('Manager')), 0)

    def test_cheap_products(self):
        pass

    def test_products_sold_by_companies(self):
        self.assertEqual(
            set(queries.products_sold_by_companies()),
            {('Alis', 198), ('Dina', 487), ('Minoo', 553)}
        )
