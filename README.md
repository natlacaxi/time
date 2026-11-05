# TalcoTime

Horloges du monde personnalisables (7 ambiances de couleurs), PWA installable, hors-ligne.

- 7 affichages : analogique, flip, arcs, néon, digital, barres, en lettres, avec bande jour/nuit
- 24 modèles prêts à l'emploi + tes propres modèles (bouton « En modèle »)
- Plein écran immersif : glisse ← → pour changer de style, ↑ ↓ pour changer d'horloge (flèches du clavier aussi)
- Une quarantaine de réglages par horloge (police, épaisseur, séparateur, animation, surface, cadran…)
- Éditeur avec aperçu en direct, bouton « Surprends-moi »
- Favoris (horloges et modèles), recherche, tri, sauvegarde JSON
- Tout est stocké dans le localStorage du navigateur

Fichiers : `index.html`, `manifest.json`, `sw.js`, les icônes (`icon-*.png`, `favicon.*`),
`gen_icons.py` (régénère les icônes, demande Pillow), `serve.py` (`python serve.py`).

Déploiement : mets le dossier à la racine d'un dépôt GitHub Pages.

## Workflows (`.github/workflows/`)

- `deploy.yml` : déploie sur GitHub Pages à chaque push sur `main`
  (Réglages → Pages → Source : **GitHub Actions**)
- `check.yml` : vérifie `manifest.json`, le JavaScript et la présence des fichiers PWA
- `icons.yml` : lancement manuel, régénère les icônes avec Python
