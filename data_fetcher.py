import requests
import os
from dotenv import load_dotenv
from typing import Any, Dict, List

load_dotenv()  # Load variables from .env into environment

API_KEY = os.getenv('API_KEY')
print(API_KEY)  # Optional: print to verify it was loaded correctly
API_URL = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name: str) -> List[Dict[str, Any]]:
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': { ... },
      'locations': [ ... ],
      'characteristics': { ... }
    }
    """
    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}
    response = requests.get(API_URL, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return []
