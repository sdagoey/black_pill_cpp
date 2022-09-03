#!/bin/python3
import serial
import argparse
from generated import basic_control_pb2


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--com', default="/dev/ttyACM0", help='The desired comport to open')
    parser.add_argument('-s', '--state', default="0", help='The desired LED state')
    args = parser.parse_args()
    with serial.Serial(args.com,115200,timeout=1) as serial_comm:
        msg = basic_control_pb2.led_state()
        msg.state = int(args.state)
        data = bytearray()
        l = len(data)
        data.extend(l.to_bytes(1, byteorder='little'))
        data.extend(msg.SerializeToString())
        serial_comm.write(data)
