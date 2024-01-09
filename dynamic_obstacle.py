
# dynamic_obstacle.py

import rclpy
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Float32
import random

class DynamicObstacle:
    def __init__(self):
        self.obstacle_position = Pose2D()
        self.obstacle_speed = 1.0
        self.obstacle_direction = 1

    def update_obstacle_position(self):
        # Update obstacle position based on speed and direction
        self.obstacle_position.x += self.obstacle_speed
        if self.obstacle_position.x > 10 or self.obstacle_position.x < 0:
            self.obstacle_direction *= -1
            self.obstacle_speed = random.uniform(0.5, 1.5)
        self.obstacle_position.y += self.obstacle_speed * self.obstacle_direction

    def publish_obstacle_position(self):
        # Publish obstacle position
        obstacle_position_publisher = self.create_publisher(Pose2D, 'obstacle_position', 10)
        obstacle_position_publisher.publish(self.obstacle_position)

    def obstacle_speed_callback(self, msg):
        # Update obstacle speed based on received message
        self.obstacle_speed = msg.data

def main(args=None):
    rclpy.init(args=args)
    dynamic_obstacle = DynamicObstacle()
    node = rclpy.create_node('dynamic_obstacle')

    # Create a subscriber to receive speed updates
    obstacle_speed_subscription = node.create_subscription(Float32, 'obstacle_speed', dynamic_obstacle.obstacle_speed_callback, 10)

    # Use a timer to update and publish obstacle position
    timer = node.create_timer(0.1, dynamic_obstacle.update_obstacle_position)

    rclpy.spin(node)

    dynamic_obstacle.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
