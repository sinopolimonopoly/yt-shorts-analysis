import csv
import os

def create_phrase_csv(phrase_dict):

    with open('MTMG Phrase Dataset.csv', 'w', newline='', encoding='utf-8') as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow(["Video ID", "Title", "SOALAS Count", "LAS Count", "Applewood Count"])

        for video_id, info in phrase_dict.items():
            title = info["Title"]
            soalas_count = info["SOALAS Count"]
            las_count = info["LAS Count"]
            applewood_count = info["Applewood Count"]

            writer.writerow([video_id, title, soalas_count, las_count, applewood_count])