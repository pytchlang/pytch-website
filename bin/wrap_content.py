import sys
import click
from bs4 import BeautifulSoup


header_html = """
<div class="NavBar">
  <a href="../app/"><h1>Pytch</h1></a>
  <ul>
    <a data-doc-root href="./index.html"><li>Help</li></a>
    <a href="../app/tutorials/"><li>Tutorials</li></a>
    <a href="../app/my-projects/"><li>My projects</li></a>
  </ul>
</div>
"""


@click.command()
@click.argument(
    "filename",
    type=click.Path(),
)
def main(filename):
    sys.stderr.write(f"Wrapping {filename}\n")
    with open(filename, "rt") as input_file:
        soup = BeautifulSoup(input_file, "html.parser")
    header_soup = BeautifulSoup(header_html, "html.parser")
    # TODO: Patch top-level doc root for things not at top level
    body_elt = soup.find("body", attrs={"class": "wy-body-for-nav"})
    body_elt.insert(0, header_soup)
    with open(filename, "wt") as output_file:
        output_file.write(str(soup))


if __name__ == "__main__":
    main()
