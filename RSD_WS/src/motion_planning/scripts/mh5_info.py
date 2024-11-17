#!/usr/bin/env python
import sys #the line above is called a shebang and it is responsible for helping ROS idntify a ROS script
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

rospy.init_node('motoman_info' , anonymous=True) #Initialising program as ros node

moveit_commander.roscpp_initialize(sys.argv) #Initializing communication with moveit

#Defining objects: A robot, A world and a set of joints is needed
robot= moveit_commander.RobotCommander() #robot object
scene= moveit_commander.PlanningSceneInterface() #world object (called scene in robotics)
group= moveit_commander.MoveGroupCommander("mh5") #Set of joints I had defined under group mh5 while setting up


motoman_joint_vals= group.get_current_joint_values() #gets current values of joints (in rad)
motoman_pose= group.get_current_pose() #gets current position in x,y,z (in m)
print("Joint Values:",motoman_joint_vals)
print("Position:", motoman_pose)

rospy.sleep(10) #wait 10s
moveit_commander.roscpp_shutdown() #break communication with moveit