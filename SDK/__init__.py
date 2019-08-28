OFFLINE = False

def set_offline():
    global OFFLINE
    OFFLINE = True


def set_online():
    global OFFLINE
    OFFLINE = False


def is_offline():
    global OFFLINE
    return OFFLINE

from .setting import *
from .wrapper import *
from .error import PyVException


def create_api_wrapper(node_host=API_NODE, api_key=API_KEY):
    return Wrapper(node_host, api_key)

from .application import *