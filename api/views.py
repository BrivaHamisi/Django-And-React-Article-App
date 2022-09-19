from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.
def article_list(request):
	if request.method == 'GET':
		articles = Article.objects.all()
		serializer = ArticleSerializer(articles, many = True)
		return JsonResponse(serializer.data, safe = False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ComplaintsFormSerializer(data=data)
		if serializer.is_valid():
			serializer.save
			return JsonResponse(serializer.data, status = 201)
		return JsonResponse(serializer.errors, status = 400)

