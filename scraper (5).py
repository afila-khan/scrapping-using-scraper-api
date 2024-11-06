import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
# Your ScraperAPI key
API_KEY = "81716f65a1801a31bc95201daf29aaf4"

# Read the Excel sheet and extract affiliation names
# (You'll need to implement this part based on your specific Excel file)
# affiliations = ["kct", "vit", "university of horizona", "university of alabama"]
df = pd.read_excel(r"C:\Users\patel\Desktop\roche_backup\local_ollama\affiliations.xlsx")

# # Create a folder for each affiliation
# for affiliation in affiliations:
#     folder_path = os.path.join("websites", affiliation)
#     os.makedirs(folder_path, exist_ok=True)
for index, row in df.iterrows():
    affiliation = row["Affiliation"]

    # Create a folder for each affiliation
    folder_path = os.path.join("websites", affiliation)
    os.makedirs(folder_path, exist_ok=True)


    # Send a request to ScraperAPI
    url = f"https://www.google.com/search?q={affiliation}"
    response = requests.get(url, headers={"x-api-key": API_KEY})

    # Parse the HTML response
    soup = BeautifulSoup(response.content, "html.parser")

    # Save the website content
    with open(os.path.join(folder_path, "index.html"), "w", encoding="utf-8") as html_file:
        html_file.write(str(soup))

    print(f"Saved website for {affiliation} in {folder_path}")

print("All websites saved successfully!")
