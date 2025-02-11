from picarx import Picarx
import time

POWER = 50
SafeDistance = 40   # > 40 safe
DangerDistance = 20 # > 20 && < 40 turn around,
                    # < 20 backward

class UltrasonicSensor:
    def __init__(self):
        self.px = Picarx()
    
    def read_distance(self):
        """Reads the ultrasonic sensor distance."""
        return round(self.px.ultrasonic.read(), 2)
    
    def move_based_on_distance(self):
        """Controls the car movement based on sensor data."""
        try:
            while True:
                distance = self.read_distance()
                print("Distance: ", distance)
                
                if distance >= SafeDistance:
                    self.px.set_dir_servo_angle(0)
                    self.px.forward(POWER)
                elif distance >= DangerDistance:
                    self.px.set_dir_servo_angle(30)
                    self.px.forward(POWER)
                    time.sleep(0.1)
                else:
                    self.px.set_dir_servo_angle(-30)
                    self.px.backward(POWER)
                    time.sleep(0.5)
        finally:
            self.px.forward(0)

# This will only run if the script is executed directly (not when imported)
if __name__ == "__main__":
    sensor = UltrasonicSensor()
    sensor.move_based_on_distance()
