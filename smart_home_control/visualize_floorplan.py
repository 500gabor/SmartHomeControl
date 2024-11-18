import matplotlib.pyplot as plt
import matplotlib.patches as patches
import itertools
import time
from enum import Enum
from smart_home_control.read_data import read_input_states

def visualize_floorplan():
    input_states = False
    class ColorEnum(Enum):
        RED = 0
        GREEN = 1
    counter = itertools.count()
    while input_states is False and next(counter) < 10:
        input_states = read_input_states()
        if not input_states:
            time.sleep(0.5)
    print(input_states, flush=True)

    # Create figure and axes
    fig, ax = plt.subplots(figsize=(10, 8))

    # Function to draw a room
    def draw_room(ax, xy, width, height, label, color='lightgrey'):
        rect = patches.Rectangle(xy, width, height, linewidth=2, edgecolor='black', facecolor=color)
        ax.add_patch(rect)
        ax.text(xy[0] + width/2, xy[1] + height/2, label, horizontalalignment='center', verticalalignment='center', fontsize=12, weight='bold')

    # Draw Rooms
    # Garage and Storage
    draw_room(ax, (0, 6), 5, 4, 'Garage')
    draw_room(ax, (0, 2), 5, 4, 'Storage')

    # Kitchen, Bathroom, Living Room, Bedrooms
    draw_room(ax, (5, 6), 5, 4, 'Kitchen')
    draw_room(ax, (5, 2), 5, 2, 'Bathroom')
    draw_room(ax, (10, 6), 6, 4, 'Living Room')
    draw_room(ax, (10, 2), 6, 2, 'Bedroom 1')
    # Draw Corridors to connect rooms
    draw_room(ax, (5, 4), 11, 2, 'Corridor')

    # Add devices as red dots
    camera, = ax.plot(0, 10, 'o', color=ColorEnum(input_states['DI0']).name, markersize=10, label='Camera')
    smart_outlet, = ax.plot(16, 3, 'o', color=ColorEnum(input_states['DI1']).name, markersize=10, label='Smart Power Outlet')
    smart_bulb, = ax.plot(7.5, 9, 'o', color=ColorEnum(input_states['DI2']).name, markersize=10, label='Smart Light Bulb')
    auto_shutter, = ax.plot(13, 10, 'o', color=ColorEnum(input_states['DI3']).name, markersize=10, label='Automatic Shutter')

    # Add hover text to the devices and change their size on hover
    def on_hover(event):
        # Reset marker sizes
        camera.set_markersize(10)
        smart_outlet.set_markersize(10)
        smart_bulb.set_markersize(10)
        auto_shutter.set_markersize(10)

        # Check if the mouse is over any of the devices
        if camera.contains(event)[0]:
            plt.gca().set_title('Camera', fontsize=12)
            camera.set_markersize(15)  # Make the camera icon bigger
        elif smart_outlet.contains(event)[0]:
            plt.gca().set_title('Smart Power Outlet', fontsize=12)
            smart_outlet.set_markersize(15)  # Make the smart outlet icon bigger
        elif smart_bulb.contains(event)[0]:
            plt.gca().set_title('Smart Light Bulb', fontsize=12)
            smart_bulb.set_markersize(15)  # Make the smart bulb icon bigger
        elif auto_shutter.contains(event)[0]:
            plt.gca().set_title('Automatic Shutter', fontsize=12)
            auto_shutter.set_markersize(15)  # Make the automatic shutter icon bigger
        else:
            plt.gca().set_title('')
        fig.canvas.draw()  # Force an update to redraw the title

    fig.canvas.mpl_connect('motion_notify_event', on_hover)

    # Set limits and aspect
    ax.set_xlim(-2, 20)
    ax.set_ylim(-2, 12)
    ax.set_aspect('equal')
    plt.axis('off')

    # Show plot
    plt.show()

# Example usage
if __name__ == "__main__":
    visualize_floorplan()
