import os
import shutil

FOLDER_PATH = "organize_me"

EXTENSIONS = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"]
}

if not os.path.exists(FOLDER_PATH):
    print("❌ Folder not found!")
    exit()

for filename in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, filename)

    if os.path.isfile(file_path):
        moved = False

        for folder, exts in EXTENSIONS.items():
            if filename.lower().endswith(tuple(exts)):
                os.makedirs(folder, exist_ok=True)
                shutil.move(file_path, os.path.join(folder, filename))
                moved = True
                break

        if not moved:
            os.makedirs("Others", exist_ok=True)
            shutil.move(file_path, os.path.join("Others", filename))

print("✅ Files organized successfully!")
