import zmq

def main(addr, who):

    ctx = zmq.Context()
    socket = ctx.socket(zmq.PUB)
    socket.bind(addr)

    while True:
        msg = raw_input("%s> " % who)
        socket.send_pyobj((msg, who))


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print "usage: prompt.py <address> <username>"
        raise SystemExit
    main(sys.argv[1], sys.argv[2])
