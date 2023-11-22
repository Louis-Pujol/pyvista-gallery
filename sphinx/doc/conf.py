extensions = [
    'sphinx_gallery.gen_gallery',
    ]

sphinx_gallery_conf = {
     'examples_dirs': '../examples',   # path to your example scripts
     'gallery_dirs': 'auto_examples',  # path to where to save gallery generated output
     'image_scrapers': ('matplotlib', 'pyvista'),
}