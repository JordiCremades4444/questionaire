import os
import random

import yaml  # type: ignore
from PIL import Image  # type: ignore


def load_config(yaml_file):
    with open(yaml_file, "r") as file:
        return yaml.safe_load(file)


def images_pool(folder_path):
    return [img for img in os.listdir(folder_path) if img.endswith(".png")]


def ensure_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Error: Folder '{folder_path}' does not exist.")


def folders_pool(folder_path):
    return [
        folder
        for folder in os.listdir(folder_path)
        if os.path.isdir(os.path.join(folder_path, folder))
    ]


def print_with_separator(text):
    print("-" * 20)
    print("-" * 20)
    print(text)
    print("-" * 20)
    print("-" * 20)


def folder_name_mapper(input_folder_name, folder_question_bank):
    if input_folder_name == "any":
        folders = folders_pool(folder_question_bank)
        folder_name = random.choice(folders)

    else:
        folder_name = input_folder_name

    return folder_name


def loop_through_images(folder_path, selected_images, num_questions):
    for i, image in enumerate(selected_images, start=1):
        question = (
            f"[{num_questions}] ({i}/{num_questions}) Q: {os.path.splitext(image)[0]}"
        )
        print(question)
        input("Press Enter to see the answer...")
        img_path = os.path.join(folder_path, image)
        img = Image.open(img_path)
        img.show()


def main():
    # Config
    config = load_config("config.yaml")
    folder_question_bank = config["folder_question_bank"]

    ensure_folder_exists(folder_question_bank)

    # Available folders
    folders = folders_pool(folder_question_bank)
    print_with_separator("'Any' selects a random folder")
    for folder in folders:
        print(f"- {folder}")

    # Input folder name
    input_name = input("Enter the project name (folder): ").strip()
    mapped_name = folder_name_mapper(input_name, folder_question_bank)

    # Ensure folder exists
    folder_path = os.path.join(folder_question_bank, mapped_name)
    ensure_folder_exists(folder_path)

    # Loop questions
    os.system("clear")

    # Loop
    print_with_separator(mapped_name)
    images = images_pool(folder_path)
    num_questions = len(images)
    loop_through_images(folder_path, images, num_questions)


if __name__ == "__main__":
    main()
