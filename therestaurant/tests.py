from django.test import TestCase
from django.urls import reverse
from project_4.urls import urlpatterns
from therestaurant.models import *

# SET "TESTING = True" in settings.py when testing.


class ReservationQuerySetTests(TestCase):
    def setUp(self):
        self.table1 = Table.objects.create(table_number=1, table_covers=2)
        self.table2 = Table.objects.create(table_number=2, table_covers=2)

    def test_queryset_filtering(self):

        Reservation.objects.create(
            first_name='test1',
            last_name='test',
            time='17:00:00',
            contact_number='0000000000',
            date='2023-01-01',
            covers='2',
            table=self.table1
            )

        Reservation.objects.create(
            first_name='test2',
            last_name='test',
            time='18:00:00',
            contact_number='0000000000',
            date='2023-01-01',
            covers='2',
            table=self.table2
            )

        queryset = Reservation.objects.filter(table=self.table1)
        self.assertEqual(queryset.count(), 1)


class ReservationViewTests(TestCase):
    def setUp(self):
        self.table1 = Table.objects.create(table_number=1, table_covers=2)
        self.table2 = Table.objects.create(table_number=2, table_covers=2)
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_post_request(self):

        form_data = {
            'user': '',
            'first_name': 'test1',
            'last_name': 'test',
            'email': 'test@test.com',
            'date': '2023-11-15',
            'time': '18:00',
            'contact_number': '0000000000',
            'covers': '2',
        }

        self.client.login(username='testuser', password='testpassword')
        url = reverse('reservetable')
        expected_redirect_url = reverse('reserve_success')
        response = self.client.post(url, data=form_data)

        self.assertRedirects(response,  expected_url=expected_redirect_url)
        self.assertEqual(Reservation.objects.count(), 1)
