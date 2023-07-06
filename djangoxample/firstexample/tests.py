from django.test import TestCase

# Create your tests here.
class AllTasksViewTest(TestCase):
    def setUp(self):
        pass

    def test_no_item(self):
        response = self.client.get('/firstexample/item/10/')
        expected_content = "<H1>Товар не найден</H1>"
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, expected_content)

    def test_one_item(self):
        response = self.client.get('/firstexample/item/1/')
        expected_content1 = "<H1>Карточка товара</h1>"
        expected_content2 = "Кроссовки abibas"
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, expected_content1)
        self.assertContains(response, expected_content2)

    def test_all_items(self):
        response = self.client.get('/firstexample/items/')
        expected_content = "<H1>Список товара</H1>"
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, expected_content)
