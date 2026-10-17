"""Check that the built homepage renders every publication in its category.

Usage: python scripts/check_publication_groups.py [public/index.html]
"""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
GROUPS = {
    "papers": "Quantum Computing Systems and Architecture",
    "other-papers": "Other Research",
}


class PublicationGroups(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sections = []
        self.links = {group: set() for group in GROUPS}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "section":
            self.sections.append(attrs.get("id"))
        if tag == "a" and self.sections and self.sections[-1] in GROUPS:
            path = urlparse(attrs.get("href", "")).path
            match = re.fullmatch(r"/publication/([^/]+)/?", path)
            if match:
                self.links[self.sections[-1]].add(match.group(1))

    def handle_endtag(self, tag):
        if tag == "section" and self.sections:
            self.sections.pop()


expected = {group: set() for group in GROUPS}
for paper in (ROOT / "content/publication").glob("*/index.md"):
    frontmatter = paper.read_text().split("---", 2)[1]
    categories = re.search(r"^categories:\s*\n((?:- .+\n)+)", frontmatter, re.M)
    assert categories, f"Missing categories: {paper}"
    values = categories.group(1).splitlines()
    groups = [group for group, category in GROUPS.items() if f"- {category}" in values]
    assert len(groups) == 1, f"Publication must belong to one homepage group: {paper}"
    expected[groups[0]].add(paper.parent.name)

parser = PublicationGroups()
parser.feed(Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / "public/index.html").read_text())
for group, slugs in expected.items():
    actual = parser.links[group]
    assert actual == slugs, (
        f"{group}: missing={sorted(slugs - actual)}, unexpected={sorted(actual - slugs)}"
    )
    print(f"{group}: {len(actual)} publications rendered correctly")
