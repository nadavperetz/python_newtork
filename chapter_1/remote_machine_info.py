import socket


def get_remote_machine_inf():
    """
    Pretty self explained, it will print the host name and ip address
    :return:
    """
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)  # Returns the host IP
    print "Host name: " + str(host_name)
    print "IP address: " + str(ip_address)


if __name__ == '__main__':  # If you are running this file, the statement return TRUE
    get_remote_machine_inf()

