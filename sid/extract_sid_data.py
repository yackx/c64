import sys


def extract(f):
    raw = f.read()

    magic = raw[0:4]
    if not magic in  [b'RSID', b'PSID']:
        print(f"Not a SID file {magic}", file=sys.stderr)
        return False
    
    data_offset = int.from_bytes(raw[0x06:0x08], byteorder="big")
    if not data_offset in [0x76, 0x07c]:
        print(f"Data offset not supported: {data_offset}", file=sys.stderr)
        return False
    
    return raw[data_offset:]


if __name__ == "__main__":
    sid_path = sys.argv[1]
    out_path = sys.argv[2]

    if sid_path == out_path:
        print("Input and output file must be different", file=sys.stderr)
        exit(1)

    with open(sys.argv[1], "rb") as fin:
        if (res := extract(fin)):
            with open(sys.argv[2], "wb") as fout:
                fout.write(res)

        exit(res)
