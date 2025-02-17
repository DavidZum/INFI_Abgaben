import os
from PIL import Image

type = 'stone'

input_folder = 'Aufgabe_06/img/' + type + '/'
output_folder = 'Aufgabe_06/img_resized/' + type + '/'

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith('.png'):
        try:
            img = Image.open(os.path.join(input_folder, filename))
            img_small = img.resize((180, 180))
            img_small.save(os.path.join(output_folder, filename))
        except Exception as e:
            print(f"Fehler bei {filename}: {e}")
