from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import InvitationSerializer, UserSerializer
from .models import Invitation, User
from .paginations import SmallSetPagination, MediumSetPagination
# Create your views here.


# @api_view(['GET', 'PUT'])
# def user_list(['GET', 'PUT']):
#     """"""
# @api_view(['GET', 'PUT'])
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = MediumSetPagination


class InvitationListCreate(generics.ListCreateAPIView):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    pagination_class = MediumSetPagination


class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = SmallSetPagination
