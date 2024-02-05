# import time

# startTime = time.localtime()

# with open("boot_timer", "r") as read_file:
#     boot_times = int(read_file.readline())
#     print(boot_times)

with open("boot_timer", "w") as file:
    file.write("This was done on bootup")



