import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    # 1. Lấy đường dẫn đến package và file xacro
    pkg_path = get_package_share_directory('my_robot_description')
    xacro_file = os.path.join(pkg_path, 'urdf', 'robot.urdf.xacro')
    
    # 2. Xử lý file Xacro thành chuỗi XML URDF
    robot_description_raw = xacro.process_file(xacro_file).toxml()

    # 3. Trả về cấu trúc LaunchDescription chứa các Node
    return LaunchDescription([
        # Node 1: robot_state_publisher (Đọc URDF, phát TF)
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description_raw}]
        ), # <--- Chú ý phải có dấu phẩy ở đây để ngăn cách các Node

        # Node 2: joint_state_publisher_gui (Bảng slider điều khiển khớp)
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        ), # <--- Chú ý phải có dấu phẩy ở đây

        # Node 3: rviz2 (Hiển thị 3D)
        Node(
            package='rviz2',
            executable='rviz2',
            output='screen'
        )
    ])
