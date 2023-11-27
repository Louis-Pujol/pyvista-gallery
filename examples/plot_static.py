"""

Static
======
Visualize a static plot with PyVista.

"""

import pyvista as pv


# %%
# Load a mesh.
sphere = pv.Sphere()


# %%
# Plot the mesh.

pl = pv.Plotter()
pl.add_mesh(sphere, color="tan", show_edges=True)
pl.show()

# %%
# Print some infos about PyVista

print(f"OFF_SCREEN : {pv.OFF_SCREEN}")
print(f"BUILDING_GALLERY : {pv.BUILDING_GALLERY}")

