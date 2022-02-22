#!/usr/bin/env python
import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    pub = rospy.Publisher("chatter", String, queue_size=10)
    rospy.init_node("talker")
    rate = rospy.Rate(10)
    
    while not rospy.is.shutdown():
        hello_str = "This is my first ros message %s" % rospy.get_time()
        pub.publish(hello_str)
        
        rate.sleep()
