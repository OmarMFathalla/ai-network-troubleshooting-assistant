import subprocess
def check_internet():
    try:
        subprocess.check_call(["ping", "-c", "1", "8.8.8.8"])
        return True
    except subprocess.CalledProcessError:
        return False

print("AI Network Troubleshooting Assistant")
print("Running on my MacBook!")

issue = input("What network problem are you experiencing? ").lower()

print("You reported:", issue)

if "slow" in issue or "lagging" in issue:
    print("Possible issue detected: Slow network connection.")
    print("Recommended action: Restart your router and run a speed test.")
    other_devices = input("Are other devices also slow? (yes/no): ").lower()
    if other_devices == "yes":
        print("This may indicate a router, modem, or internet service issue.")
    elif other_devices == "no":
        print("This may indicate a device-specific issue.")
elif "disconnect" in issue or "dropping" in issue or "drops" in issue:
    print("Possible issue detected: Network connection is dropping.")
    print("Recommended action: Check signal strength and restart your router.")
elif "no internet" in issue:
    print("Possible issue detected: No internet access.")
    print("Recommended action: Check your router lights and verify your internet service is online.")
elif "wifi" in issue or "wi-fi" in issue:    
    print("Possible issue detected: Wi-Fi connectivity problem.")
    print("Recommended action: Ensure you are connected to the correct Wi-Fi network and check the signal strength.")
else:
    print("Issue not recognized. Please provide more details.")
print(check_internet())