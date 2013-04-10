import pygame
import sys
from geometry_msgs.msg import Twist
import rospy

rospy.init_node('ranger_vw_ctrl')
twist = rospy.Publisher('/cmd_vel', Twist)

v = 0.0
w = 0.0

msg = Twist()

pygame.init()

done = False

clock = pygame.time.Clock()

pygame.joystick.init()
joystick_count = pygame.joystick.get_count()

if joystick_count == 0:
    print("Plug your joystick!")
    sys.exit(1)

joystick = pygame.joystick.Joystick(0)
joystick.init()

while done==False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.JOYBUTTONDOWN:
            print("Leaving now")
            done = True

    w = joystick.get_axis( 0 )
    v = -joystick.get_axis( 1 )

    # Limit to 20 frames per second
    clock.tick(20)

    print("V:%s      W:%s" % (v,w))

    msg.linear.x = v
    msg.angular.z = w
    twist.publish(msg)


pygame.quit ()

