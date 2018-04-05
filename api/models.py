from django.db import models


class Name(models.Model):
    name = models.CharField(max_length=45)
    tmdb_id = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Keyword(models.Model):
    keyword = models.CharField(max_length=45)

    def __str__(self):
        return self.keyword

class Tag(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
