# pylint: disable=missing-class-docstring
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from jsonfield import JSONField

# Create your models here.


class Mouth(models.Model):
    title = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    a_e_h = models.FileField(
        blank=False,
        null=False,
        upload_to="images/test_normal/",
        validators=[FileExtensionValidator(["png"])],
    )
    d_j_ch_h = models.FileField(
        blank=False,
        null=False,
        upload_to="images/test_normal/",
        validators=[FileExtensionValidator(["png"])],
    )
    f_h = models.FileField(
        blank=False,
        null=False,
        upload_to="images/test_normal/",
        validators=[FileExtensionValidator(["png"])],
    )
    l_h = models.FileField(
        blank=False,
        null=False,
        upload_to="images/test_normal/",
        validators=[FileExtensionValidator(["png"])],
    )
    m_b_close_h = models.FileField(
        blank=False,
        null=False,
        upload_to="images/test_normal/",
        validators=[FileExtensionValidator(["png"])],
    )
    o_big_h = models.FileField(
        blank=False,
        null=False,
        upload_to="images/test_normal/",
        validators=[FileExtensionValidator(["png"])],
    )
    o_small_h = models.FileField(
        blank=False,
        null=False,
        upload_to="images/test_normal/",
        validators=[FileExtensionValidator(["png"])],
    )
    oh_h = models.FileField(
        blank=False,
        null=False,
        upload_to="images/test_normal/",
        validators=[FileExtensionValidator(["png"])],
    )
    th_h = models.FileField(
        blank=False,
        null=False,
        upload_to="images/test_normal/",
        validators=[FileExtensionValidator(["png"])],
    )
    trans_h = models.FileField(
        blank=False,
        null=False,
        upload_to="images/test_normal/",
        validators=[FileExtensionValidator(["png"])],
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("store:mouth_details", args=[self.title])
        
class File(models.Model):
    audio = models.FileField(
        blank=False,
        null=False,
        upload_to="audio/",
        validators=[FileExtensionValidator(["mp3", "wav"])],
    )
    script = models.FileField(
        blank=False,
        null=False,
        upload_to="script/",
        validators=[FileExtensionValidator(["txt"])],
    )
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=100, null=True, blank=True)
    mouth = models.ForeignKey(Mouth, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name + " : " + self.mouth.title

    def get_absolute_url(self):
        return reverse("store:video_details", args=[self.slug])


class GentleJson(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE, null=True)
    # the_json = jsonfield.JSONField()
    json = JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name


class VideoFrame(models.Model):
    gentle_josn = models.ForeignKey(GentleJson, on_delete=models.CASCADE, null=True)
    video_frame = JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    video_frame_keys = JSONField(null=True)

    def __str__(self):
        return self.gentle_josn.file.name


class Video(models.Model):
    video_frame = models.ForeignKey(VideoFrame, on_delete=models.CASCADE)
    video = models.FileField(blank=False, null=False, upload_to="video/")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.video_frame.gentle_josn.file.name


class Question(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to="images/blog_images/")
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    
    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("store:blog_details", args=[self.slug])
