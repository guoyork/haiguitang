from django.shortcuts import render, redirect
from .forms import InputForm
from .models import UserInput, QA
from django.http import JsonResponse, HttpResponse
from django.conf import settings
import json
import os


def index(request):
    print(111)
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = InputForm()

    inputs = UserInput.objects.all().order_by('-created_at')
    return render(request, 'user_inputs/index2.html', {'form': form, 'inputs': inputs})


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
    print(1111)
    return HttpResponse(data, content_type='text/plain')


def save(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            save_data = QA(name=data.get('name'), question=data.get('question'), answer=data.get('answer'))
            save_data.save()
            # print(QA.objects.all())
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
