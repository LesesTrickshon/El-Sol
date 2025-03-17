import os
import requests
import time

# Global Variables:
links = []
list_name = input("Name of the scraped file: ")
list_path = os.path.join(".\Data\csv", list_name)
img_dir = ".\Data\Train-Images"

# Saves each link from the provided csv file into the links array
l = open(list_path, 'r')
for line in l:
    clean_line = line.strip()
    links.append(clean_line)
l.close()

# Copys the Image Data, Creates a new file and pastes the data into it.
print("\n===[ Beginning the Download! ]===\n")
for url in range(0, len(links)):
    bar = "" 
    data = requests.get(links[url]).content
    img = open(os.path.join(img_dir, str(url) + ".jpg"), "wb")
    img.write(data)
    img.close()

    # Gives Information about the download (Also adds a progess bar)
    print(f"Downloaded image {url+1}.jpg from {links[url]}")
    percent = (url+1) / len(links) * 100
    bar_percent = int(percent/2)
    for i in range(0,50):
        if i <= bar_percent:
            bar += "█"
        else:
            bar += "-"
    print(f"{int(percent)}% {bar} 100%\n\n")

    # Makes it not seem like a Dos tool!
    time.sleep(0.5)
