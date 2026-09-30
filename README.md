# Personal website

Static site: plain HTML and CSS, no build step.

## Publish on GitHub Pages
1. Create a repository named `mariossal.github.io` (replace mariossal with your GitHub username).
2. Upload every file in this folder to the root of the repository.
3. Settings > Pages > Source: Deploy from a branch, branch `main`, folder `/ (root)`.
4. Wait a minute, then open https://mariossal.github.io

## Editing
Edit the HTML files directly. `style.css` holds all styling. Replace `cv.pdf`, `portrait.jpg` and `portrait-2.jpg` to update the CV and photos.
After choosing a custom domain, replace mariossal.github.io in `sitemap.xml` and `robots.txt` with the domain.

## Languages
English pages live at the root and are the source. Greek, Italian and Spanish pages are generated:
edit a translation in `i18n/translations.py`, then run `python3 i18n/translations.py && python3 i18n/build.py`.
Strings without a translation stay in English (publication titles, names, tool names).
