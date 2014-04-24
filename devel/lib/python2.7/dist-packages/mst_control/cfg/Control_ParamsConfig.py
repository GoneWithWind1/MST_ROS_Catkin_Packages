## *********************************************************
## 
## File autogenerated for the mst_control package 
## by the dynamic_reconfigure package.
## Please do not edit.
## 
## ********************************************************/

##**********************************************************
## Software License Agreement (BSD License)
##
##  Copyright (c) 2008, Willow Garage, Inc.
##  All rights reserved.
##
##  Redistribution and use in source and binary forms, with or without
##  modification, are permitted provided that the following conditions
##  are met:
##
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above
##     copyright notice, this list of conditions and the following
##     disclaimer in the documentation and/or other materials provided
##     with the distribution.
##   * Neither the name of the Willow Garage nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
##  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
##  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
##  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
##  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
##  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
##  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
##  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
##  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
##  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
##  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
##  POSSIBILITY OF SUCH DAMAGE.
##**********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 233, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 262, 'description': 'max robot speed in lineardirection', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'base_linear_speed', 'edit_method': '', 'default': 1.0, 'level': 1, 'min': 0.0, 'type': 'double'}, {'srcline': 262, 'description': 'max robot speed in angular direction', 'max': 4.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'base_rot_speed', 'edit_method': '', 'default': 1.0, 'level': 1, 'min': 0.0, 'type': 'double'}, {'srcline': 262, 'description': 'multiplyer of turbo button x', 'max': 5.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'turbo_x', 'edit_method': '', 'default': 1.5, 'level': 1, 'min': 0.0, 'type': 'double'}, {'srcline': 262, 'description': 'multiplyer of turbo button y', 'max': 5.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'turbo_y', 'edit_method': '', 'default': 2.0, 'level': 1, 'min': 0.0, 'type': 'double'}, {'srcline': 262, 'description': 'the percent that the dpad is scaled down', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'd_pad_percent', 'edit_method': '', 'default': 50.0, 'level': 1, 'min': 0.0, 'type': 'double'}, {'srcline': 262, 'description': 'phrase to say when plus button is pressed', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'plus_mesage', 'edit_method': '', 'default': 'Pardon me. coming through.', 'level': 1, 'min': '', 'type': 'str'}, {'srcline': 262, 'description': 'sound to play when minus button is pressed', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'minus_sound', 'edit_method': '', 'default': '/home/robot/Documents/Joemegatron_IGVC_2011/sounds/Ahooga_Car_Horn.wav', 'level': 1, 'min': '', 'type': 'str'}, {'srcline': 262, 'description': '.yaml file with autonomous waypoints', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'autonomous_waypoints', 'edit_method': '', 'default': '/home/robot/Documents/Joemegatron_IGVC_2011/yaml/Autonomous_Waypoints.yaml', 'level': 1, 'min': '', 'type': 'str'}, {'srcline': 262, 'description': '.yaml file with autonomous waypoints', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'navigation_waypoints', 'edit_method': '', 'default': '/home/robot/Documents/Joemegatron_IGVC_2011/yaml/Navigation_Waypoints.yaml', 'level': 1, 'min': '', 'type': 'str'}, {'srcline': 262, 'description': 'sound to play when minus button is pressed', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'waypoint_sound', 'edit_method': '', 'default': '/home/robot/Documents/Joemegatron_IGVC_2011/sounds/Ahooga_Car_Horn.wav', 'level': 1, 'min': '', 'type': 'str'}, {'srcline': 262, 'description': 'sound to play when minus button is pressed', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'done_sound', 'edit_method': '', 'default': '/home/robot/Documents/Joemegatron_IGVC_2011/sounds/Ahooga_Car_Horn.wav', 'level': 1, 'min': '', 'type': 'str'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])    
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

