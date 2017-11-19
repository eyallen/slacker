import channels
import sys

CHANNELS_COMMAND    = "/channels"
HELP_COMMAND        = "/help"
QUIT_COMMAND        = "/quit"
STATUS_COMMAND      = "/status"

CHANNELS = channels.Channels()

def do_command_loop():
    shouldexit = False
    while not shouldexit:
        shouldexit = handle_command(raw_input("> "))

def handle_command(command):
    #split the command to allow for sub-processing
    commands = command.split()

    return {
        CHANNELS_COMMAND: handle_channels,
        HELP_COMMAND: print_help,
        QUIT_COMMAND: do_quit,
        STATUS_COMMAND: print_status
    }.get(commands[0], print_help)(command)

def handle_channels(command):
    CHANNELS.handle_command(command)
    return

def print_help(command):
    print ("need some help?")
    return

def do_quit(command):
    sys.exit()

def print_status(command):
    print ("Current Channel: none")
    return