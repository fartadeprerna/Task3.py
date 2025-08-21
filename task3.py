import os
import shutil
import re
import requests

def move_jpg_files():
    src = input("Enter source folder path: ")
    dst = input("Enter destination folder path: ")

    if not os.path.exists(dst):
        os.makedirs(dst)

    count = 0
    for file in os.listdir(src):
        if file.lower().endswith(".jpg"):
            shutil.move(os.path.join(src, file), os.path.join(dst, file))
            count += 1

    print(f"{count} JPG file(s) moved successfully!")


def extract_emails():
    input_file = input("Enter path of input .txt file: ")
    output_file = input("Enter path to save emails (e.g., emails.txt): ")

    with open(input_file, "r") as f:
        text = f.read()

    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text)

    with open(output_file, "w") as f:
        for email in emails:
            f.write(email + "\n")

    print(f"{len(emails)} email(s) extracted and saved to {output_file}!")


def scrape_title():
    url = input("Enter webpage URL: ")
    output_file = input("Enter path to save title (e.g., title.txt): ")

    response = requests.get(url)
    title = re.search(r"<title>(.*?)</title>", response.text, re.IGNORECASE)

    if title:
        with open(output_file, "w") as f:
            f.write(title.group(1))
        print(f"Title saved to {output_file}!")
    else:
        print("No title found.")


def main():
    while True:
        print("\n--- Task Automation Menu ---")
        print("1. Move all .jpg files to a new folder")
        print("2. Extract emails from a .txt file")
        print("3. Scrape the title of a webpage")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            move_jpg_files()
        elif choice == "2":
            extract_emails()
        elif choice == "3":
            scrape_title()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
