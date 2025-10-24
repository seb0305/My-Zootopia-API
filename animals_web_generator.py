import data_fetcher
from pathlib import Path
from typing import Any, Dict, List

TEMPLATE_PATH = "animals_template.html"
OUTPUT_PATH = "animals.html"
PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"

def serialize_animal(animal: Dict[str, Any]) -> str:
    """
    Creates an HTML card block containing basic information about a single animal.

    Args:
        animal (dict): Animal dictionary with keys 'name', 'locations', 'characteristics'.

    Returns:
        str: HTML string for this animal's card; empty string if key data is missing.
    """
    name = animal.get("name")
    locations = animal.get("locations") or []
    characteristics = animal.get("characteristics") or {}
    diet = characteristics.get("diet")
    type_ = characteristics.get("type")
    if not any([name, diet, locations, type_]):
        return ""
    lines: List[str] = []
    lines.append('<li class="cards__item">')
    if name:
        lines.append(f'  <div class="card__title">{name}</div>')
    lines.append('  <p class="card__text">')
    if diet:
        lines.append(f'      <strong>Diet:</strong> {diet}<br/>')
    if locations:
        lines.append(f'      <strong>Location:</strong> {locations[0]}<br/>')
    if type_:
        lines.append(f'      <strong>Type:</strong> {type_}<br/>')
    lines.append("  </p>")
    lines.append("</li>")
    return "\n".join(lines)

def build_animals_html_items(data: List[Dict[str, Any]]) -> str:
    """
    Serializes a list of animal dictionaries into a single HTML string,
    where each animal is rendered as a card.

    Args:
        data (list): List of animal dictionaries.

    Returns:
        str: Combined HTML string with all cards.
    """
    parts = []
    for animal in data:
        item_html = serialize_animal(animal)
        if item_html:
            parts.append(item_html)
    return "\n".join(parts)

def read_template(path: str) -> str:
    """
    Loads the HTML template from disk.

    Args:
        path (str): Path to the template file.

    Returns:
        str: Template file content.
    """
    return Path(path).read_text(encoding="utf-8")

def write_output(path: str, content: str) -> None:
    """
    Writes the generated HTML content to the output file.

    Args:
        path (str): Path to output HTML file.
        content (str): HTML content to write.
    """
    Path(path).write_text(content, encoding="utf-8")

def generate_html(animal_name: str,
                  template_path: str = TEMPLATE_PATH,
                  output_path: str = OUTPUT_PATH,
                  placeholder: str = PLACEHOLDER) -> str:
    """
    Fetches animal data for the given animal name and generates a website HTML file.
    If no animals are found, displays a friendly error message.

    Args:
        animal_name (str): Name of the animal to search.
        template_path (str): Path to the HTML template.
        output_path (str): Path for the output HTML file.
        placeholder (str): Placeholder in template to replace with animal HTML.

    Returns:
        str: Output path to the generated HTML website.
    """
    data = data_fetcher.fetch_data(animal_name)
    if not data:
        items_html = f'<h2 style="color:red; text-align:center;">The animal \"{animal_name}\" doesn\'t exist.</h2>'
    else:
        items_html = build_animals_html_items(data)
    template = read_template(template_path)
    html_out = template.replace(placeholder, items_html)
    write_output(output_path, html_out)
    return output_path

def main() -> None:
    """
    Main program loop. Asks for animal name, generates the website, prints output path.
    """
    animal_name = input("Please enter an animal: ")
    out = generate_html(animal_name)
    print(f"Website was successfully generated to the file {out}.")

if __name__ == "__main__":
    main()
