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
- [ ] Move examples folder outside of docs

```python
# Write
return [Path(relpath(Path(e), start=Path(rel_to_dir))).as_posix() for e in dir_or_list_of_dirs]
# instead of
return [Path(e).relative_to(Path(rel_to_dir)).as_posix() for e in dir_or_list_of_dirs]
```

in `mkdocs-gallery/src/mkdocs_gallery/plugin.py`, `l.348`

- [ ] add a vedo scraper

        
