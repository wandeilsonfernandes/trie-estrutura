# trieapp/views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Trie

trie = Trie()

class TrieView(View):
    def get(self, request):
        return render(request, 'trieapp/index.html')

    def post(self, request):
        action = request.POST.get('action')
        word = request.POST.get('word')
        prefix = request.POST.get('prefix')
        
        if action == 'insert' and word:
            trie.insert(word)
            message = f'Palavra "{word}" inserida.'
        elif action == 'search' and word:
            found = trie.search(word)
            message = f'Palavra "{word}" encontrada: {found}.'
        elif action == 'starts_with' and prefix:
            starts_with = trie.starts_with(prefix)
            message = f'Palavras que começam com "{prefix}": {starts_with}.'
        else:
            message = 'Ação inválida ou parâmetros ausentes..'

        return render(request, 'trieapp/index.html', {'message': message})
