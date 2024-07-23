import uuid
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse


def thumbnail_upload_to(self, filename):
    return f"thumbnails/{self.cid}/{filename}"


def chapter_video_upload_to(instance, filename):
    return f"courses/{instance.section.course.cid}/videos/{filename}"


class Category(models.Model):
    name = models.CharField(verbose_name="name of the category", max_length=100)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_name": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"


class Subcategory(models.Model):
    name = models.CharField(verbose_name="name of the subcategory", max_length=150)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name="subcategories", null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Subcategories"


class Course(models.Model):
    cid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name="Title of the course", max_length=500)
    subtitle = models.CharField(verbose_name="Subtitle of the course", max_length=1000)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name="courses", null=True
    )
    language = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    thumbnail = models.ImageField(upload_to=thumbnail_upload_to, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Courses"


class Section(models.Model):
    sequence = models.IntegerField(verbose_name="the section number or sequence number")
    title = models.CharField(max_length=150)
    tot_time = models.IntegerField(
        verbose_name="total time taken to complete the section", default=0
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="sections"
    )
    description = models.CharField(max_length=100)

    def calc_time(self):
        time = 0
        chapters = self.chapters.all()
        for chapter in chapters:
            time += chapter.time if chapter.time else 0
        return time

    def save(self, *args, **kwargs):
        if self._state.adding:
            last_section = (
                Section.objects.filter(course=self.course).order_by("sequence").last()
            )
            if last_section:
                self.sequence = last_section.sequence + 1
            else:
                self.sequence = 1

        super(Section, self).save(*args, **kwargs)
        self.tot_time = self.calc_time()
        super(Section, self).save(update_fields=["tot_time"])

    def time_taken(self):
        return f"{self.tot_time//60}hr {self.tot_time%60}min" if self.tot_time else "0s"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Sections"


class Chapter(models.Model):
    order = models.PositiveIntegerField(
        verbose_name="order number of the chapter in a lesson"
    )
    title = models.CharField(max_length=150)
    time = models.IntegerField(default=0)  # Set a default value to avoid None
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="chapters"
    )
    video = models.FileField(
        upload_to="chapter_video_upload_to", blank=True, null=True
    )
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Chapters"
