from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework import generics
from rest_framework import mixins


class ArticleList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

	def get(self, request):
		return self.list(request)
		
	def post(self, request):
		return self.create(request)
	

	

class ArticleDetails(APIView):
	def get_object(self, pk):
		try:
			return Article.objects.get(pk=pk)
		
		except Article.DoesNotExist:
			return Response(staus=status.HTTP_400_BAD_REQUEST)

	def get(self, request, pk):
		articles = self.get_object(pk=pk)
		serializer = ArticleSerializer(articles)
		return Response (serializer.data)

	def put(self, request, pk):
		article = self.get_object(pk=pk)
		serializer = ArticleSerializer(article, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		article = self.get_object(pk=pk)
		article.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)




# Create your views here.
# @api_view(['GET', 'POST'])
# def article_list(request):
# 	if request.method == 'GET':
# 		articles = Article.objects.all()
# 		serializer = ArticleSerializer(articles, many = True)
# 		return Response (serializer.data)

# 	elif request.method == 'POST':
# 		serializer = ArticleSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status = status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	
# @api_view(['GET', 'PUT', 'DELETE'])
# def article_details(request, pk):
# 	try:
# 		article = Article.objects.get(pk=pk)
	
# 	except Article.DoesNotExist:
# 		return Response(staus=status.HTTP_400_BAD_REQUEST)

# 	if request.method == 'GET':
# 		serializer = ArticleSerializer(article)
# 		return Response(serializer.data)

# 	elif request.method == 'PUT':
# 		serializer = ArticleSerializer(article, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# 	elif request.method == 'DELETE':
# 		article.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)



