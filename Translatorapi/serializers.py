from rest_framework import serializers
from Translatorapi.models import Video,Audio,PDF,Link,TranslatedAudio,TranslatedVideo,TranslatedPDF,TransaltedLink

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Audio
        fields="__all__"

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields="__all__"

class PdfSerializer(serializers.ModelSerializer):
    class Meta:
        model=PDF
        fields="__all__"

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Link
        fields="__all__"        

class TranslatorAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model=TranslatedAudio
        fields="__all__"    

class TranslatorVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=TranslatedVideo
        fields="__all__"       

class TranslatorPdfSerializer(serializers.ModelSerializer):
    class Meta:
        model=TranslatedPDF
        fields="__all__"


class TranslatorlinkSerializer(serializers.ModelSerializer):
    class Meta:
        model=TransaltedLink
        fields="__all__"        