import os
import random
import yaml
from PIL import Image

def load_config():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)

def ask_questions(folder_path, num_questions):
    images = [img for img in os.listdir(folder_path) if img.endswith(".png")]
    selected_images = random.choices(images, k=num_questions)

    for i, image in enumerate(selected_images, start=1):
        question = f"({i}/{num_questions}) Q: {os.path.splitext(image)[0]}"
        print(question)
        input("Press Enter to see the answer...")
        img_path = os.path.join(folder_path, image)
        img = Image.open(img_path)
        img.show()

def main():
    config = load_config()
    num_questions = config["num_questions"]
    question_bank = config["folder_question_bank"]

    # List available folders in alphabetical order
    if not os.path.exists(question_bank):
        print(f"Error: Question bank folder '{question_bank}' does not exist.")
        return

    available_folders = sorted(
        [folder for folder in os.listdir(question_bank) if os.path.isdir(os.path.join(question_bank, folder))]
    )
    print("Available folders:")
    for folder in available_folders:
        print(f"- {folder}")

    folder_name = input("Enter the project name (folder): ").strip()
    folder_path = os.path.join(question_bank, folder_name)

    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    ask_questions(folder_path, num_questions)

if __name__ == "__main__":
    main()
