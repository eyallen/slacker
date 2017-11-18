import os
import json
from slackclient import SlackClient

def get_list_of_channels(sc):
    print("Getting List of Channels")
    print(80 * "=")
    # get list of channels
    channels = sc.api_call("channels.list")
    channels = json.dumps(channels)
    channels = json.loads(str(channels))
    return channels

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

channels = get_list_of_channels(sc)
for channel in channels["channels"]:
    print(channel["name"])


