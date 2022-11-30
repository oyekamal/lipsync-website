from django.db import models
from jsonfield import JSONField

# Create your models here.


class File(models.Model):
    audio = models.FileField(blank=False, null=False, upload_to='audio/')
    script = models.FileField(blank=False, null=False, upload_to='script/')
    remark = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.remark

class GentleJson(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE,null=True)
    # the_json = jsonfield.JSONField()   
    json = JSONField(null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.file.remark

class VideoFrame(models.Model):
    gentle_josn = models.ForeignKey(GentleJson, on_delete=models.CASCADE, null=True)
    video_frame = JSONField(null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    video_frame_keys = JSONField(null=True) 

    def __str__(self):
        return self.gentle_josn.file.remark

class Video(models.Model):
    video_frame = models.ForeignKey(VideoFrame, on_delete=models.CASCADE)
    video = models.FileField(blank=False, null=False, upload_to='video/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.video_frame.gentle_josn.file.remark