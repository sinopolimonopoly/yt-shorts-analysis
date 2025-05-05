import csv
import os

def create_phrase_csv(phrase_dict, channel, output_folder="../../../data/phrase_datasets"):

    file_name = f"{channel}_phrase_dataset.csv"
    
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), output_folder))

    file_path = os.path.join(base_dir, file_name)

    with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow(["Video ID", "Title", "SOALAS Count", "LAS Count", "Applewood Count", "Transcript?"])

        for video_id, info in phrase_dict.items():
            title = info["Title"]
            soalas_count = info["SOALAS Count"]
            las_count = info["LAS Count"]
            applewood_count = info["Applewood Count"]
            is_transcript = info["Transcript?"]

            writer.writerow([video_id, title, soalas_count, las_count, applewood_count, is_transcript])