import json
import os
from slackclient import SlackClient

HELP_COMMAND = "help"
INFO_COMMAND = "info"
JOIN_COMMAND = "join"
LIST_COMMAND = "list"

# TODO: This really needs to be in a class
CHANNEL_LIST = {}

def handle_command(command):
    commands = command.split()

    if len(commands) == 1:
        print_help(command)
        return

    {
        HELP_COMMAND: print_help,
        INFO_COMMAND: get_channel_info,
        JOIN_COMMAND: join_channel,
        LIST_COMMAND: list_channels,
    }.get(commands[1], print_help)(command)

    return

def get_channel_info(command):
    channelname = command.split()[2]

    #TODO: normalize for #name or name
    channelid = CHANNEL_LIST[channelname]

    #TODO: move me to a class object
    slack_token = os.environ["SLACK_API_TOKEN"]
    sc = SlackClient(slack_token)

    info = sc.api_call("channels.info", channel=channelid)
    #info = json.dumps(info)
    #info = json.loads(str(info))

    print(info)

    return

def join_channel(command):
    channelname = command.split()[2]
    #TODO: move me to a class object
    slack_token = os.environ["SLACK_API_TOKEN"]
    sc = SlackClient(slack_token)

    sc.api_call("channels.join", channel=channelname)

    return

def list_channels(command):

    #TODO: move me to a class object
    slack_token = os.environ["SLACK_API_TOKEN"]
    sc = SlackClient(slack_token)

    # get list of channels
    channels = sc.api_call("channels.list")
    channels = json.dumps(channels)
    channels = json.loads(str(channels))

    print("Channels")
    for channel in channels["channels"]:
        # TODO: do this at init, not here
        CHANNEL_LIST[channel["name"]] = channel["id"]
        print("# " + channel["name"])

def print_help(command):
    print("channels help")