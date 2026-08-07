# Personal Site — Project Structure

```
personal-site/
├── index.html      → homepage markup and content (the diary entries)
├── blog_template/
│   └── blog.html   → placeholder template for individual blog entries
├── blog_entries/
├── css/
│   └── style.css   → all styling, colors, fonts, spacing
│   └── blog.css    → all styling for individual blog entries
└── js/
    └── main.js     → theme toggle + hero word animation
```

## How to preview it

Open `index.html` directly in a browser, or run a tiny local server from
this folder (recommended, avoids some browser file-loading quirks):

```
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Editing content (text, entries, links)

All content lives in `index.html`.

- **To edit an entry**: find its `<div class="entry">` block and change
  the date, title, or description text.
- **To add an entry**: copy an existing `<div class="entry">...</div>`
  block within the diary you want, paste it above or below the others,
  and edit the text. Newest entries should go first.
- **To add a brand-new diary** (a 6th category): copy an entire
  `<div class="diary" data-cat="...">...</div>` block, give it a new
  `data-cat` value (e.g. `data-cat="music"`), and add matching colors
  for it in `style.css` (see below).
- **To change nav links or footer links**: edit the `<nav>` and
  `<footer>` sections near the top and bottom of `index.html`.

## Editing the theme (colors, fonts, spacing)

All visual styling lives in `css/style.css`, and the file is organized
into labeled sections in this order: tokens, base, header, hero,
diaries, footer, responsive.

- **Colors**: everything is driven by CSS variables defined at the top
  of the file, under `:root` (light mode) and `html.dark` (dark mode).
  Change a variable once and it updates everywhere it's used.
- **Diary accent colors**: each diary category has its own accent
  color (`--terracotta`, `--olive`, `--umber`, `--rose`, `--gold`).
  These are wired to categories near the bottom of the file, under
  "per-diary accent colors" — match the `data-cat` value from
  `index.html` to a color variable.
- **Fonts**: three font families are loaded via Google Fonts in
  `index.html`'s `<head>` — Fraunces (serif, headings), Work Sans
  (sans-serif, body), and IBM Plex Mono (dates, labels, tags). Swap
  the Google Fonts link and the `font-family` values in `style.css`
  to change them.
- **Spacing / density**: look for `padding`, `margin`, and `gap`
  values in each section of `style.css`.

## Editing behavior

`js/main.js` has two small, independent pieces:

- Theme toggle (click handler on the sun/moon button)
- Hero role-word rotation (edit the `roles` array to change the words)

Both are short and commented — safe to edit directly.

## Adding new pages

Right now `index.html` is the homepage only. Each diary's "OPEN DIARY"
link currently points to `#`. When you're ready to build a dedicated
page per diary (e.g. `writing.html`), copy `index.html` as a starting
point, keep the same `<link>` and `<script>` tags so it shares the
same `style.css` and `main.js`, then replace the `.diaries` section
with a full list of entries for that one diary.
