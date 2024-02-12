import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# ISL29125 address, 0x44(68)
# Select configuation-1register, 0x01(01)
# 0x0D(13) Operation: RGB, Range: 360 lux, Res: 16 Bits
bus.write_byte_data(0x44, 0x01, 0x05)

time.sleep(1)

print("Reading colour values and displaying them in a new window\n")

def getAndUpdateColour():
    while True:
	# Read the data from the sensor
        # Insert code here
        time.sleep(1)
        sensor_data = bus.read_i2c_block_data(0x44,0x09,6)
        # Convert the data to green, red and blue int values
        # Insert code here
        red = sensor_data[1]
        green = sensor_data[3]
        blue = sensor_data[5]
        # Output data to the console RGB values
        # Uncomment the line below when you have read the red, green and blue values
        if max(red, green, blue) == blue:
            print("the color is blue!")
        elif max(red, green, blue) == red:
            print("the color is red!")
        elif max(red, green, blue) == green:
            print("the color is green")
        print(f"RGB: ({red} {green} {blue})")
        time.sleep(1) 

getAndUpdateColour()
