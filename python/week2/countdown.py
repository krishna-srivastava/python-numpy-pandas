import time

minutes = int(input("Enter a minutes: "))
seconds = int(input("Enter a seconds: "))

totaltime = minutes * 60 + seconds

while totaltime:
    mins, secs = divmod(totaltime,60)
    print(f"{mins:02}:{secs:02}", end = "\r")
    time.sleep(1)
    totaltime -= 1

print("Time up!\a")