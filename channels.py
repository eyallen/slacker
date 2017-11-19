import json
import os
from slackclient import SlackClient

HELP_COMMAND = "help"
LIST_COMMAND = "list"

def handle_command(command):
    commands = command.split()

    if len(commands) == 1:
        print_help()
        return False

    {
        HELP_COMMAND: print_help,
        LIST_COMMAND: get_list_of_channels,
    }.get(commands[1], print_help)()

    return False

def get_list_of_channels():

    #TODO: move me to a class object
    slack_token = os.environ["SLACK_API_TOKEN"]
    sc = SlackClient(slack_token)

    print("Getting List of Channels")
    print(80 * "=")
    # get list of channels
    channels = sc.api_call("channels.list")
    channels = json.dumps(channels)
    channels = json.loads(str(channels))

    for channel in channels["channels"]:
        print(channel["name"])

def print_help():
    print("channels help")