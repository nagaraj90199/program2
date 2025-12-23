import sys

if len(sys.argv) == 5:  # scriptname + 4 arguments
    scriptname = sys.argv[0]
    vid = sys.argv[1]
    vname = sys.argv[2]
    uop = sys.argv[3]
    cost = sys.argv[4]
    print("User provided inputs")
else:
    scriptname = sys.argv[0]
    vid = 101
    vname = "Car"
    uop = 50
    cost = 20000
    print("Using default values")
print(f"Script Name: {scriptname}")
print(f"Vehicle ID: {vid}")
print(f"Vehicle Name: {vname}")
print(f"Usage of Petrol: {uop}")
print(f"Cost: {cost}")
