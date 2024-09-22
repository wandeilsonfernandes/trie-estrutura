import time
from django.shortcuts import render
from django.views import View
from .models import Trie

trie = Trie()

# Carregar o dicionário do arquivo
with open('trieapp/dicionario.txt', 'r', encoding='utf-8') as f:
    words = [line.strip() for line in f.readlines()]
    trie.load_dictionary(words)

class TrieView(View):
    def get(self, request):
        suggestions = []
        message = ''
        prefix = request.GET.get('prefix', '')
        
        if prefix:
            start_time = time.time()
            suggestions = trie.autocomplete(prefix)
            elapsed_time = time.time() - start_time
            message = f'Sugestões para "{prefix}": {suggestions} (tempo: {elapsed_time:.4f}s)'
        
        return render(request, 'trieapp/index.html', {'suggestions': suggestions, 'message': message})

    def post(self, request):
        action = request.POST.get('action')
        word = request.POST.get('word')

        if action == 'insert' and word:
            trie.insert(word)
            message = f'Palavra "{word}" inserida.'
        else:
            message = 'Ação inválida ou parâmetros ausentes.'

        return render(request, 'trieapp/index.html', {'message': message, 'suggestions': []})
