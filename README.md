# Nebula Admin

Flask-based admin panel with user authentication and Bootstrap 5 UI.

## Getting Started

### Prerequisites
- Python 3.7+
- MySQL Server

### Installation

1. **Clone and navigate to project**
```bash
cd nebula_admin
```

2. **Create virtual environment**
```bash
python -m venv .venv
```

3. **Activate virtual environment**
- Windows: `.venv\Scripts\activate`
- Linux/Mac: `source .venv/bin/activate`

4. **Install dependencies**
###### run
```bash
pip install Flask Flask-SQLAlchemy Flask-Login PyMySQL python-dotenv
```
**or**

```bash
pip install -r requirements.txt
```

5. **Configure environment**
```
cp .env.example .env
# Edit .env with your database credentials
```

6. **Run application**
```bash
python app.py
```

7. **Seed database (optional)**
```bash
python seeders.py
```

Application will run at `http://127.0.0.1:5000`

## Database Seeding
```bash
# Seed database with sample users
python seeders.py
```
```bash
# Clear database and seed fresh data
python seeders.py --fresh
```
```bash
# Only clear database without seeding
python seeders.py --clear-only
```

**Default Seeded Users:**
- john.doe@example.com
- jane.smith@example.com
- admin@example.com
- test@example.com

All users have password: `password123`

## Sass Commands
#### install sass globally
```bash
npm install -g sass
```
#### compile scss to css
```
sass <src> <destination> --style=compressed
```
