import time

def focus_timer(minutes):
    seconds = minutes * 60
    for second in range(seconds, 0, -1):
        print(f"\r{second} seconds remaining", end="")
        time.sleep(1)

    print("\nTime's up! Take a break.")

if __name__ == "__main__":
    focus_minutes = int(input("Enter the minutes for focus session: "))
    focus_timer(focus_minutes)
