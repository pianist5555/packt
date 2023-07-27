import socket
from binascii import hexlify


def find_service_name():
    protocolname = "tcp"
    for port in [80, 25]:
        print(
            f"Port: {port} -> service name: {socket.getservbyport(port, protocolname)}"
        )

    print(f"Port: {53} -> service name: {socket.getservbyport(53, 'udp')}")
    print(
        f"Port: {8009} -> service name: {socket.getservbyport(53, protocolname)}"
    )


if __name__ == "__main__":
    find_service_name()
