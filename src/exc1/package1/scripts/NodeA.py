#!/usr/bin/env python3
import rospy
from std_msgs.msg import UInt16

#Constants
STEP_SIZE = 4
PUBLISH_RATE = 20

def publish_data(publisher):
    rate = rospy.Rate(PUBLISH_RATE)
    k = 1

    while not rospy.is_shutdown():
        publisher.publish(k)
        rospy.loginfo(f"Published data -> {k}")
        k += STEP_SIZE
        rate.sleep()

def init_publisher():
    rospy.init_node('node_a', anonymous=True)
    return rospy.Publisher("/wattman", UInt16, queue_size=100)

def main():
    publisher = init_publisher()
    publish_data(publisher=publisher)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass