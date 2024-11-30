import csv
import random
from itertools import cycle

date_range = ['2024-11-13', '2024-11-14', '2024-11-15', '2024-11-16', '2024-11-17']
date_cycle = cycle(date_range)

video_ids = [f"vid_{i}" for i in range(1, 11)]
content_ids = [f"cid_{i}" for i in range(1, 11)]

data = []
for video_id, content_id in zip(video_ids, content_ids):
    for _ in range(5):
        row = {
            "video_id": video_id,
            "content_id": content_id,
            "uploaded_date": next(date_cycle),
            "quantity": random.randint(2500, 20000),
        }
        data.append(row)

output_file = 'Generated_Viewership.csv'
with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    fieldnames = ["video_id", "content_id", "uploaded_date", "quantity"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print(f"File {output_file} has been created successfully.")
