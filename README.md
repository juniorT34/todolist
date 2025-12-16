# Todo List

A small Python project that demonstrates a simple todo application structure with models and utilities.

## Overview

This repository contains a minimal todo application skeleton. It includes data models for users and todos, utility helpers for database access and logging, and a small entrypoint in `main.py`.

## Features

- Lightweight, dependency-free project structure
- `models/` for domain objects (`todo.py`, `user.py`)
- `utils/` for shared helpers (`database.py`, `logger.py`)

## Requirements

- Python 3.13 or newer (see `pyproject.toml`)

## Quickstart

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt  # or use pyproject-based tools
```

3. Run the app:

```bash
python main.py
```

## Project Structure

- `main.py` — application entrypoint
- `models/` — `todo.py`, `user.py`
- `utils/` — `database.py`, `logger.py`

