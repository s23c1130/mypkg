# SPDX-FileCopyrightText: 2024 Toki Makabe <s23c1130sm@s.chibakoudai.jp>
# SPDX-License-Identifier:BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    MousePointPub = launch_ros.actions.Node(
            package = 'mypkg',
            executable = 'MousePointPub',
            )

    listener = launch_ros.actions.Node(
            package = 'mypkg',
            executable = 'listener',
            output = 'screen'
            )

    return launch.LaunchDescription([MousePointPub, listener])