import sys
import numpy as np
import py3d

sys.path.append("../Open3D/build/lib/")

print("Load a ply point cloud, print it, and render it")
pcd = py3d.read_point_cloud("/home/sanjeev309/Open3D/build/lib/TestData/fragment.ply")
print(pcd)
print(np.asarray(pcd.points))
py3d.draw_geometries([pcd])

print("Downsample the point cloud with a voxel of 0.05")
downpcd = py3d.voxel_down_sample(pcd, voxel_size=0.05)
py3d.draw_geometries([downpcd])

print("Recompute the normal of the downsampled point cloud")
py3d.estimate_normals(downpcd, search_param=py3d.KDTreeSearchParamHybrid(
    radius=0.1, max_nn=30))
py3d.draw_geometries([downpcd])
print("")

print("Load a polygon volume and use it to crop the original point cloud")
vol = py3d.read_selection_polygon_volume("/home/sanjeev309/Open3D/build/lib/TestData/Crop/cropped.json")
chair = vol.crop_point_cloud(pcd)
py3d.draw_geometries([chair])
print("")

print("Paint chair")
chair.paint_uniform_color([0, 0, 0])
py3d.draw_geometries([chair])
print("")
