from django.db import models

# Create your models here.
# trieapp/models.py

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def load_dictionary(self, words):
        for word in words:
            self.insert(word)

    def autocomplete(self, prefix, limit=10):
        results = []
        node = self._find_node(prefix)
        if node:
            self._find_words(node, prefix, results)
        return results[:limit]  # Limitar a quantidade de sugestões

    def _find_node(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def _find_words(self, node, prefix, results):
        if node.is_end_of_word:
            results.append(prefix)
        for char, child_node in node.children.items():
            self._find_words(child_node, prefix + char, results)
