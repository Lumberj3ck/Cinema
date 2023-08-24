from django.test import TestCase
from django.urls import reverse
from .settings_test import Settings



class Film_collection_url(Settings):
    def setUp(self):
        self.url = reverse('premiere')

    def test_is_right_url(self):
        self.assertEqual(self.url, '/', msg='Should be just home url')
    
    def test_url_is_responding_right(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.resolver_match.view_name, 'premiere')

    def test_url_name(self):
        response = self.client.get(self.url)
        self.assertEqual(response.resolver_match.url_name, 'premiere')

    def test_db_collection(self):
        response = self.client.get(self.url)

    def test_view_logic(self):
        bad_response = self.client.get('premiere/sort-by=1')
        self.assertEqual(bad_response.status_code, 404)
        right_response = self.client.get('?sort-by=name')
        self.assertEqual(right_response.status_code, 200)
        self.assertQuerysetEqual(right_response.context['page_obj'], self.premiere_collection.films.order_by('name'))
    
    def test_genres_in_view(self):
        genre = 1
        response = self.client.get(f'?sort-by=name&genre={genre}')
        self.assertQuerysetEqual(response.context['page_obj'], self.premiere_collection.films.order_by('name').filter(genres=genre))
        response = self.client.get(f'?genre={genre}&page=2')
        self.assertEqual(response.status_code, 200)
    

        



        
