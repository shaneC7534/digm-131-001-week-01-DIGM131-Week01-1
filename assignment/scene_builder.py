"""
DIGM 131 - Assignment 1: Procedural Scene Builder
==================================================

OBJECTIVE:
    Build a simple 3D scene in Maya using Python scripting.
    You will practice using maya.cmds to create and position geometry,
    and learn to use descriptive variable names.

REQUIREMENTS:
    1. Create a ground plane (a large, flat polygon plane).
    2. Create at least 5 objects in your scene.
    3. Use at least 2 different primitive types (e.g., cubes AND spheres,
       or cylinders AND cones, etc.).
    4. Position every object using descriptive variable names
       (e.g., house_x, tree_height -- NOT x1, h).
    5. Add comments explaining what each section of your code does.

GRADING CRITERIA:
    - [20%] Ground plane is created and scaled appropriately.
    - [30%] At least 5 objects are created using at least 2 primitive types.
    - [25%] All positions/sizes use descriptive variable names.
    - [15%] Code is commented clearly and thoroughly.
    - [10%] Scene is visually coherent (objects are placed intentionally,
            not overlapping randomly).

TIPS:
    - Run this script from Maya's Script Editor (Python tab).
    - Use maya.cmds.polyCube(), maya.cmds.polySphere(), maya.cmds.polyCylinder(),
      maya.cmds.polyCone(), maya.cmds.polyPlane(), etc.
    - Use maya.cmds.move(x, y, z, objectName) to position objects.
    - Use maya.cmds.scale(x, y, z, objectName) to resize objects.
    - Use maya.cmds.rename(oldName, newName) to give objects meaningful names.
"""

import maya.cmds as cmds

# ---------------------------------------------------------------------------
# Clear the scene so we start fresh each time the script runs.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# ---------------------------------------------------------------------------
# Ground Plane
# ---------------------------------------------------------------------------
# Descriptive variables for the ground plane dimensions and position.
ground_width = 50
ground_depth = 50
ground_y_position = 0

ground = cmds.polyPlane(
    name="ground_plane",
    width=ground_width,
    height=ground_depth,
    subdivisionsX=1,
    subdivisionsY=1,
)[0]
cmds.move(0, ground_y_position, 0, ground)

# ---------------------------------------------------------------------------
# Example Object 1 -- a simple building (cube)
# This is provided as an example. Study it, then add your own objects below.
# ---------------------------------------------------------------------------
building_width = 4
building_height = 6
building_depth = 4
building_x = -8
building_z = 5

building = cmds.polyCube(
    name="building_01",
    width=building_width,
    height=building_height,
    depth=building_depth,
)[0]
# Raise the building so its base sits on the ground plane.
cmds.move(building_x, building_height / 2.0, building_z, building)



# Ground Plane 
ground_width = 50
ground_depth = 50
ground = cmds.polyPlane(name ="ground_plane", width=ground_width, height=ground_depth)

# Object 1
building_1_width = 7
building_1_height = 6
building_1_depth = 5
building_1_x = -5
building_1_z = 5
building_1 = cmds.polyCube(name = "building_1", width=building_width , height=building_height, depth=building_depth)
cmds.move(building_x, building_height/2,building_z, building_1)

# ---------------------------------------------------------------------------
# TODO: Add Object 2
# Create a second object using a DIFFERENT primitive type than the cube above.
# Remember to:
#   - Use descriptive variable names for size and position.
#   - Name the object meaningfully with the 'name' parameter or cmds.rename().
#   - Position it so it sits on the ground (not floating or buried).
# ---------------------------------------------------------------------------
building_2_height = 8
building_2_x = 10
building_2_z = 3
building_2_radius = 3
building_2 = cmds.polyCylinder(name="building_2", height=building_2_height, radius = building_2_radius)
cmds.move(building_2_x, building_2_height/2, building_2_z, building_2)
# ---------------------------------------------------------------------------
# TODO: Add Object 3
# ---------------------------------------------------------------------------
building_3_width=5
building_3_height=10
building_3_depth=6
building_3_x=-10
building_3_z=-19
building_3 = cmds.polyCube(name="building_3",width=building_3_width,height=building_3_height,depth=building_3_depth)
cmds.move(building_3_x,building_3_height/2, building_3_z, building_3)

# ---------------------------------------------------------------------------
# TODO: Add Object 4
# ---------------------------------------------------------------------------

#Base of the First Lightpole
lightPole_1_Base_height = 4
lightPole_1_Base_radius = 0.5
lightPole_1_Base_x= 12
lightPole_1_Base_z= -6
lightPole_1_Base = cmds.polyCylinder(name="lightPole_1_Base", height = lightPole_1_Base_height, radius = lightPole_1_Base_radius)
cmds.move(lightPole_1_Base_x, lightPole_1_Base_height/2, lightPole_1_Base_z, lightPole_1_Base)

#the light itself
light_Source_radius = 0.7
#the light sources x and z coordinates will change with the lightpole's base for it to stay in one piece 
light_Source_x = lightPole_1_Base_x
light_Source_y = 4.57
light_Source_z = lightPole_1_Base_z
light_Source = cmds.polySphere(name="light_Source", radius= light_Source_radius)
cmds.move(light_Source_x, light_Source_y, light_Source_z, light_Source)

#the top part of the lightpole
lightPole_Top_height = 1
lightPole_Top_radius = 0.7

#the x and z coordinates use the light pole's base numbers for it to stay together 
lightPole_Top_x= lightPole_1_Base_x
lightPole_Top_y= 5.4
lightPoly_Top_z= lightPole_1_Base_z
lightPole_Top= cmds.polyCone(name = "lightPole_Cap", height= lightPole_Top_height, radius= lightPole_Top_radius)
cmds.move(lightPole_Top_x, lightPole_Top_y, lightPoly_Top_z, lightPole_Top)
# ---------------------------------------------------------------------------
# TODO: Add Object 5
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# TODO (Optional): Add more objects to make your scene more interesting!
# Consider: trees, lamp posts, fences, vehicles, animals, etc.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Frame All -- so the whole scene is visible in the viewport.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.viewFit(allObjects=True)
print("Scene built successfully!")
