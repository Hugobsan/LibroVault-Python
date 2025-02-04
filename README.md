# 📚 Semantic Search API - FastAPI

Este projeto é um **microsserviço em Python** que utiliza **FastAPI** e **Sentence-Transformers** para geração e comparação de embeddings de texto. Ele fornece dois endpoints para o Laravel interagir:

1. **`embedding/make`** → Gera um embedding para um conteúdo textual de um livro.
2. **`embedding/compare`** → Compara uma query com embeddings previamente armazenados e retorna um ranking de similaridade.

---

## 🚀 Tecnologias Utilizadas
- [FastAPI](https://fastapi.tiangolo.com/) → Framework web assíncrono para API REST.
- [Hypercorn](https://pgjones.gitlab.io/hypercorn/) → Servidor ASGI para execução da API.
- [Sentence-Transformers](https://www.sbert.net/) → Modelo de NLP para geração de embeddings.
- [NumPy](https://numpy.org/) → Processamento vetorial e cálculos matemáticos.
- [Pydantic](https://docs.pydantic.dev/) → Validação de dados de entrada.

---

## 📌 Requisitos
- Python 3.8+
- Pip
- Virtualenv

---

## 📦 Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-repositorio.git semantic_service
   cd semantic_service
   ```

2. **Crie e ative o ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o ambiente**
   ```bash
   cp .env.example .env
   ```

---

## ▶️ Como Rodar

**Rodar com Hypercorn**
```bash
python main.py
```
---

## 📡 Endpoints

### 1️⃣ Criar Embedding (`embedding/make`)

**Rota:**  
`POST /api/embedding/make`

**Request Body:**
```json
{
    "text": "Este é um exemplo de texto para teste.",
    "book_id": 1,
    "page_number": 10
}
```

**Resposta esperada:**
```json
{
    "embedding": [0.123, -0.456, 0.789, ...]
}
```

---

### 2️⃣ Buscar Embeddings (`embedding/compare`)

**Rota:**  
`POST /api/embedding/compare`

**Request Body:**
```json
{
    "query": "Qual é o conteúdo sobre inteligência artificial?",
    "embeddings": [
        {
            "page_number": 1,
            "book_id": 3,
            "embedding": "/caminho/para/embedding1.json"
        },
        {
            "page_number": 2,
            "book_id": 3,
            "embedding": "/caminho/para/embedding2.json"
        }
    ]
}
```

**Resposta esperada:**
```json
{
    "ranking": [
        {
            "page_number": 1,
            "book_id": 3,
            "embedding": "/caminho/para/embedding1.json",
            "similarity": 0.98
        },
        {
            "page_number": 2,
            "book_id": 3,
            "embedding": "/caminho/para/embedding2.json",
            "similarity": 0.95
        }
    ]
}
```
## 📝 Licença
Este projeto é de código aberto e está sob a **MIT License**.

---

## 💡 Contribuição
Sinta-se à vontade para abrir issues e pull requests para melhorias no projeto.

---
