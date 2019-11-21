#!/home/robot/.pyenv/versions/ros_py36/bin/python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class SelfDrive:
    def __init__(self, publisher):
        self.publisher = publisher
        self.count = 0

    def lds_callback(self, scan):
        # scan 분석 후 속도 결정
        # ...
        print("scan[0]:", scan.ranges[0])
        print("scan[270]:", scan.ranges[60])
        turtle_vel = Twist()
        rate = rospy.Rate(3)

        turtle_vel.linear.x = 0.25
        self.publisher.publish(turtle_vel)
        if scan.ranges[0] <= 0.25:
            turtle_vel.linear.x = 0.0
            turtle_vel.angular.z = -1.5
            self.publisher.publish(turtle_vel)
            rate.sleep()
        if scan.ranges[25] <= 0.15:
            turtle_vel.linear.x = 0.0
            turtle_vel.angular.z = -1.5
        if scan.ranges[335] <= 0.15:
            turtle_vel.linear.x = 0.0
            turtle_vel.angular.z = 1.5


        self.publisher.publish(turtle_vel)






def main():
    rospy.init_node('self_drive')
    publisher = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    driver = SelfDrive(publisher)
    subscriber = rospy.Subscriber('scan', LaserScan,
                                  lambda scan: driver.lds_callback(scan))
    rospy.spin()

if __name__ == "__main__":
    main()
