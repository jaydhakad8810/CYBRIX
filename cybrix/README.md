# CYBRIX AI

Initial full-stack foundation for the CYBRIX AI cybersecurity analysis platform.

## Stack

- Frontend: React + Vite + Tailwind CSS
- Backend: FastAPI
- Database: Supabase (planned, not wired yet)

## Project Structure

```text
cybrix/
├── frontend/
├── backend/
└── docs/
```

## Run Backend

```bash
cd cybrix/backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs at `http://localhost:8000`.

## Run Frontend

```bash
cd cybrix/frontend
npm install
npm run dev
```

Frontend runs at `http://localhost:5173`.

## Environment Notes

The frontend uses `VITE_API_BASE_URL` if provided. Otherwise it defaults to `http://localhost:8000`.

Example:

```bash
VITE_API_BASE_URL=http://localhost:8000
```

## Current Scope

- Placeholder analysis endpoints
- Simple analysis UI
- Frontend-to-backend connectivity
- No business logic yet
