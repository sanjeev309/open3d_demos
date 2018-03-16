import sys
import py3d
import matplotlib.pyplot as plt

sys.path.append("../Open3D/build/lib/")

print("Read Redwood dataset")
color_raw = py3d.read_image("/home/sanjeev309/Open3D/build/lib/TestData/RGBD/color/00000.jpg")
depth_raw = py3d.read_image("/home/sanjeev309/Open3D/build/lib/TestData/RGBD/depth/00000.png")
rgbd_image = py3d.create_rgbd_image_from_color_and_depth(
        color_raw, depth_raw);
print(rgbd_image)
plt.subplot(1, 2, 1)
plt.title('Redwood grayscale image')
plt.imshow(rgbd_image.color)
plt.subplot(1, 2, 2)
plt.title('Redwood depth image')
plt.imshow(rgbd_image.depth)
plt.show()
pcd = py3d.create_point_cloud_from_rgbd_image(rgbd_image,
                                              py3d.PinholeCameraIntrinsic.prime_sense_default)
# Flip it, otherwise the pointcloud will be upside down
pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
py3d.draw_geometries([pcd])
print("Writing ply file")
py3d.write_point_cloud("Redwood.ply", pcd)
