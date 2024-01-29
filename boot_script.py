times_booted = 0

file = open("boot_timer", "w")
data = file.readline()
times_booted += 1
data = "times booted: " + times_booted + "\n"
file.writelines( data )
file.close()

