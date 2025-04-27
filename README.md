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

- 🧠 **Movie Knowledge Quiz**
  - Answer 5 multiple-choice questions about different movies and cinematography.
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
hogwarts-explorer/
├── hogwarts/             # Django app for houses, characters, chat views
├── hp_explorer/          # Django project settings (wsgi, urls, settings)
├── staticfiles/          # Collected static files after running collectstatic
├── .gitignore            # Rules for ignoring unnecessary files in Git
├── Procfile              # Command for starting the app on Render
├── README.md             # Project documentation
├── create_superuser.py   # Script for auto-creating Django superuser
├── manage.py             # Django management utility
└── requirements.txt      # List of Python dependencies
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

## Unique Approaches and Methodologies

- Used Local Storage to manage user favorites without authentication.
- Integrated dynamic AI chatbot responses without training custom models.
- Combined Bootstrap with custom CSS for a clean and modern UI.
- Ensured graceful fallback if character fields are missing.
- Focused on mobile-first responsive design early in the process.

## Trade-offs During Development

- Chose client-side storage for favorites instead of database storage to keep the project lightweight and avoid adding authentication.
- Pulled character data live from external API rather than storing it locally to ensure always up-to-date data with minimal database load.
- Limited AI conversation to one character (Harry Potter) to prioritize stability over feature complexity.
- Used a simple form-based filtering instead of a live search bar to reduce backend complexity.

## Known Issues

- Some characters from the API may lack images or have incomplete data.
- No loading spinner currently shown while fetching character data.
- Occasionally, AI bot responses may be less coherent due to OpenRouter external service behavior.
- House filtering depends on exact house names; minor inconsistency might occur based on external API data.

## External APIs 📡

- **OpenRouter AI API**  
  Source: [https://openrouter.ai/](https://openrouter.ai/)  
  Provides AI-generated responses for character chat functionality using models like GPT-3.5 and Mistral 7B.

- **Harry Potter API**  
  Source: [https://hp-api.onrender.com/api/characters](https://hp-api.onrender.com/api/characters)  
  Provides character data used for browsing and filtering.

- **Open Trivia Database (OpenTDB)**  
  Source: [https://opentdb.com/](https://opentdb.com/)  
  Provides multiple-choice quiz questions used for the quiz feature.

## License 📄

This project is open-source and available for educational and non-commercial use.

## Author 👨‍💻

Developed by Abylay Slamzhanov.

Feel free to open an issue or submit a pull request to contribute to this project.
Email: abylajslamzanov@gmail.com

---

# 🎉 Enjoy exploring the magical world of Harry Potter!






