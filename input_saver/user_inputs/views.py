from django.shortcuts import render, redirect, get_object_or_404
from .forms import RatingForm
from .models import QA, Rating, Questions
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.conf import settings
import json
import os



def home(request):
    return render(request, "user_inputs/index.html")  # 指向你的模板


def game(request):
    return render(request, "user_inputs/game.html")  # 指向你的模板


def index_json(request):
    json_path = os.path.join(settings.BASE_DIR, 'puzzles', 'puzzles.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return JsonResponse(data, safe=False)


def puzzles(request):
    file_name = request.GET.get('name', '')
    json_path = os.path.join(settings.BASE_DIR, 'puzzles', file_name)
    with open(json_path, 'r', encoding='utf-8') as f:
        data = f.read()
    return HttpResponse(data, content_type='text/plain')


def save(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title=data.get('name')[:-3]
            save_data = QA(question=Questions.objects.get(title=title), query=data.get('question'), answer=data.get('answer'))
            save_data.save()
            return JsonResponse({
                'status': 'success',
                'message': 'JSON saved successfully',
                'id': save_data.id
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)

    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method'
    }, status=405)

def rate_item(request):
    title=request.GET.get('name', '')[:-3]
    print(request.GET.get('name', ''))
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            # 创建新评分记录（无需用户）
            rating = Rating.objects.create(
                question=Questions.objects.get(title=title),
                score=form.cleaned_data['score']
            )
            # 计算新的平均评分
            print(11111)
            return JsonResponse({
                'status': 'success',
            })
        return JsonResponse({'status': 'error', 'errors': form.errors})