from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C
from time import sleep

# Setup
ultrasonic = UltrasonicSensor()
motor_left = LargeMotor(OUTPUT_B)
motor_right = LargeMotor(OUTPUT_C)

# Move forward until the distance is less than 10 cm
while True:
    distance = ultrasonic.distance_centimeters
    if distance < 10:  # Stop if an object is closer than 10 cm
        motor_left.stop()
        motor_right.stop()
        print("Object detected! Stopping.")
        break
    else:
        motor_left.run_forever(speed_sp=300)
        motor_right.run_forever(speed_sp=300)
    sleep(0.1)
