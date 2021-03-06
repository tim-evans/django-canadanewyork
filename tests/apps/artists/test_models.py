from django.test import TestCase

from .factories import ArtistFactory
from ..exhibitions.factories import ExhibitionFactory
from ..press.factories import PressFactory


class ArtistVisibleTest(TestCase):
    def setUp(self):
        self.in_gallery = ArtistFactory.FACTORY_FOR.in_gallery

    def test_in_gallery(self):
        ArtistFactory.create(visible=True)

        self.assertTrue(self.in_gallery.exists())

    def test_not_in_gallery(self):
        ArtistFactory.create(visible=False)

        self.assertFalse(self.in_gallery.exists())


class ArtistAllPressTest(TestCase):
    def setUp(self):
        self.ArtistPress = PressFactory.create(title='artist_press')
        self.ExhibitionPress = PressFactory.create(title='exhibition_press')

        self.Artist = ArtistFactory.create()
        self.Exhibition = ExhibitionFactory.create()
        self.Exhibition.artists.add(self.Artist)

    def test_no_press(self):
        self.assertFalse(self.Artist.all_press.exists())

    def test_with_artist(self):
        self.ArtistPress.artist = self.Artist
        self.ArtistPress.save()
        self.assertEqual(self.Artist.all_press[0], self.ArtistPress)
        self.assertEqual(len(self.Artist.all_press), 1)

    def test_with_exhibition_with_artist(self):
        self.ExhibitionPress.exhibition = self.Exhibition
        self.ExhibitionPress.save()

        self.assertEqual(self.Artist.all_press[0], self.ExhibitionPress)
        self.assertEqual(len(self.Artist.all_press), 1)

    def test_with_artist_and_exhibition_with_artist(self):
        self.ExhibitionPress.exhibition = self.Exhibition
        self.ExhibitionPress.save()
        self.ArtistPress.artist = self.Artist
        self.ArtistPress.save()

        self.assertIn(self.ExhibitionPress, self.Artist.all_press)
        self.assertIn(self.ArtistPress, self.Artist.all_press)
        self.assertEqual(self.Artist.all_press.count(), 2)
