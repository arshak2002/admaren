from rest_framework import generics, permissions
from .models import Snippet, Tag
from .serializers import SnippetSerializer, TagSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class SnippetListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            tag_title = request.data.get('tag', {}).get('title')
            if tag_title:
                tag, _ = Tag.objects.get_or_create(title=tag_title)
                serializer.validated_data['tag'] = tag
            serializer.validated_data['user'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
class SnippetRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticated]


class TagListAPIView(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)


class TagRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
