from django.test import TestCase
from django.urls import reverse
from .models import Recipe


class RecipeTestCase(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            description='This is a test recipe',
            instructions='Test instructions',
            ingredients='Test ingredients'
        )

    def test_recipe_detail_view(self):
        url = reverse('recipe:recipe_detail', args=[self.recipe.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipe.title)
        self.assertContains(response, self.recipe.description)
        self.assertContains(response, self.recipe.instructions)
        self.assertContains(response, self.recipe.ingredients)

    def test_main_view(self):
        url = reverse('recipe:main')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['recipes'], [repr(self.recipe)])
