import struct


class SCTP:
    def __init__(self, data):
        self.src_port, self.dest_port, self.ver_tag, self.checksum, = struct.unpack(
            '! H H L L', data[:12])
        self.data = data[12:]
