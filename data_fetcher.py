import requests
from typing import Any, Dict, List

API_KEY = "yMFgesWf8cTpujXTRlKTfg==P7czWNYAwh7rLA6J"
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
