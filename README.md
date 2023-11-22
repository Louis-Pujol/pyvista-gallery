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
mkdocs serve
```

## TODO :
- [x] Create a gallery with `sphinx-gallery` with a static pyvista plot 
- [x] Create a gallery with `sphinx-gallery` with a pyvista animation
- [] understand how `pyvista.plotting.utilities.sphinx_gallery.Scraper` works
