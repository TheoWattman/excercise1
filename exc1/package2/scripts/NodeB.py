#!/usr/bin/env python3

import rospy
from std_msgs.msg import UInt16, Float32

def process_data(data):
    return data / 0.15

def callback(data, publisher):      # callback is ran when the node recieves a message
    rospy.loginfo(f"Recieved data -> {data.data}")  # Logs info to log file and console

    processedData = process_data(data.data)

    publisher.publish(processedData)

    rospy.loginfo(f"Published data -> {processedData}")  # Logs info to log file and console


def init_node_b():
    rospy.init_node("node_b", anonymous=True)      # Initialize nodeB, anynomous true handles cases were multiple instances of the same node might be running

    publisher = rospy.Publisher("/kthfs/result", Float32, queue_size=100)
    rospy.Subscriber("/wattman", UInt16, callback, callback_args=publisher) # Adds a subscription to the global topic "wattman" with data type unsigned integer 16 bits


def main():
    init_node_b()
    rospy.spin() # Stops python from exiting until node is closed

try:
    if __name__ == '__main__': 
        main()
except rospy.ROSInterruptException:
    pass