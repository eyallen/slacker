import os
import json
from slackclient import SlackClient

# slacker modules
import channels
import commands
import helpers

#slack_token = os.environ["SLACK_API_TOKEN"]
#sc = SlackClient(slack_token)

helpers.clear_screen()
commands.do_command_loop()