# Hogwarts Explorer 🪄

**Hogwarts Explorer** is a web application where users can browse Harry Potter characters, explore Hogwarts houses, favorite their favorite characters, and chat with an AI bot role-playing Harry Potter characters.

🌐 The project is deployed and available live at:  
👉 [https://harrypotter-app.onrender.com](https://harrypotter-app.onrender.com)
## Features ✨

- 🏠 **Houses Explorer**
  - View detailed information about the four Hogwarts houses.
  - Each house has unique attributes such as name, colors, animal symbol, founder, and traits.

- 🧙‍♂️ **Characters Directory**
  - Browse through characters from the Harry Potter universe.
  - Search characters by name.
  - Filter characters by house.
  - View detailed character pages including house, patronus, and image.

- ⭐ **Favorite Characters**
  - Add characters to your favorites list.
  - View and manage your favorites conveniently.

- 💬 **AI Chat with Characters**
  - Send messages to Harry Potter characters.
  - Receive AI-generated responses via the Hugging Face Inference API.

- 🧠 **Harry Potter Quiz**
  - Answer 5 Harry Potter-related multiple-choice questions.
  - Instantly receive your quiz results.

- 🔎 **Pagination**
  - Smooth and responsive paginated character listings.

- 🎨 **Responsive Design**
  - Built with Bootstrap 5 for full mobile and desktop compatibility.

## Technologies Used 🛠️

- Python 3.10
- Django 5.2
- PostgreSQL
- Bootstrap 5
- Requests (to fetch data from external APIs)
- Slugify (to generate clean URL slugs)
- Hugging Face Inference API (for AI chat functionality)

## Setup Instructions 🧩

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/harrypotter-app.git
cd harrypotter-app
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables (`.env`):
- `DATABASE_URL`
- `SECRET_KEY`
- `OPENROUTER_API_KEY`

### 4. Apply migrations:

```bash
python manage.py migrate
```

### 5. Collect static files:

```bash
python manage.py collectstatic --noinput
```

### 6. Run the server locally:

```bash
python manage.py runserver
```

## Project Structure 📂

```plaintext
hpotter_explorer/
├── hogwarts/           # Django app for Hogwarts features
│   ├── templates/      # HTML templates
│   ├── static/         # Static files (CSS, JS)
│   ├── urls.py         # App-specific URLs
│   ├── views.py        # App views
│   └── models.py       # Django models (House)
├── hp_explorer/        # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py           # Django management file
├── db.sqlite3          # Local database
├── .env                # Environment variables (excluded from Git)
├── .gitignore          # Ignored files list
└── README.md           # Project documentation
```
## Design and Development

The project was divided into several parts:
- Setting up Django project and applications.
- Creating models for Hogwarts houses and favorite characters.
- Integrating external Harry Potter character API.
- Developing character search and filter functionalities.
- Implementing favorites feature with local storage.
- Adding chat functionality via OpenRouter AI API.
- Designing adaptive UI using Bootstrap 5.
- Deploying to Render with PostgreSQL as a database.

## External APIs 📡

- **OpenRouter AI API**  
  Source: [https://openrouter.ai/](https://openrouter.ai/)  
  Provides AI-generated responses for character chat functionality using models like GPT-3.5 and Mistral 7B.

- **Harry Potter API**  
  Source: [https://hp-api.onrender.com/api/characters](https://hp-api.onrender.com/api/characters)  
  Provides character data used for browsing and filtering.

- **Open Trivia Database (OpenTDB)**  
  Source: [https://opentdb.com/](https://opentdb.com/)  
  Provides multiple-choice quiz questions used for the Harry Potter quiz feature.

## License 📄

This project is open-source and available for educational and non-commercial use.

## Author 👨‍💻

Developed by Abylay Slamzhanov.

Feel free to open an issue or submit a pull request to contribute to this project.

---

# 🎉 Enjoy exploring the magical world of Harry Potter!






