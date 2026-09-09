# Repository Guidelines

## Adding Publications

Publication content lives in `content/publication/<slug>/index.md`. Use a lowercase
slug in the form `<first-author-surname>-<year>-<short-name>`, for example
`zhao-2025-class`.

When adding a publication, copy the front matter structure from the most recent
similar entry (conference or journal) and follow these rules:

- Set `title` to the official paper title.
- List authors in publication order under `authors`. Use `admin` for Zhao Yilun so
  the site links and highlights the local author profile.
- Add `author_notes` only when the paper explicitly identifies equal contribution
  or another author note. Its entries correspond to authors by position.
- Use a full ISO 8601 value for `date` and `publishDate`. `date` controls publication
  ordering; do not invent a precise day when only a year is known.
- Use CSL types in `publication_types`: `paper-conference` for conference papers and
  `article-journal` for journal articles.
- Put the official venue text in `publication` and wrap it in `*...*`. Put the venue
  abbreviation in `publication_short` when one is commonly used.
- Include acceptance rates, award status, or candidate status only when verified.
- Keep `abstract`, `summary`, `tags`, `projects`, and `slides` empty unless content
  is explicitly provided.
- Set `featured` deliberately. It does not control whether the homepage collection
  includes the publication.

## Publication Links and Files

- Every publication must include its verified official publisher URL in a custom
  `links` block using the same URL label and link icon:

  ```yaml
  links:
  - icon: link
    icon_pack: fas
    name: URL
    url: "https://publisher.example/paper"
  ```

- Prefer the canonical DOI URL or the publisher's article page. Do not populate the
  `doi` field; the official URL belongs only in the `links` block so the site uses a
  consistent URL icon rather than a DOI badge.
- Do not add an empty `url_pdf` field.
- When a PDF file is available, place it beside `index.md`, name it after the slug
  (for example `zhao-2025-class.pdf`), and set `url_pdf` to that filename.
- Use `url_code` only for the paper's public source repository. Leave the other
  `url_*` fields empty unless a real, public resource exists.
- Never label a publisher landing page as a PDF. If no PDF is available, omit
  `url_pdf`.
- Do not add placeholder links or fabricate metadata.

## Images and Validation

- Add `featured.jpg` or `featured.png` beside `index.md` only when a publication
  image is supplied. Keep the standard `image` configuration otherwise.
- Preserve the YAML front matter delimiters and existing formatting style.
- Before finishing, run `git diff --check` and, when Hugo is installed, build with
  the Hugo version specified in `netlify.toml`.
