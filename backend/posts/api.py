from django.shortcuts import render
from django.http import JsonResponse
from .serializers import PostSerializer
from .models import Posts
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import PostForm


# Create your views here.

@api_view(['GET'])
def post_list(request):
    posts = Posts.objects.all()

    serializer = PostSerializer(posts, many=True)

    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def create_post(request):
    form = PostForm(request.data)

    if form.is_valid():
        post = form.save(commit=False)
        post.owner = request.user
        post.save()

        serializer = PostSerializer(post)

        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'add smothing to the error message'})