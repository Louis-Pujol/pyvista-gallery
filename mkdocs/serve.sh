pip uninstall -y mkdocs-gallery
python -m pip install 'mkdocs-gallery @ git+https://github.com/Louis-Pujol/mkdocs-gallery.git@main'

for folder in "docs/generated/" "docs/__pycache__/"
do
    # Check if the folder exists
    if [ -d "$folder" ]; then
        # Remove the folder
        rm -rf "$folder"
    fi
done

mkdocs serve