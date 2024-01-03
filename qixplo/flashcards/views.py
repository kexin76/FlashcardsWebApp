from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def index(request):
    return HttpResponse("Flashcards index")

def flashcard(request, flashcard_id):
    return HttpResponse(f"Place holder-------Flashcard ID: {flashcard_id}")
    
def create(request):
    return HttpResponse("Creating Flashcards")
