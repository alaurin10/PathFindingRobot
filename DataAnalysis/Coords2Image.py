import matplotlib.pyplot as plt
import numpy as np


# ------------------- Functions -------------------
# Function to find the max and min bounds of both x and y
def find_bounds(x, y):
    max_x = np.max(x)
    min_x = np.min(x)
    max_y = np.max(y)
    min_y = np.min(y)
    return max_x, min_x, max_y, min_y

# Function to find the index of the created image that most closely matches a value
def closest_index(input_list, input_value):
    arr = np.asarray(input_list)
    i = (np.abs(arr - input_value)).argmin()
    return i



# Read in contents of each txt file. Split coordnites into a nested list
object1 = [x.split() for x in open('OBJ01_pts.txt').read().split('\n') if x != '']
object1 = [list(map(float, lst)) for lst in object1]

object2 = [x.split() for x in open('OBJ02_pts.txt').read().split('\n') if x != '']
object2 = [list(map(float, lst)) for lst in object2]


# Create x and y coords from index 0 and 2 of the lists. Index 1 is unused
x = []
y = []
for i in range(len(object1)):
    x.append(object1[i][0])
    y.append(object1[i][2])
    

resolution = 100    # Define the resolution of the new image
x_max, x_min, y_max, y_min = find_bounds(x, y)  # Find max and min bounds

# Create rows and columns that start and end at min and max of x and y
# Rows and columns have n equaly spaced points in between where n is resolution
cols_locations = np.arange(x_min, x_max, (x_max - x_min)/resolution)
rows_locations = np.arange(y_min, y_max, (y_max - y_min)/resolution)

# Create temporary image array of zeros
image = np.zeros((resolution,resolution))

# Match each xy value with the row, col index that most closely matches their value
for coord in range(len(x)):
    row_pos = closest_index(rows_locations, y[coord])
    col_pos = closest_index(cols_locations, x[coord])
    image[row_pos][col_pos] = 1     # Set this pixel to 1


# Plot the x,y coords of room 1 in a new figure
plt.figure()
plt.plot(x,y)
plt.title('Room 2')
plt.show()  # Show both figures

# Display binary image
plt.figure()
plt.imshow(image, cmap='Greys')
