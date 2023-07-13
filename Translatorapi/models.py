from django.db import models

class Audio(models.Model):
    name=models.CharField(max_length=100)
    file=models.FileField(upload_to='audios/')
    language=models.CharField(max_length=50,null=True,blank=True)
    uploaded_at=models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name

class Video(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    video_file=models.FileField(upload_to='videos/')
    language=models.CharField(max_length=50,null=True,blank=True)
    uploaded_at=models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name

class PDF(models.Model):
    name=models.CharField(max_length=100)
    file=models.FileField(upload_to='pdfs/')
    language=models.CharField(max_length=50,null=True,blank=True)
    uploaded_at=models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name
    
class Link(models.Model):
    name=models.CharField(max_length=100)
    url=models.URLField(max_length=200)
    uploaded_at=models.DateTimeField(auto_now_add=True)

class TranslatedAudio(models.Model):
    audio=models.ForeignKey(Audio, on_delete=models.CASCADE)
    translated_file=models.FileField(upload_to='translated_audios/')
    translated_language=models.CharField(max_length=50)

    def _str_(self):
        return f"{self.audio.name} ({self.translated_language})"

class TranslatedVideo(models.Model):
    video=models.ForeignKey(Video, on_delete=models.CASCADE)
    translated_file=models.FileField(upload_to='translated_videos/')
    translated_language=models.CharField(max_length=50)

    def _str_(self):
        return f"{self.video.name} ({self.translated_language})"

class TranslatedPDF(models.Model):
    pdf=models.ForeignKey(PDF, on_delete=models.CASCADE)
    translated_file=models.FileField(upload_to='translated_pdfs/')
    translated_language=models.CharField(max_length=50)

    def _str_(self):
        return f"{self.pdf.name} ({self.translated_language})"
    
class TransaltedLink(models.Model):
    link=models.ForeignKey(Link,on_delete=models.CASCADE)
    translated_file=models.FileField(upload_to='translated_links/')
    translated_language=models.CharField(max_length=50)

    def _str_(self):
        return f"{self.link.name} ({self.translated_language})"
