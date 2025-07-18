import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Circle


def physics(velocity, angle, frames = 100):
    display_array = np.zeros((128, 128))

    display_array = np.stack((display_array, np.zeros((128, 128))))
    display_array = np.concatenate((display_array, np.zeros((1, 128, 128))), axis=0).astype(np.uint8)
    display_array = np.transpose(display_array, (1, 2, 0))

    def kick(velocity, angle, frames = frames, display_array = display_array):
        angle = np.radians(angle)
        x_distance = 2
        y_distance = 2
        y_velocity = velocity * np.sin(angle)
        x_velocity = velocity * np.cos(angle)
        time = (2 * velocity * np.sin(angle) / 9.81) / frames

        fig, ax = plt.subplots()
        circle = Circle((x_distance, 127 - y_distance), radius = 2, facecolor='red', edgecolor='red')
        ax.add_patch(circle)
        ax.imshow(display_array)
        plt.show()

        for frame in range(frames):
            x_distance = x_distance + time * x_velocity
            y_distance = y_distance + time * y_velocity - (9.81 * (time) ** 2 / 2)
            y_velocity = y_velocity - (9.81 * (time))
            x_velocity = x_velocity - (0 * (time))
            fig, ax = plt.subplots()
            circle = Circle((x_distance, 127 - y_distance), radius = 2, facecolor='red', edgecolor='red')
            ax.add_patch(circle)
            ax.imshow(display_array)
            plt.show()
        return x_velocity, x_distance, y_distance

    def floor_motion(x_velocity, x_distance, y_distance, frames = frames, display_array = display_array):

        time = x_velocity / (9.81 * 0.43) / frames
        for frame in range(frames + 1):
            x_distance = x_distance + x_velocity * (time) - (9.81 * 0.43 * (time) ** 2 / 2)
            x_velocity = x_velocity - (9.81 * 0.43 * (time))
            fig, ax = plt.subplots()
            circle = Circle((x_distance, 127 - y_distance), radius = 2, facecolor='red', edgecolor='red')
            ax.add_patch(circle)
            ax.imshow(display_array)
            plt.show()
            print(int(y_distance))

    x_velocity, x_distance, y_distance = kick(velocity=velocity, angle=angle, frames=frames)
    floor_motion(x_velocity, x_distance, y_distance)

physics(20, 45, frames = 40)