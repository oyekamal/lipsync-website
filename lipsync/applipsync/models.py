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
    
    # def __str__(self):
    #     return self.json.name