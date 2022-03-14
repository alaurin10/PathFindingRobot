import matplotlib.pyplot as plt
import Coords2Image

# Display binary image converted from the coordinates
resolution = 30
image = Coords2Image.Convert2Image('OBJ01_pts.txt', resolution)

current_pos = (1,1)
final_pos = (resolution-2,resolution-2)

# Function to generate the coordinates of all 8 cells around the current cell
def GetCoords(curr_pos):
    F = (curr_pos[0]+1, curr_pos[1]+0)
    FR = (curr_pos[0]+1, curr_pos[1]-1)
    FL = (curr_pos[0]+1, curr_pos[1]+1)
    R = (curr_pos[0]+0, curr_pos[1]-1)
    L = (curr_pos[0]+0, curr_pos[1]+1)
    B = (curr_pos[0]-1, curr_pos[1]+0)
    BR = (curr_pos[0]-1, curr_pos[1]-1)
    BL = (curr_pos[0]-1, curr_pos[1]+1)

    return F, FR,FL, R, L, B, BR, BL

# Function to decide which cell the robot should move to next
def NextCell(curr_pos):

    (F, FR,FL, R, L, B, BR, BL) = GetCoords(curr_pos)

    new_pos = curr_pos

    # If obstacle is F, L, and FL, move back to previous position
    if image[F] and image[L] and image[FL]:
        new_pos = B

    # If obstacle is F and L, move back to previous position
    elif image[F] and image[L]:
        new_pos = B

    # If obstacle is L and FL, move F
    elif image[L] and image[FL]:
        new_pos = F

    # If obstacle is F and FL, move L
    elif image[F] and image[FL]:
        new_pos = L

    # If obstacle is F (forward), move L (left)
    elif image[F]:
        new_pos = L

    # If obstacle is L (left), move F (forward)
    elif image[L]:
        new_pos = F

    # If obstacle is FL (diagonal), move F or L
    # Move the direction that is furthest from the goal
    elif image[FL]:
        if curr_pos[0] < curr_pos[1]:
            new_pos = F
        else:
            new_pos = L

    # If no obstacle present, move FL (diagonally)
    else:
        new_pos = FL

    return new_pos


# Loop path planning algorithm until desitination has been reached
while True:

    # Plot the current cell and display the grid
    image[current_pos] = 2  
    plt.figure()
    plt.imshow(image)
    plt.show()
    print(current_pos)

    # When the destination has been reached, break the loop
    if current_pos == final_pos:
        print("Path Complete!")
        break

    previous_pos = current_pos
    current_pos = NextCell(current_pos)

