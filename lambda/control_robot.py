
import roslibpy
import time

# user_command_dict = {
#     'action': 'move',
#     'distance': 0.3,
#     'direction': 'forward'
# }

def move_robot(user_command_dict):
    client = roslibpy.Ros(host='10.246.167.235', port=9090)
    client.run()

    pub = roslibpy.Topic(client, '/locobot/mobile_base/commands/velocity', 'geometry_msgs/Twist')

    # Control to direction forward or backward
    if user_command_dict['direction'] == 'backward':
        user_command_dict['distance'] = -float(user_command_dict['distance'])
    elif user_command_dict['direction'] == 'forward':
        user_command_dict['distance'] = float(user_command_dict['distance'])

    # Move forward
    move_message = roslibpy.Message({
        'linear': {'x': user_command_dict['distance'], 'y': 0.0, 'z': 0.0},
        'angular': {'x': 0.0, 'y': 0.0, 'z': 0.0}
    })
    pub.publish(move_message)

    # To let the robot move for some time
    time.sleep(float(user_command_dict['distance']))

    # Stop the robot
    stop_message = roslibpy.Message({
        'linear': {'x': 0.0, 'y': 0.0, 'z': 0.0},
        'angular': {'x': 0.0, 'y': 0.0, 'z': 0.0}
    })
    pub.publish(stop_message)

    client.terminate()

# Call the function to move the robot
# move_robot(user_command_dict)