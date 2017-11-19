import json
import os
from slackclient import SlackClient

HELP_COMMAND = "help"
INFO_COMMAND = "info"
JOIN_COMMAND = "join"
LIST_COMMAND = "list"

class Channels:
    _channel_list = {}
    _command_list = {}

    _slack_token = ""
    _slack_client = None

    def __init__(self):
        self._slack_token = os.environ["SLACK_API_TOKEN"]
        self._slack_client = SlackClient(self._slack_token)
        self._command_list = {
            HELP_COMMAND: self.print_help,
            INFO_COMMAND: self.get_channel_info,
            JOIN_COMMAND: self.join_channel,
            LIST_COMMAND: self.list_channels,
        }

        #TODO: init _channel_list here

    def handle_command(self, command):
        commands = command.split()

        if len(commands) == 1:
            self.print_help(command)
            return

        self._command_list.get(commands[1], self.print_help)(command)

        return

    #TODO: makes sense to have an option to just pass name/channel object
    def get_channel_info(self, command):
        channelname = self.normalize_channel_name(command.split()[2])
        channelid = self._channel_list[channelname]        

        info = self._slack_client.api_call("channels.info", channel=channelid)
        info = json.dumps(info)
        info = json.loads(str(info))

        return info

    def print_channel_header(self, channelinfo):
        print("#" + channelinfo["channel"]["name"])
        print("{members} | {topic}".format(
            members=len(channelinfo["channel"]["members"]),
            topic=channelinfo["channel"]["topic"]["value"]))

    def join_channel(self, command):
        #Doesn't seem like slack cares about #channel or channel, but it would be good
        #to confirm that
        channelname = command.split()[2]

        self._slack_client.api_call("channels.join", channel=channelname)

        channelinfo = self.get_channel_info(command)
        self.print_channel_header(channelinfo)

        return

    def list_channels(self, command):
        # get list of channels
        channels = self._slack_client.api_call("channels.list")
        channels = json.dumps(channels)
        channels = json.loads(str(channels))

        print("Channels")
        for channel in channels["channels"]:
            # TODO: do this at init, not here
            channelname = self.normalize_channel_name(channel["name"])
            self._channel_list[channelname] = channel["id"]
            print("# " + channel["name"])

    def print_help(self, command):
        print("channels help")

    def normalize_channel_name(self, channelname):
        return channelname.strip("#")