import os
import pickle
import logging
from rich import print
from langchain_text_splitters import HTMLHeaderTextSplitter

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Define the headers for splitting
HEADERS_TO_SPLIT_ON = [
    ("h1", "Header 1"),
    ("h2", "Header 2"),
    ("h3", "Header 3"),
]

html_splitter = HTMLHeaderTextSplitter(HEADERS_TO_SPLIT_ON)


def split_html(file_path, output_pkl, output_txt, interactive):
    """
    Split HTML file on headers and save results.

    Args:
        file_path (str): Path to the HTML file.
        output_pkl (str): Name of the pickle file for serialized splits.
        output_txt (str): Name of the text file for saving split contents.
        interactive (bool): Enable interactive mode for rejecting splits.
    """
    try:
        # Read HTML file
        with open(file_path, "r", encoding="utf-8") as f:
            html_string = f.read()

        all_html_header_splits = []
        html_header_splits = html_splitter.split_text(html_string)

        for split in html_header_splits:
            if interactive:
                os.system("cls" if os.name == "nt" else "clear")  # Clear the screen
                print("=====")
                print(split.metadata)
                print(split.page_content)
                user_input = input(
                    "Press <Enter> to keep this split, <d> to disregard: "
                )
                if user_input.lower() == "d":
                    continue

            all_html_header_splits.append(split)

        # Save splits to pickle
        with open(output_pkl, "wb") as f:
            pickle.dump(all_html_header_splits, f)
        logger.info(f"Serialized splits saved to {output_pkl}")

        # Save splits to text file
        with open(output_txt, "w", encoding="utf-8") as f:
            for header_split in all_html_header_splits:
                f.write("=====\n")
                f.write(str(header_split.metadata) + "\n")
                f.write(header_split.page_content + "\n")
        logger.info(f"Split contents saved to {output_txt}")

        logger.info(f"Number of header splits: {len(all_html_header_splits)}")

    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
