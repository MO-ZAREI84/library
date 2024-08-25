from django.db import models
class BookManager(models.Manager):
    def archived_exluded_queryset(self):
        return self.filter(archived=False)
class Author (models.Model):
    name=models.CharField(max_length=10)

class Book(models.Model):
    title=models.CharField(max_length=20)
    authors=models.ManyToManyField(Author)
    archived = models.BooleanField(default=False)
    objects = BookManager()
# برای وارد کردن دیتا many to many
# >>> Author5=Author.objects.create(name='mostafa')
# >>> book.authors.add(Author5)
# >>> books=Book.objects.all()
# >>> for book in books:
# ...     author_names=book.authors.values_list('name',flat=True)
# ...     print(f"book:{book.title} authors={author_names}")
# ...
# book:saa authors=<QuerySet []>
# book:My First Book authors=<QuerySet ['Author1', 'Author2']>
# book:pirmard va darya authors=<QuerySet ['tolsoi']>
# book:1984 authors=<QuerySet ['jorj']>
# book:sahab authors=<QuerySet ['mostafa']>
    
class Profile(models.Model):
    email=models.EmailField(default='default@example.com')
    phone_number=models.IntegerField()

class Person(models.Model):
    profile=models.OneToOneField(Profile,on_delete=models.CASCADE)
