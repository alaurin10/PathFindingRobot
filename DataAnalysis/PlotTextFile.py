import matplotlib.pyplot as plt

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

# Plot the x,y coords of room 1 in a new figure
plt.figure()
plt.plot(x,y)
plt.plot([1, -1, -1, 1, 1], [1, 1, -1, -1, 1]) # Add box to center of figure
plt.title('Room 1')


# Create x and y coords from index 0 and 2 of the lists. Index 1 is unused
x = []
y = []
for i in range(len(object2)):
    x.append(object2[i][0])
    y.append(object2[i][2])

# Plot the x,y coords of room 1 in a new figure
plt.figure()
plt.plot(x,y)
plt.title('Room 2')
plt.show()  # Show both figures
