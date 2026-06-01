# AngelicaAI GPT-3 Django Project

This is a refactored Django project that combines a simple GPT-powered assistant with a 3D Angelica scene renderer.

## What it does

- Serves a web application using Django
- Provides a natural language assistant powered by OpenAI
- Keeps the existing 3D canvas experience intact
- Uses environment variables for secrets and configuration

## Features

- Clean web form for asking questions
- GPT-3.5 Turbo chat integration
- Friendly error handling when the API key is missing or the request fails
- Simple modern project structure

## Setup

1. Copy the example environment file:

```bash
cp .env.example .env
```

2. Install dependencies in a fresh environment:

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

3. Set your OpenAI API key in `.env`:

```env
OPENAI_API_KEY=sk-...
```

4. Run migrations and start the server:

```bash
python gpt3_django/manage.py migrate
python gpt3_django/manage.py runserver
```

5. Open the browser at `http://127.0.0.1:8000`

## Notes

- The project no longer stores API keys in source code.
- The old `virtual_env` folder was replaced with a standard `.venv`.
- The 3D viewer and chat assistant are intended to coexist on the same page.
