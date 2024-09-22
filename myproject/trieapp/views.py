# trieapp/views.py

from django.shortcuts import render
from django.views import View
from .models import Trie

# Inicializa a Trie
trie = Trie()

# Carrega o dicionário de palavras de um arquivo
def carregar_palavras_do_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        palavras = arquivo.read().splitlines()  # Remove as quebras de linha
    return palavras

# Carregar as palavras do dicionário na Trie
caminho_arquivo = 'trieapp/dicionario.txt'
palavras = carregar_palavras_do_arquivo(caminho_arquivo)
for palavra in palavras:
    trie.inserir(palavra)

class TrieView(View):
    def get(self, request):
        suggestions = []
        message = ''
        prefix = request.GET.get('prefix', '')

        if prefix:
            suggestions = trie.autocompletar(prefix)
            message = f'Sugestões para "{prefix}": {suggestions}'

        return render(request, 'trieapp/index.html', {'suggestions': suggestions, 'message': message})
