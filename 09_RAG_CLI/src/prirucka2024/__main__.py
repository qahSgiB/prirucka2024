import click

from prirucka2024.download_url import download_url as download_url_func
from prirucka2024.split_html_on_headers import split_html as split_html_func
from prirucka2024.fill_vector_store import fill_vector_store as fill_vector_store_func


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
    default="all_html_header_splits.pkl",
    help="Name of the pickle output file.",
)
@click.option(
    "--output-txt", default="split_headers.txt", help="Name of the text output file."
)
@click.option(
    "--interactive", is_flag=True, help="Enable interactive mode for rejecting splits."
)
@click.option(
    "--drop-empty-metadata", is_flag=True, help="Drop splits with empty metadata."
)
def split_html_on_headers(
    file_path, output_pkl, output_txt, interactive, drop_empty_metadata
):
    """Split HTML file on headers and save results."""
    split_html_func(file_path, output_pkl, output_txt, interactive, drop_empty_metadata)


@main.command()
@click.argument("pickle_file")
@click.argument("chroma_db_dir")
@click.option(
    "--embedding-model",
    default="text-embedding-ada-002",
    help="OpenAI embedding model to use for vectorization.",
)
def fill_vector_store(pickle_file, chroma_db_dir, embedding_model):
    """
    Load serialized documents and populate a Chroma vector store.
    """
    fill_vector_store_func(pickle_file, chroma_db_dir, embedding_model)


if __name__ == "__main__":
    main()
