import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():

    player1 = launch_ros.actions.Node(
            package = 'mypkg',
            executable = 'player1',
            )
    
    player2 = launch_ros.actions.Node(
            package = 'mypkg',
            executable = 'player2',
            output = 'screen'
            )
    return launch.LaunchDescription([player1, player2])
