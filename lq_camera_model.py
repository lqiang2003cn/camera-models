import matplotlib.pyplot as plt
import numpy as np

from camera_models import *  # our package

DECIMALS = 2  # how many decimal places to use in print

X = np.array([4.0, 2.0, 3.0])
print(f"X: {X}")
Xh = to_homogeneus(X)
print(f"X in homogeneous coordinates: {Xh}")

Xh = np.array([8.0, 4.0, 6.0, 2.0])
print(f"X in homogeneous coordinates: {Xh}")
X = to_inhomogeneus(Xh)
print(f"X: {X}")

###############################################################################
fig = plt.figure()
ax = fig.add_subplot(2, 2, 1, projection="3d")
Rx = get_rotation_matrix(theta_x=np.pi / 2.0)  # Roll
Ry = get_rotation_matrix(theta_y=np.pi / 2.0)  # Pitch
Rz = get_rotation_matrix(theta_z=np.pi / 2.0)  # Yaw
world_origin = np.zeros(3)
dx, dy, dz = np.eye(3)
world_frame = ReferenceFrame(
    origin=world_origin,
    dx=dx,
    dy=dy,
    dz=dz,
    name="World",
)
roll_frame = ReferenceFrame(
    origin=np.zeros(3),
    dx=Rx @ dx,
    dy=Rx @ dy,
    dz=Rx @ dz,
    name="Camera",
)
pitch_frame = ReferenceFrame(
    origin=np.zeros(3),
    dx=Ry @ dx,
    dy=Ry @ dy,
    dz=Ry @ dz,
    name="Camera",
)
yaw_frame = ReferenceFrame(
    origin=np.zeros(3),
    dx=Rz @ dx,
    dy=Rz @ dy,
    dz=Rz @ dz,
    name="Camera",
)
world_frame.draw3d(ax=ax)
set_xyzlim3d(-1, 1, ax=ax)
set_xyzticks([], ax=ax)
ax.set_title(f"No Rotation")

ax = fig.add_subplot(2, 2, 2, projection="3d")
roll_frame.draw3d(ax=ax)
set_xyzlim3d(-1, 1, ax=ax)
ax.set_title(f"Roll (90°)")
set_xyzticks([], ax=ax)

ax = fig.add_subplot(2, 2, 3, projection="3d")
pitch_frame.draw3d(ax=ax)
set_xyzlim3d(-1, 1, ax=ax)
set_xyzticks([], ax=ax)
ax.set_title(f"Pitch (90°)")

ax = fig.add_subplot(2, 2, 4, projection="3d")
yaw_frame.draw3d(ax=ax)
set_xyzlim3d(-1, 1, ax=ax)
set_xyzticks([], ax=ax)
ax.set_title(f"Yaw (90°)")
fig.suptitle("Camera Rotation")
plt.tight_layout()
plt.show()

###############################################################################
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
world_origin = np.zeros(3)
dx, dy, dz = np.eye(3)
t = np.array([3, -4, 2])  # camera's translation in world
world_frame = ReferenceFrame(
    origin=world_origin,
    dx=dx,
    dy=dy,
    dz=dz,
    name="World",
)
camera_frame = ReferenceFrame(
    origin=t,
    dx=dx,
    dy=dy,
    dz=dz,
    name="Camera",
)
world_frame.draw3d(ax=ax)
camera_frame.draw3d(ax=ax)
# arrow from point world_origin to point t
draw3d_arrow(world_origin, t, color="tab:red", name="t", ax=ax)
set_xyzlim3d(-5, 5, ax=ax)
# ax.set_title(f"Camera Translation (t = {t})")
# plt.tight_layout()
# plt.show()


###############################################################################
F = 3.0  # focal length
PX = 2.0  # principal point x-coordinate
PY = 1.0  # principal point y-coordinate
THETA_X = np.pi / 2  # roll angle
# THETA_Y = np.pi / 2
THETA_Z = np.pi  # yaw angle
C = np.array([3, -5, 2])  # camera centre
IMAGE_HEIGTH = 4
IMAGE_WIDTH = 6

R = get_rotation_matrix(theta_x=THETA_X,  theta_z=THETA_Z)
world_origin = np.zeros(3)
dx, dy, dz = np.eye(3)
world_frame = ReferenceFrame(
    origin=world_origin,
    dx=dx,
    dy=dy,
    dz=dz,
    name="World",
)
camera_frame = ReferenceFrame(
    origin=C,
    dx=R @ dx,
    dy=R @ dy,
    dz=R @ dz,
    name="Camera",
)
Z = PrincipalAxis(
    camera_center=camera_frame.origin,
    camera_dz=camera_frame.dz,
    f=F,
)
image_frame = ReferenceFrame(
    origin=Z.p - camera_frame.dx * PX - camera_frame.dy * PY,
    dx=R @ dx,
    dy=R @ dy,
    dz=R @ dz,
    name="Image",
)
image_plane = ImagePlane(
    origin=image_frame.origin,
    dx=image_frame.dx,
    dy=image_frame.dy,
    heigth=IMAGE_HEIGTH,
    width=IMAGE_WIDTH,
)
fig = plt.figure(figsize=(6, 6))
ax = plt.axes(projection="3d")
ax.text(*C, "C")
world_frame.draw3d(ax=ax)
camera_frame.draw3d(ax=ax)
image_frame.draw3d(ax=ax)
Z.draw3d(ax=ax)
image_plane.draw3d(ax=ax)
ax.view_init(elev=30.0, azim=30.0)
ax.set_title("Pinhole Camera Geometry")
plt.tight_layout()
plt.show()
