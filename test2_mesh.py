import sys
import numpy as np
import py3d
import copy

sys.path.append("../Open3D/build/lib/")

print("Testing mesh in py3d ...")
mesh = py3d.read_triangle_mesh("/home/sanjeev309/Open3D/build/lib/TestData/knot.ply")
print(mesh)
print(np.asarray(mesh.vertices))
print(np.asarray(mesh.triangles))
print("")


print("Try to render a mesh with normals (exist: " + str(mesh.has_vertex_normals()) + ") and colors (exist: " + str(mesh.has_vertex_colors()) + ")")
py3d.draw_geometries([mesh])
print("A mesh with no normals and no colors does not seem good.")


print("Computing normal and rendering it.")
mesh.compute_vertex_normals()
print(np.asarray(mesh.triangle_normals))
py3d.draw_geometries([mesh])


print("We make a partial mesh of only the first half triangles.")
mesh1 = copy.deepcopy(mesh)
mesh1.triangles = py3d.Vector3iVector(
        np.asarray(mesh1.triangles)[:len(mesh1.triangles)//2, :])
mesh1.triangle_normals = py3d.Vector3dVector(
        np.asarray(mesh1.triangle_normals)
        [:len(mesh1.triangle_normals)//2, :])
print(mesh1.triangles)
py3d.draw_geometries([mesh1])


print("Painting the mesh")
mesh1.paint_uniform_color([1, 0.706, 0])
py3d.draw_geometries([mesh1])
