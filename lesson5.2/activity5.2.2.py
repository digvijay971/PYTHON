class a:
    def __init__(self):
        print("a PAGAL has been created")
    def __del__(self):
        print("a PAGAL has been destroyed")
def b():
    print("starting the mission")
    d = a()
    print("mission accomplished")
    return d
print(" good job b for completing the mission")
d = b()
print("now you need to kill the PAGAL")        