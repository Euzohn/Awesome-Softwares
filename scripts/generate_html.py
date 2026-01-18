#!/usr/bin/env python3
"""
Awesome Softwares - HTML Generator
Generates index.html with embedded JSON data to avoid CORS issues
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "software.json"
HTML_FILE = Path(__file__).parent.parent / "index.html"

def main():
    # Load the JSON data
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Read the HTML template
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Embed the JSON data as a JavaScript variable
    embedded_data = json.dumps(data, ensure_ascii=False, indent=None)

    # Replace the embedded data (if exists) or add it
    if "const data = " in html_content:
        # Find the start of const data =
        start = html_content.find("const data = ")
        # Find the end of the data object (assuming it's followed by ; and \n)
        end = html_content.find(";", start) + 1
        old_data = html_content[start:end]
        new_data = "const data = " + embedded_data + ";"
        html_content = html_content.replace(old_data, new_data)
    else:
        # Fallback: replace the fetch-based loadData function with embedded data
        old_load_data = """        async function loadData() {
            try {
                const response = await fetch('data/software.json');
                const data = await response.json();
                softwareList = data.software_list;
                categories = data.categories;
                populateCategories();
                displaySoftware(softwareList);
            } catch (error) {
                console.error('Error loading data:', error);
            }
        }"""

        new_load_data = "        const data = " + embedded_data + ";\n        softwareList = data.software_list;\n        categories = data.categories;\n        populateCategories();\n        displaySoftware(softwareList);"

        html_content = html_content.replace(old_load_data, new_load_data)

    # Remove the loadData() call at the end
    html_content = html_content.replace("        loadData();", "")

    # Write the updated HTML back to the file
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)

    print("Generated index.html with embedded data")

if __name__ == "__main__":
    main()