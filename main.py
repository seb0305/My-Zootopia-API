import requests

API_KEY = "yMFgesWf8cTpujXTRlKTfg==P7czWNYAwh7rLA6J"

def search_animal(animal_name):
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {"X-Api-Key": API_KEY}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Return JSON data on success
        return response.json()
    else:
        # Return error info if request failed
        return {
            "error_code": response.status_code,
            "error_message": response.text
        }

if __name__ == "__main__":
    # Example with an existing animal
    animal = "cheetah"
    result = search_animal(animal)
    print(f"Results for '{animal}':")
    print(result)

    # Example with a non-existent animal
    animal = "unicorn123"
    result = search_animal(animal)
    print(f"\nResults for '{animal}':")
    print(result)
