from turtle import distance
import serial
import FindPath
from MoveRobot import Move
import numpy as np
import math
import time



def find_dist_angle(path):
    distances = []
    angles = []
    for i, point in enumerate(path):
        try:
            x1 = point[1]
            y1 = point[2]

            x2 = path[i+1][1]
            y2 = path[i+1][2]

            d = (((y2-y1)**2) + ((x2-x1)**2))**(1/2)
            distances.append(d)

            angle = math.atan2(y1 - y2, x2 - x1) * 180 / math.pi
            angles.append(angle)

        except IndexError:
            pass

    return distances, angles




def main():
    current_angle = 0

    robot = Move()

    while True:
        try:
            path = FindPath.find_path()
        except IndexError:
            continue
        else:
            run = input('Run this path? (y/n): ')
            if run == 'y':
                break
            else:
                continue

    distances, angles = find_dist_angle(path)
    first_flag = True
    for dist, angle in zip(distances, angles):

        rotation = angle - current_angle

        if rotation < 0:
            robot.turn_right(0.25, abs(rotation))
        elif rotation > 0:
            robot.turn_left(0.25, rotation)
        elif rotation == 0:
            pass
        current_angle = angle
        
        print(f'Rotation: {rotation}, Distance: {dist}')

        time.sleep(2)

        robot.move(0.5, dist)
        time.sleep(3)
        

if __name__ == '__main__':
    main()
