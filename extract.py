import os
import shutil
import pandas as pd

df = pd.read_csv("data_from_17Feb.csv")
a = int(input("Enter start range: "))
b = int(input("Enter ending range: "))
for i in range(a, b):
    
    folder_name = df["folder_name"][i]  # Safer indexing
    print(folder_name)

    source = "/media/appsmartz/storage/annotation/static/instrumantal_midi_unlabled/"+str(folder_name)
    print(f"Source:{source}")
    destination = "/media/appsmartz/storage/annotation/Kartik_Codes/Todays_18/"+str(folder_name)
    print(f"Destination: {destination}") 

    if os.path.exists(source):
        shutil.move(source, destination)
        print(f"Moved: {folder_name}")
    else:
        print(f"Source not found: {folder_name}")
