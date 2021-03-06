#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#     stringEcho.py
#
#     This file is part of the RoboEarth Cloud Engine framework.
#
#     This file was originally created for RoboEearth
#     http://www.roboearth.org/
#
#     The research leading to these results has received funding from
#     the European Union Seventh Framework Programme FP7/2007-2013 under
#     grant agreement no248942 RoboEarth.
#
#     Copyright 2012 RoboEarth
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
#     \author/s: Dominique Hunziker
#
#

import roslib; roslib.load_manifest('Test')
import rospy
from std_msgs.msg import String

from Test.srv import StringEcho


def string_echo_server():
    rospy.init_node('stringEchoNode')

    pub = rospy.Publisher('stringEchoResp', String, latch=True)
    rospy.Subscriber('stringEchoReq', String, pub.publish)
    rospy.Service('stringEchoService', StringEcho, lambda msg: msg.data)
    rospy.spin()


if __name__ == "__main__":
    string_echo_server()
