from django.shortcuts import render, redirect
from .models import Categoria, Flashcard
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.
def novo_flashcard(request):
    if not request.user.is_authenticated:
        return redirect('/usuarios/logar/')
    if request.method == 'GET':
        dificuldades = Flashcard.DIFICULDADE_CHOICES
        categorias = Categoria.objects.all()
        flashcards = Flashcard.objects.filter(user=request.user)
        
        categoria_filtro = request.GET.get('categoria')
        dificuldade_filtro = request.GET.get('dificuldade')
        if categoria_filtro:
            flashcards = flashcards.filter(categoria__id=categoria_filtro)
            
        if dificuldade_filtro:
            flashcards = flashcards.filter(dificuldade=dificuldade_filtro)
            
        return render(request, 'novo_flashcard.html', {'categorias': categorias, 'dificuldades': dificuldades, 
                                                       'flashcards': flashcards})
    elif request.method == "POST":
        pergunta = request.POST.get('pergunta')
        resposta = request.POST.get('resposta')
        categoria = request.POST.get('categoria')
        dificuldade = request.POST.get('dificuldade')
        
        if len(pergunta.strip()) == 0 or len(resposta.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'FlashCard não cadastrado. Preencha todos os campos.')
            return redirect('/flashcard/novo_flashcard/')
        
        
        flashcard = Flashcard(
            user = request.user,
            pergunta = pergunta,
            resposta = resposta,
            categoria_id = categoria,
            dificuldade = dificuldade,
        )
        flashcard.save()
        
        messages.add_message(request, constants.SUCCESS, 'FlashCard cadastrado com sucesso.')
        return redirect('/flashcard/novo_flashcard')
    