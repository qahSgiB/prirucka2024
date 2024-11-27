import click

from prirucka2024.download_url import download_url as download_url_func
from prirucka2024.pdf_parser_raw import parse_pdf_raw as parse_pdf_raw_func
#from prirucka2024.pdf_parser import parse_pdf as parse_pdf_func


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
@click.argument("infile")
@click.argument("outfile")
def parse_pdf_raw(infile, outfile):
    """Force-parse the text content of a PDF file and save it to a text file."""

    parse_pdf_raw_func(infile, outfile)


#@main.command()
#@click.argument("infile")
#@click.argument("outfile")
#def parse_pdf(infile, outfile):
#    """Parse the text content of a PDF file and save it in a better fashion to a text file."""
#
#    parse_pdf_func(infile, outfile)


if __name__ == "__main__":
    main()
