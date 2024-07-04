import signal
import sys
import asyncio
import asyncssh
import paramiko
import threading
import socket


async def start_server():
    class SSHServer(paramiko.ServerInterface):
     def __init__(self):
        self.event = threading.Event()

     def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
 
     def check_auth_password(self, username, password):
        if (username == 'your_username' and password == 'your_password'):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

     def check_auth_publickey(self, username, key):
        return paramiko.AUTH_FAILED

def start_ssh_server():
    # Generate SSH server keys (you can skip this if you already have keys)
    host_key = paramiko.RSAKey.generate(2048)

    # Create SSH server
    server = SSHServer()
    server_key = socket.gethostbyname(socket.gethostname()), 22

    # Start SSH server
    ssh_transport = paramiko.Transport(server_key)
    ssh_transport.add_server_key(host_key)
    ssh_transport.start_server(server=server)

    print("SSH server started on port 22...")

    # Wait for connection
    server.event.wait()

start_ssh_server()


