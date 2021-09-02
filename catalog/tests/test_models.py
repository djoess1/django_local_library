from django.test import TestCase

from catalog.models import Author,Book,BookInstance,Genre,Language

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_label, 'died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name},{author.first_name}'
        self.assertEqual(str(author), expected_object_name)

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), '/catalog/author/1')

    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label , 'last name')

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length        
        self.assertEqual(max_length, 100)

    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEqual(field_label, 'date of birth')




class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Book.objects.create(title='Big', summary='summary', isbn='1234')

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_summary_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('summary').verbose_name
        self.assertEqual(field_label, 'summary')

    def test_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_summary_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('summary').max_length
        self.assertEqual(max_length, 1000)

    def test_isbn_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('isbn').verbose_name
        self.assertEqual(field_label, 'ISBN')

    def test_isbn_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('isbn').max_length
        self.assertEqual(max_length, 13)

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(book.get_absolute_url(), '/catalog/book/1')

    # def test_last_name_label(self):
    #     author = Author.objects.get(id=1)
    #     field_label = author._meta.get_field('last_name').verbose_name
    #     self.assertEqual(field_label , 'last name')

    # def test_last_name_max_length(self):
    #     author = Author.objects.get(id=1)
    #     max_length = author._meta.get_field('last_name').max_length        
    #     self.assertEqual(max_length, 100)

    # def test_date_of_birth_label(self):
    #     author = Author.objects.get(id=1)
    #     field_label = author._meta.get_field('date_of_birth').verbose_name
    #     self.assertEqual(field_label, 'date of birth')