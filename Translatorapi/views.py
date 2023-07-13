import tempfile
import magic
import PyPDF2
import docx2txt

from django.shortcuts import render

from .models import Video
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VideoSerializer, AudioSerializer, PdfSerializer,LinkSerializer

class SaveVideoView(APIView):
    def post(self, request, format=None):
        name = request.data.get("name")
        video_data = {"name": name, "video_file": request.FILES.get("video_file")}
        serializer = VideoSerializer(data=video_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
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





class SavePdfView(APIView):
    def post(self, request, format=None):
        name = request.data.get("name")
        pdf_file = request.FILES.get("file")
        pdf_data = {"name": name, "file": pdf_file}
        serializer = PdfSerializer(data=pdf_data)
        
        if serializer.is_valid():
            serializer.save()
            
            # Convert the uploaded PDF file to text
            self.convert_to_text(pdf_file)
            
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def convert_to_text(self, pdf_file):
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as temp_pdf:
            temp_pdf.write(pdf_file.read())
            temp_pdf_path = temp_pdf.name

        file_type = magic.from_file(temp_pdf_path, mime=True)
        
        if file_type == 'application/pdf':
            self.convert_pdf_to_text(temp_pdf_path)
        elif file_type == 'application/msword':
            self.convert_doc_to_text(temp_pdf_path)
        else:
            print("Unsupported file format:", file_type)

    def convert_pdf_to_text(self, pdf_path):
        text_path = pdf_path[:-4] + '.txt'

        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            text_content = []

            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                text_content.append(page.extract_text())

            with open(text_path, 'w', encoding='utf-8') as text_file:
                text_file.write('\n'.join(text_content))

        print("PDF converted to text successfully.")

    def convert_doc_to_text(self, doc_path):
        text_path = doc_path[:-4] + '.txt'
        text_content = docx2txt.process(doc_path)

        with open(text_path, 'w', encoding='utf-8') as text_file:
            text_file.write(text_content)

        print("DOC converted to text successfully.")



     
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




        