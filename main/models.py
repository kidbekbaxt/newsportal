from django.db import models
from django.utils.translation import get_language


class Category(models.Model):
    name_uz = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    name_tr = models.CharField(max_length=50)



    @property
    def name(self):
        return getattr(self,f"name_{get_language()}")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    subject_uz = models.CharField(max_length=200)
    subject_en = models.CharField(max_length=200)
    subject_tr = models.CharField(max_length=200)
    content_uz = models.TextField()
    content_en = models.TextField()
    content_tr = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)



    @property
    def subject(self):
        return getattr(self,f"subject_{get_language()}")

    @property
    def content(self):
        return getattr(self, f"content_{get_language()}")


