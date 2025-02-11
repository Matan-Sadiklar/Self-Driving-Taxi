#!/usr/bin/env python3


from sensors import UltrasonicSensor

def main():
    sensor = UltrasonicSensor()
    sensor.move_based_on_distance()

if __name__ == "__main__":
    main()
