# Program to find average speed and compare cyclists without using list

# Speeds of three cyclists
speed1 = 10
speed2 = 20
speed3 = 30

# Calculate average speed
average_speed = (speed1 + speed2 + speed3) / 3

print("Average speed:", average_speed, "km/h")

# Compare each cyclist's speed with average
if speed1 < average_speed:
    print("Cyclist 1 with speed", speed1, "km/h is slower than the average.")
elif speed1 == average_speed:
    print("Cyclist 1 with speed", speed1, "km/h is equal to the average.")
else:
    print("Cyclist 1 with speed", speed1, "km/h is faster than the average.")

if speed2 < average_speed:
    print("Cyclist 2 with speed", speed2, "km/h is slower than the average.")
elif speed2 == average_speed:
    print("Cyclist 2 with speed", speed2, "km/h is equal to the average.")
else:
    print("Cyclist 2 with speed", speed2, "km/h is faster than the average.")

if speed3 < average_speed:
    print("Cyclist 3 with speed", speed3, "km/h is slower than the average.")
elif speed3 == average_speed:
    print("Cyclist 3 with speed", speed3, "km/h is equal to the average.")
else:
    print("Cyclist 3 with speed", speed3, "km/h is faster than the average.")
