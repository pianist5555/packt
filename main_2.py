import socket


def print_machine_info():
    remote_host = 'www.python.org'
    try:
        print(
            f"IP address of {remote_host}: {socket.gethostbyname(remote_host)}"
        )
    except socket.error as err_msg:
        print(f"{remote_host, err_msg}")


if __name__ == '__main__':
    print_machine_info()
