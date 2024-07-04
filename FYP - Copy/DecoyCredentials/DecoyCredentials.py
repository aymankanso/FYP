from tkinter import *
import sqlite3
import asyncio
import asyncssh
import sys
import time
import random

def handle_client(process):
    process.exit(0)

conn = sqlite3.connect(r"C:\Users\user\Desktop\FYP\DecoyCredentials\.vs\slnx.sqlite")
c = conn.cursor()
conn.commit()
conn.close()

class MySSHServer(asyncssh.SSHServer):
    def connection_made(self, conn):
        self._conn = conn

    def password_auth_supported(self):
        return True

    def validate_password(self, username, password):
        print('Login attempt from %s with username %s and password %s' %
              (self._conn.get_extra_info('peername')[0], username, password))
        # Sleep, then disconnect
        time.sleep(random.randint(0, 5))
        raise asyncssh.DisconnectError(10, "Connection lost")

async def start_server():
    await asyncssh.create_server(MySSHServer, '', 1234,
                                  server_host_keys=[r"C:\Users\user\ssh_host_key"],
                                  process_factory=handle_client,
                                  server_version='AsyncSSH_1.0')


# Run the SSH server
asyncio.run(start_server())
