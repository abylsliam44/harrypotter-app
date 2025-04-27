# Harry Potter Explorer

Harry Potter Explorer is a Django web application that allows users to explore Hogwarts houses, browse Harry Potter characters, save favorites, take a themed quiz, and chat with AI-powered characters.

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

### 2. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Mac/Linux
```

### 3. Install the dependencies:

```bash
pip install -r requirements.txt
```

### 4. Create a .env file for secret keys:

```bash
HF_API_KEY=your_huggingface_api_key
```

### 5. Run the Django development server:

```bash
HF_API_KEY=your_huggingface_api_key
```

### Open your browser and go to:

```bash
http://127.0.0.1:8000/
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
- Setting up Django project and applications (hogwarts, core).
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






