import os
import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from slugify import slugify
from hogwarts.models import House

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def home(request):
    return render(request, 'hogwarts/home.html')

def houses(request):
    # Fetch all houses from the database
    houses = House.objects.all()
    return render(request, 'hogwarts/houses.html', {'houses': houses})

def characters(request):
    search_query = request.GET.get('search', '')
    house_filter = request.GET.get('house', '')
    page_number = request.GET.get('page')

    # Fetch character data from external API
    response = requests.get('https://hp-api.onrender.com/api/characters')
    data = response.json()

    # Apply search and house filters
    if search_query:
        data = [char for char in data if search_query.lower() in char['name'].lower()]
    if house_filter:
        data = [char for char in data if char.get('house') == house_filter]

    # Paginate character list (12 per page)
    paginator = Paginator(data, 12)
    page_obj = paginator.get_page(page_number)

    return render(request, 'hogwarts/characters.html', {
        'page_obj': page_obj,
        'search_query': search_query,
        'selected_house': house_filter
    })

def character_detail(request, slug):
    # Fetch character details from external API
    response = requests.get('https://hp-api.onrender.com/api/characters')
    data = response.json()

    # Find the character by slugified name
    character = next(
        (char for char in data if slugify(char['name']) == slug), None
    )

    if not character:
        return render(request, 'hogwarts/character_not_found.html', {'name': slug})

    return render(request, 'hogwarts/character_detail.html', {'character': character})

def favorites(request):
    return render(request, 'hogwarts/favorites.html')

def chat_with_character(request, name):
    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        prompt = f"Imagine you are {name} from Harry Potter. Respond to this message: {user_message}"

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mistralai/mistral-7b-instruct",  
                "messages": [{"role": "user", "content": prompt}]
            }
        )

        try:
            result = response.json()
            print("OpenRouter raw:", result)
            ai_reply = result['choices'][0]['message']['content']
        except Exception as e:
            print("OpenRouter error:", e)
            ai_reply = "Sorry, I couldn't generate a response right now."

        return JsonResponse({'reply': ai_reply})

    return render(request, 'hogwarts/chat.html', {'name': name})

def quiz(request):
    # Fetch 5 easy quiz questions from external API
    url = "https://opentdb.com/api.php?amount=5&category=11&difficulty=easy&type=multiple"
    response = requests.get(url)
    questions = response.json()['results']

    if request.method == 'POST':
        answers = {
            'q1': request.POST.get('q1'),
            'q2': request.POST.get('q2'),
            'q3': request.POST.get('q3'),
            'q4': request.POST.get('q4'),
            'q5': request.POST.get('q5'),
        }

        correct_answers = [q['correct_answer'] for q in questions]
        
        # Calculate score based on correct answers
        score = sum([1 for i, ans in answers.items() if ans == correct_answers[int(i[-1])-1]])

        return render(request, 'hogwarts/quiz_result.html', {'score': score})

    return render(request, 'hogwarts/quiz.html', {'questions': questions})
