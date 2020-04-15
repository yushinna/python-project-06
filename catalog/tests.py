from django.urls import reverse
from django.test import TestCase

from .models import Mineral


class ViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.get(pk=1)

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'index.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'detail.html')
        self.assertEqual(resp.context['mineral'], self.mineral)

    def test_random_mineral_view(self):
        resp = self.client.get(reverse('random'))
        self.assertEqual(resp.status_code, 302)
