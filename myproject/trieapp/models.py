class TrieNode:
    def __init__(self, valor):
        self.valor = valor
        self.filhos = {}
        self.folha = False

class Trie:
    def __init__(self):
        self.raiz = TrieNode(None)

    def inserir(self, palavra):
        no_atual = self.raiz
        for letra in palavra:
            if letra not in no_atual.filhos:
                no_atual.filhos[letra] = TrieNode(letra)
            no_atual = no_atual.filhos[letra]
        no_atual.folha = True

    def buscar(self, palavra):
        return self._buscar(palavra, self.raiz)

    def _buscar(self, palavra, no_atual):
        if palavra == '':
            return no_atual.folha
        if palavra[0] in no_atual.filhos:
            return self._buscar(palavra[1:], no_atual.filhos[palavra[0]])
        return False

    def remover(self, palavra):
        self._remover(palavra, self.raiz)

    def _remover(self, palavra, no_atual):
        if palavra == '':
            if no_atual.folha:
                no_atual.folha = False
            return len(no_atual.filhos) == 0

        letra = palavra[0]
        if letra not in no_atual.filhos:
            return False

        filho_atual = no_atual.filhos[letra]
        pode_apagar = self._remover(palavra[1:], filho_atual)

        if pode_apagar:
            del no_atual.filhos[letra]
            return len(no_atual.filhos) == 0 and not no_atual.folha
        return False

    def autocompletar(self, prefixo, limite=10):
        resultados = []
        no_atual = self._encontrar_no(prefixo)
        if no_atual:
            self._encontrar_palavras(no_atual, prefixo, resultados)
        return resultados[:limite]

    def _encontrar_no(self, prefixo):
        no_atual = self.raiz
        for letra in prefixo:
            if letra not in no_atual.filhos:
                return None
            no_atual = no_atual.filhos[letra]
        return no_atual

    def _encontrar_palavras(self, no_atual, prefixo, resultados):
        if no_atual.folha:
            resultados.append(prefixo)
        for letra, filho in no_atual.filhos.items():
            self._encontrar_palavras(filho, prefixo + letra, resultados)
