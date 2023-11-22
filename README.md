# pyvista-gallery

Integrate pyvista plotters in sphinx-gallery/mkdocs-gallery

## Build documentation
 
- with `sphinx`
```bash
cd sphinx
pip install -r requirements.txt
make html
firefox build/html/index.html
```

- with `mkdocs`
```bash
cd mkdocs
pip install -r requirements.txt
bash serve.sh
```

## TODO :
- [x] Create a gallery with `sphinx-gallery` with a static pyvista plot 
- [x] Create a gallery with `sphinx-gallery` with a pyvista animation
- [x] Understand how `pyvista.plotting.utilities.sphinx_gallery.Scraper` works
- [x] Write a pyvista scraper in `mkdocs-gallery`
- [x] Replicate static/animated examples with pyvista
