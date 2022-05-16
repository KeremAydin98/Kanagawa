from django.db import models
import uuid
from django.urls import reverse
from django.contrib.auth import get_user_model
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors


class Book(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    title = models.CharField(max_length=500)

    author = models.CharField(max_length=200)

    price = models.DecimalField(max_digits=6, decimal_places=2)

    cover = models.ImageField(upload_to='covers/', blank=True, null=True)

    class Meta:

        permissions = [('special_status', 'Can read all books')]

    def __str__(self):

        return self.title

    def get_absolute_url(self):

        return reverse('book_detail', args=[str(self.id)])


class Comment(models.Model):

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    comment = models.CharField(max_length=200)

    def __str__(self):

        return self.comment


class Recommends(models.Model):

    df = pd.read_csv("df.csv")

    df_pivot = df.pivot(index='title', columns='user', values='rating').fillna(0)
    df_matrix = csr_matrix(df_pivot.values)

    model_knn = NearestNeighbors(metric='cosine', algorithm='brute')
    model_knn.fit(df_matrix)

    def get_recommends(self,book,df_pivot=df_pivot, model_knn=model_knn):
        index = df_pivot.transpose().columns.get_loc(book)
        distances, indices = model_knn.kneighbors(df_pivot.iloc[index, :].values.reshape(1, -1), n_neighbors=6)

        self.recommended_books = []

        for i in range(len(distances.flatten())):
            self.recommended_books.append(df_pivot.index[indices.flatten()[i]])

        return self.recommended_books

    title = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='recommends'
    )

    def __str__(self):

        return self.recommended








