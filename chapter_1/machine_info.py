import socket

def print_machine_inf():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print "Host name: " + str(host_name)
    print "IP address: " + str(ip_address)


if __name__ == '__main__':
    print_machine_inf()

