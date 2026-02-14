# Animals Website Generator
**Web-based HTML Generator for Animal Facts, Locations & Taxonomy (API Ninjas Integration)**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Requests](https://img.shields.io/badge/Requests-HTTP%20Client-green)](https://docs.python-requests.org/)
[![dotenv](https://img.shields.io/badge/python-dotenv-yellow)](https://pypi.org/project/python-dotenv/)

## 🎯 Features

| Feature | Description |
|---------|-------------|
| **Live Animals API Lookup** | Fetches animal data from the API Ninjas Animals endpoint by name (e.g. "frog", "lion").  |
| **Card-Based HTML Layout** | Generates responsive animal cards (name, diet, location, type) into a styled gallery.  |
| **Template-Driven Output** | Injects content into `animals_template.html` using a placeholder (`REPLACE_ANIMALS_INFO`). |
| **Friendly Error Page** | Shows a clear red message in the HTML if no animals are found for the given query.  |
| **Single-File Result** | Produces a standalone `animals.html` page ready to open in any browser.  |

## 🏗️ Tech Stack

Frontend: Static HTML + CSS (custom card layout in `animals_template.html`)  
Backend: Python 3 script (`animals_web_generator.py`) orchestrating fetch → transform → render  
API: [API Ninjas – Animals](https://api-ninjas.com/api/animals) via `requests` 
Config: `.env` file for `API_KEY` using `python-dotenv`   
Dependencies: Listed in `requirements.txt` (requests, python-dotenv)

## 🚀 Quick Start

```bash
# Clone & install
git clone https://github.com/seb0305/Animals-Website-Generator.git
cd Animals-Website-Generator
pip install -r requirements.txt

# Set API Ninjas key in .env
echo "API_KEY=your_api_key_here" > .env

# Run generator
python animals_web_generator.py

# When prompted, enter an animal name (e.g. "frog" or "lion")
# Website will be generated as animals.html
```

Open the generated file in your browser:

```bash
# On most systems
open animals.html          # macOS
xdg-open animals.html      # Linux
start animals.html         # Windows
```

## 🎮 How to Use
1. Start the Generator
    Run python animals_web_generator.py in your project directory.
2. Enter an Animal Name
   
    When prompted (Please enter an animal), type a name, for example:

    - frog → Generates cards for many frog species.

    - lion → Generates cards for lion-related entries.

3. View the Result Page: The script fetches data via data_fetcher.fetch_data, serializes each animal into an HTML li class="cards-item" with:

    - Name (card title)

    - Diet

    - Location (first location if multiple)

    - Type (e.g., Amphibian, Mammal)

4. No Results Case

    If the API returns an empty list, the placeholder is replaced by:

```xml
<h2 style="color:red; text-align:center">
  The animal X doesn't exist.
</h2>
```
so the user sees a clear error message in the browser.

5. Iterate and Explore

    Re-run the script with different animal names to generate fresh animals.html pages as often as you like.

## 🧠 Implementation Details
- API Fetching (data_fetcher.py)

    - Loads API_KEY from .env using dotenv.load_dotenv() at import time.

    - Calls https://api.api-ninjas.com/v1/animals with header X-Api-Key: API_KEY and name query param.

    - Returns a list of animal dictionaries with fields like name, locations, characteristics (diet, type, etc.).

- HTML Generation (animals_web_generator.py)

    - serialize_animal(animal):

    - Extracts name, first locations entry, diet, and type from characteristics.

    - Skips animals where all of these are missing to avoid empty cards.

    - Produces a single <li> card with <div class="card-title"> and <p class="card-text">.

- build_animals_html(data):

    - Loops over all animals and concatenates card HTML into one big string.

- generate_html(animal_name):

    - Fetches data, builds cards or error message, reads animals_template.html, replaces the REPLACE_ANIMALS_INFO placeholder, and writes to animals.html.

    - Returns the path to the generated file.

- Template (animals_template.html)

    - Defines page layout, fonts, and card styling (shadow, rounded corners, centered title).

    - Contains:

```xml
<h1>My Animal Repository</h1>
<ul class="cards">
  REPLACE_ANIMALS_INFO
</ul>
```

which becomes a full gallery after replacement.


## 📝 Development
```bash
# Run generator in dev mode (same as prod, no server needed)
python animals_web_generator.py

# Quick API test
python -c "from data_fetcher import fetch_data; print(len(fetch_data('frog')))"

# Regenerate sample page from template
python -c "from animals_web_generator import generate_html; generate_html('frog')"
```

## 🙌 Contributing
- Fork & clone the repository.

- Improve card design (CSS), add new fields, or adjust the template.

- Extend error handling (rate limits, network issues).

- Add tests for serialize_animal and build_animals_html.

- Open a pull request with a clear description of your changes.

## 📄 License
MIT – Free for personal and educational use.