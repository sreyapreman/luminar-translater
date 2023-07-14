import tempfile
import magic
import PyPDF2
from PyPDF2 import PdfReader
import docx2txt
import subprocess
import os

from django.shortcuts import render

from Translatorapi.models import Video
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Translatorapi.serializers import VideoSerializer, AudioSerializer, PdfSerializer,LinkSerializer

from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from django.conf import settings








from django.http import HttpResponse
import datetime
import uuid

class SaveVideoView(APIView):
    def post(self, request, format=None):
        name = request.data.get("name")
        video_file = request.FILES.get("video_file")
        video_data = {"name": name, "video_file": video_file}
        serializer = VideoSerializer(data=video_data)

        if serializer.is_valid():
            saved_video = serializer.save()
            video_path = saved_video.video_file.path

            # Convert video to audio
            video_clip = VideoFileClip(video_path)
            audio = video_clip.audio

            # Generate a unique file name with timestamp and UUID
            timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            unique_id = str(uuid.uuid4())[:8]
            file_name = f"extractedaudio_{timestamp}_{unique_id}.mp3"

            # Define the target audio file path within the 'audio' folder
            target_folder = os.path.join(settings.BASE_DIR, 'audio')
            target_file = os.path.join(target_folder, file_name)

            # Save audio to the target file path
            audio.write_audiofile(target_file)

            # Return success response
            return HttpResponse(f"Audio saved in {target_file}")

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    


class SaveAudioView(APIView):
    def post(self, request, format=None):
        name = request.data.get("name")
        audio_data = {"name": name, "file": request.FILES.get("file")}
        serializer = AudioSerializer(data=audio_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class ConvertFileView(APIView):
    def post(self, request, format=None):
        file_data = request.FILES.get("file")
        
        # Save the uploaded file temporarily
        with tempfile.NamedTemporaryFile(suffix='.' + file_data.name.split('.')[-1], delete=False) as temp_file:
            temp_file.write(file_data.read())
            temp_file_path = temp_file.name
        
        # Convert the file to text
        text_content = self.convert_to_text(temp_file_path)
        
        # Remove the temporary file
        os.remove(temp_file_path)
        
        if text_content:
            return Response({'text_content': text_content})
        
        return Response({'error': 'Unsupported file format'}, status=status.HTTP_400_BAD_REQUEST)

    def convert_to_text(self, file_path):
        file_type = magic.from_file(file_path, mime=True)
        
        if 'application/pdf' in file_type:
            return self.convert_pdf_to_text(file_path)
        elif 'application/msword' in file_type or 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' in file_type:
            return self.convert_doc_to_text(file_path)
        elif 'text/plain' in file_type:
            return self.read_text_file(file_path)
        else:
            return None

    def convert_pdf_to_text(self, pdf_path):
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            text_content = [page.extract_text() for page in pdf_reader.pages]
            text_content = '\n'.join(text_content)

            print(text_content)

        return text_content

    def convert_doc_to_text(self, doc_path):
        text_content = docx2txt.process(doc_path)

        return text_content

    def read_text_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as text_file:
            text_content = text_file.read()

        return text_content

     
class SaveLinkView(APIView):
    def post(self, request, format=None):
        name = request.data.get("name")
        url_data = {"name": name, "url": request.data.get("url")}
        serializer = LinkSerializer(data=url_data)
        
        if serializer.is_valid():
            serializer.save()
            print(url_data)
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




        