from django.urls import path
from rest_framework.routers import DefaultRouter
from Translatorapi.views import SaveVideoView,SaveAudioView,SaveLinkView,ConvertFileView

# router=DefaultRouter()

# router.register("upload",VideoView,basename="uplodvideo")

urlpatterns =[
    path('videoupload/',SaveVideoView.as_view(),name='video'),
    path('audioupload/',SaveAudioView.as_view(),name="audio"),
    path('pdfupload/',ConvertFileView.as_view(),name="pdf"),
    path('urlupload/',SaveLinkView.as_view(),name="link"),

]
