from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    # User authorization settings
    authorizer = DummyAuthorizer()
    # Add user: (username, password, root directory, permissions)
    authorizer.add_user("user", "12345", "C:/ftp_folder", perm="elradfmw")
    # Anonymous user (optional)
    authorizer.add_anonymous("C:/ftp_folder")

    # FTP handler settings
    handler = FTPHandler
    handler.authorizer = authorizer

    # Server settings (IP and port)
    server = FTPServer(("0.0.0.0", 21), handler)

    # Maximum connection settings (optional)
    server.max_cons = 256
    server.max_cons_per_ip = 5

    print("FTP Server started. IP: 0.0.0.0, Port: 21")
    # Start the server
    server.serve_forever()

if __name__ == "__main__":
    main()