# 📚 Projeto Trie com Django

Este repositório contém uma implementação de uma **Trie** usando o framework **Django**. O projeto foi desenvolvido como parte de uma apresentação na disciplina **Estrutura de Dados II** da **Universidade Estadual de Roraima**. Ele utiliza uma lista de mais de 240 mil palavras em português para demonstração de funcionalidades como inserção, busca, remoção e autocompletar.

---

## 🚀 Funcionalidades

- 🔍 **Busca**: Verifique se uma palavra existe no dicionário.
- ✏️ **Inserção**: Adicione palavras à Trie.
- ❌ **Remoção**: Remova palavras específicas.
- ✨ **Autocompletar**: Sugestões de palavras com base em um prefixo fornecido.
- 📖 **Dicionário Extenso**: Mais de 240 mil palavras pré-carregadas!

---

## 🛠️ Como executar o projeto

Siga os passos abaixo para configurar e executar o projeto:

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/wandeilsonfernandes/trie-estrutura.git
cd projeto-trie
```

### 2️⃣ Crie e ative um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure o banco de dados do Django
```bash
python manage.py migrate
```

### 5️⃣ Adicione o arquivo de palavras
- Certifique-se de que o arquivo `dicionario.txt` com as 240 mil palavras esteja localizado em `trieapp/dicionario.txt`.

### 6️⃣ Execute o servidor
```bash
python manage.py runserver
```

### 7️⃣ Acesse o projeto no navegador
Abra o navegador e vá para [http://127.0.0.1:8000/trie/](http://127.0.0.1:8000/trie/).

---

## 📋 Estrutura do Projeto

- **`models.py`**: Contém a implementação da estrutura Trie.
- **`views.py`**: Define as interações entre o usuário e a Trie.
- **`urls.py`**: Configura as rotas para acesso à interface da Trie.
- **`dicionario.txt`**: Arquivo contendo as palavras usadas para preencher a Trie.
- **`index.html`**: Interface básica para exibir resultados de busca e autocompletar.

---

## 🧐 Como funciona?

1. Ao iniciar o projeto, a Trie é preenchida com as palavras do arquivo `dicionario.txt`.
2. O usuário pode buscar palavras ou solicitar sugestões com base em um prefixo:
   - Exemplo: Digite **"car"** no campo de prefixo, e o sistema sugerirá palavras como **"carro"**, **"carta"**.
3. Os resultados são exibidos na interface web gerada pelo Django.

---

## 📚 O que é uma Trie?

Uma **Trie** (ou árvore de prefixo) é uma estrutura de dados eficiente para armazenar e buscar strings. Ela é amplamente usada em sistemas de autocompletar e dicionários.

---

## 🛡️ Tecnologias Utilizadas

- 🐍 **Python 3.9+**
- 🌐 **Django 4.0+**
- 📄 **HTML/CSS**
- 📖 **Dicionário de Palavras em Português**

---

## 🧑‍💻 Desenvolvido por

👨‍🎓 **Wandeilson Fernandes**  
📧 Entre em contato: [wandeilson@alunos.uerr.edu.br](mailto:wandeilson@alunos.uerr.edu.br)

---

🎉 **Divirta-se explorando o projeto** 🎉
