from django.db import models
from jsonfield import JSONField
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
# Create your models here.


class Mouth(models.Model):
    title = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    a_e_h = models.FileField(blank=False, null=False, upload_to='images/test_normal/',
                             validators=[FileExtensionValidator(['png'])])
    d_j_ch_h = models.FileField(
        blank=False, null=False, upload_to='images/test_normal/', validators=[FileExtensionValidator(['png'])])
    f_h = models.FileField(blank=False, null=False, upload_to='images/test_normal/',
                           validators=[FileExtensionValidator(['png'])])
    l_h = models.FileField(blank=False, null=False, upload_to='images/test_normal/',
                           validators=[FileExtensionValidator(['png'])])
    m_b_close_h = models.FileField(
        blank=False, null=False, upload_to='images/test_normal/', validators=[FileExtensionValidator(['png'])])
    o_big_h = models.FileField(
        blank=False, null=False, upload_to='images/test_normal/', validators=[FileExtensionValidator(['png'])])
    o_small_h = models.FileField(
        blank=False, null=False, upload_to='images/test_normal/', validators=[FileExtensionValidator(['png'])])
    oh_h = models.FileField(blank=False, null=False, upload_to='images/test_normal/',
                            validators=[FileExtensionValidator(['png'])])
    th_h = models.FileField(blank=False, null=False, upload_to='images/test_normal/',
                            validators=[FileExtensionValidator(['png'])])
    trans_h = models.FileField(
        blank=False, null=False, upload_to='images/test_normal/', validators=[FileExtensionValidator(['png'])])
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class File(models.Model):
    audio = models.FileField(blank=False, null=False, upload_to='audio/',
                             validators=[FileExtensionValidator(['mp3', 'wav'])])
    script = models.FileField(blank=False, null=False, upload_to='script/',
                              validators=[FileExtensionValidator(['txt'])])
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=100, null=True, blank=True)
    mouth = models.ForeignKey(Mouth, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

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
    gentle_josn = models.ForeignKey(
        GentleJson, on_delete=models.CASCADE, null=True)
    video_frame = JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    video_frame_keys = JSONField(null=True)

    def __str__(self):
        return self.gentle_josn.file.name


class Video(models.Model):
    video_frame = models.ForeignKey(VideoFrame, on_delete=models.CASCADE)
    video = models.FileField(blank=False, null=False, upload_to='video/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.video_frame.gentle_josn.file.name
