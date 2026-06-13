from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema, OpenApiResponse
from .serializers import UserSerializer, NoteSerializer
from .models import Note


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(responses=UserSerializer)
    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name
        }, status=status.HTTP_200_OK)

    @extend_schema(request=UserSerializer, responses=UserSerializer)
    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(responses=NoteSerializer(many=True))
    def get(self, request):
        notes = Note.objects.filter(user=request.user)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=NoteSerializer, responses=NoteSerializer)
    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Note.objects.get(pk=pk, user=user)
        except Note.DoesNotExist:
            return None

    @extend_schema(responses=NoteSerializer)
    def get(self, request, pk):
        note = self.get_object(pk, request.user)
        if not note:
            return Response({'error': 'Nota não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        return Response(NoteSerializer(note).data)

    @extend_schema(request=NoteSerializer, responses=NoteSerializer)
    def put(self, request, pk):
        note = self.get_object(pk, request.user)
        if not note:
            return Response({'error': 'Nota não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(request=NoteSerializer, responses=NoteSerializer)
    def patch(self, request, pk):
        note = self.get_object(pk, request.user)
        if not note:
            return Response({'error': 'Nota não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(responses=OpenApiResponse(description='Nota deletada com sucesso'))
    def delete(self, request, pk):
        note = self.get_object(pk, request.user)
        if not note:
            return Response({'error': 'Nota não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        note.delete()
        return Response({'message': 'Nota deletada com sucesso'}, status=status.HTTP_204_NO_CONTENT)
