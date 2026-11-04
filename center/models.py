from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField("სათაური", max_length=180)
    summary = models.CharField("მოკლე აღწერა", max_length=280)
    body = models.TextField("სრული ტექსტი")
    image_url = models.URLField("ფოტოს ბმული", blank=True)
    published_at = models.DateTimeField("გამოქვეყნების თარიღი", default=timezone.now)
    is_published = models.BooleanField("გამოქვეყნებულია", default=False)

    class Meta:
        ordering = ["-published_at"]
        verbose_name = "სიახლე"
        verbose_name_plural = "სიახლეები"

    def __str__(self):
        return self.title

class Event(models.Model):
    STATUS_CHOICES = [
        ("planned", "დაგეგმილი"),
        ("cancelled", "გაუქმებული"),
        ("completed", "დასრულებული"),
    ]
    title = models.CharField("სათაური", max_length=180)
    summary = models.CharField("მოკლე აღწერა", max_length=280)
    description = models.TextField("აღწერა")
    starts_at = models.DateTimeField("დაწყების თარიღი და დრო")
    location = models.CharField("ადგილმდებარეობა", max_length=180)
    image_url = models.URLField("ფოტოს ბმული", blank=True)
    registration_url = models.URLField("რეგისტრაციის ბმული", blank=True)
    status = models.CharField("სტატუსი", max_length=20, choices=STATUS_CHOICES, default="planned")

    class Meta:
        ordering = ["starts_at"]
        verbose_name = "ღონისძიება"
        verbose_name_plural = "ღონისძიებები"

    def __str__(self):
        return self.title

class Opportunity(models.Model):
    title = models.CharField("სათაური", max_length=180)
    category = models.CharField("კატეგორია", max_length=80)
    description = models.TextField("აღწერა")
    deadline = models.DateField("განაცხადის ბოლო ვადა", blank=True, null=True)
    application_url = models.URLField("განაცხადის ბმული", blank=True)
    is_published = models.BooleanField("გამოქვეყნებულია", default=False)

    class Meta:
        ordering = ["deadline", "title"]
        verbose_name = "შესაძლებლობა"
        verbose_name_plural = "შესაძლებლობები"

    def __str__(self):
        return self.title

class Project(models.Model):
    STATUS_CHOICES = [
        ("ongoing", "მიმდინარე"),
        ("completed", "დასრულებული"),
        ("planned", "დაგეგმილი"),
    ]
    title = models.CharField("სათაური", max_length=180)
    summary = models.CharField("მოკლე აღწერა", max_length=280)
    description = models.TextField("აღწერა")
    image_url = models.URLField("ფოტოს ბმული", blank=True)
    status = models.CharField("სტატუსი", max_length=20, choices=STATUS_CHOICES, default="ongoing")
    is_published = models.BooleanField("გამოქვეყნებულია", default=False)

    class Meta:
        ordering = ["title"]
        verbose_name = "პროექტი"
        verbose_name_plural = "პროექტები"

    def __str__(self):
        return self.title
