import pyvista as pv
from pyvista import examples
import os


pv.OFF_SCREEN = True
pv.BUILDING_GALLERY = True
# os.environ['PYVISTA_BUILDING_GALLERY'] = 'true'


from pyvista.plotting.utilities.sphinx_gallery import generate_images, html_rst

#Create a basic python iterator
class MyIterator:
    def __init__(self, max):
        self.max = max
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            self.n += 1
            return str(self.n)
        else:
            raise StopIteration

iter = MyIterator(10)


mesh = examples.download_armadillo()
scalars = mesh.points[:, 1]
plotter = pv.Plotter()
plotter.add_mesh(mesh, scalars=scalars)
plotter.show()

figure_list = generate_images(iter, dynamic=True)

# html = html_rst(figure_list, sources_dir=".")
# print(html)

##########################################################


