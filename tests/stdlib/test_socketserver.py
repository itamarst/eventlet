#!/usr/bin/env python

from eventlet import patcher
from eventlet.green import SocketServer
from eventlet.green import socket
from eventlet.green import select
from eventlet.green import time
from eventlet.green import threading

# to get past the silly 'requires' check
from test import test_support
test_support.use_resources = ['network']

patcher.inject(
    'test.test_socketserver',
    globals(),
    ('SocketServer', SocketServer),
    ('socket', socket),
    ('select', select),
    ('time', time),
    ('threading', threading))

if __name__ == "__main__":
    test_main()
