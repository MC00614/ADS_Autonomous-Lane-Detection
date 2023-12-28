from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='lane_perception',
            executable='lane_perception',
            name='lane_perception'
        ),
        Node(
            package='path_planner',
            executable='path_planner',
            name='path_planner'
        ),
        Node(
            package='vehicle_controller',
            executable='vehicle_controller',
            name='vehicle_controller'
        )
    ])