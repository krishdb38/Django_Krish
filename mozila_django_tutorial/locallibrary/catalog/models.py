from django.db import models
from django.urls import reverse
import uuid


class Genre(models.Model):
    """
    Model representing a book genre.

    Args:
        models ([type]): [description]
    """
    name = models.CharField(max_length=200, help_text="Enter a book Genre")

    def __str__(self):
        "String for representinf the Model object"
        return self.name


class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)

    Args:
        models ([type]): [description]
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    subject = models.TextField(
        max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField("ISBN", max_length=13,
                            unique=True, help_text="13 character ")

    # ManyToMany Field used because genre can contain many books. Books can cover many genre
    # Genre class has already been defined so we can specify the object above
    genre = models.ManyToManyField(
        Genre, help_text="Select a genre for this book ")

    def __str__(self):
        "String for representing the Model object "
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", args=[self(self.id)])

    # https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models
    
    def display_genre(self):
        " Create a string for the Genre. This is required to display genre in Admin "
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    
    display_genre.short_description = "Genre" #


class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library )

    Args:
        models ([type]): [description]
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book ")
    book = models.ForeignKey("Book", on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateTimeField(null=True, blank=True)
    
    LOAN_STATUS = (
        ("m", "Maintenance"),
        ("o", "On Loan"),
        ('a', "Available"),
        ('r', "Reserved"),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default = "m", help_text = "Book availiability")
    
    class Meta:
        ordering = ["due_back"]
        
    def __str__(self):
        "String for representing the Model object "
        return f"{self.id} ({self.book.title})"
    

class Author(models.Model):
    """Model representing an author

    Args:
        models ([type]): [description]
    """
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    date_of_death = models.DateTimeField("Died", null=True, blank=True)
    
    class Meta:
        ordering = ["last_name", "first_name"]
        
    def get_absolute_url(self):
        "Returns the url to access a particular author instance "
        return reverse("author-detail", args = [self(self.id)])
    

    
    def __str__(self):
        """String for representing the Model object. 
        """
        return f'{self.last_name}, {self.first_name}'
