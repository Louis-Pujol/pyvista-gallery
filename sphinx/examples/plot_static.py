"""
.. _static_example:

Static
~~~~~~
Simple example of a static plot with PyVista.


"""

import pyvista as pv


###############################################################################
# Create a mesh
#
sphere0 = pv.Sphere()

###############################################################################
# Setup the plotter open a movie, and write a frame after moving the sphere.
#

pl = pv.Plotter()
pl.add_mesh(sphere0, color="tan", show_edges=True)
pl.show()