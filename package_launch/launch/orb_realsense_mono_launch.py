from launch import LaunchDescription
from launch_ros.actions import Node
import ament_index_python.packages

import os


def generate_launch_description():
  config_settings = os.path.join( ament_index_python.packages.get_package_share_directory('orbslam3'),
    'config','monocular','EuRoC.yaml')
  
  config_voc = os.path.join( ament_index_python.packages.get_package_share_directory('orbslam3'),
    'vocabulary','ORBvoc.txt')
  
  

  # params = os.path.join(config_directory, 'zed_f9p.yaml')

  return LaunchDescription([
      # Node(
      #     package='package_launch',
      #     executable='cam2img',
      #     name='cam2img',
      #     output='screen',
      # ),
      Node(
          package='orbslam3',
          executable='mono',
          name='mono',
          output='screen',
          arguments=[
              # config_voc,
              "/home/lemonx/it/nomad_software/nomad_core/ROS2_ORB-SLAM3_Odometry/orbslam3_ros2/vocabulary/ORBvoc.txt",
              "/home/lemonx/it/nomad_software/nomad_core/ROS2_ORB-SLAM3_Odometry/orbslam3_ros2/config/monocular/EuRoC.yaml",
              "use_sim_time:=True"
              # config_settings,
          ],
          remappings=[
              ('/camera', '/camera_left/image_raw'),
              ('/odom', '/odom_camera'),
          ]
      )
      # Node(
      #     package='tf2_ros',
      #     executable='static_transform_publisher',
      #     name='base_to_camera_tf',
      #     arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'camera_link']
      # )
  ])
