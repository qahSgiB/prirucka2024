import click

from prirucka2024.download_url import download_url as download_url_func
from prirucka2024.split_html_on_headers import split_html as split_html_func


@click.group()
def main():
    """CLI for the prirucka2024 RAG application."""
    pass


@main.command()
@click.argument("url")
@click.argument("output_file")
def download_url(url, output_file):
    """Download the HTML content from a given URL and save it to a file."""
    download_url_func(url, output_file)


@main.command()
@click.argument("file_path")
@click.option(
    "--output-pkl",
    default="chunks.pkl",
    help="Name of the pickle output file.",
)
@click.option(
    "--output-txt", default="chunks.txt", help="Name of the text output file."
)
@click.option(
    "--interactive", is_flag=True, help="Enable interactive mode for rejecting splits."
)
def split_html_on_headers(file_path, output_pkl, output_txt, interactive):
    """Split HTML file on headers and save results."""
    split_html_func(file_path, output_pkl, output_txt, interactive)


if __name__ == "__main__":
    main()
