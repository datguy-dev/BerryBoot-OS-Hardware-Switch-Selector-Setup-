#!/usr/bin/env python

from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
import boot_selector_config

user = boot_selector_config.ftp_user
passw = boot_selector_config.ftp_pass
port = boot_selector_config.ftp_port


authorizer = DummyAuthorizer()
authorizer.add_user(user, passw, '.', perm='elradfmwMT')

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(['0.0.0.0', port], handler)
server.serve_forever()
