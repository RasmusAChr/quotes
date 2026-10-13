# Quotes

A tiny static site for collecting quotes. The site itself is read-only; quotes live in
`quotes.json`, and only people with push access to this repo (you) can add them.

## Add a quote

```sh
./add.py "The quote text" "Source"
git commit -am "Add quote" && git push
```

Or run `./add.py` with no arguments to be prompted. You can also edit `quotes.json`
directly, including from GitHub's web editor on your phone.

## Preview locally

```sh
python3 -m http.server
# open http://localhost:8000
```

## Deploy (GitHub Pages)

```sh
git init && git add . && git commit -m "Initial commit"
gh repo create quotes --public --source=. --push
gh api -X POST repos/RasmusAChr/quotes/pages -f "source[branch]=main" -f "source[path]=/"
```

The site will be at `https://rasmusachr.github.io/quotes/`.
Any static host (Netlify, Cloudflare Pages) works the same way — just point it at this folder.
