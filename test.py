gang_member = []
def add_members(name,age,gang):
    new_member = {"name":name,
                  "age":age,
                  "gang":gang
                  }
    gang_member.append(new_member)
while True:
    choices = input("1 for add member, 2 for show member, any key for quit:")
    if choices == "1":
        name = input("Enter Name: ")
        age = int(input("Enter age: "))
        gang = input("Enter gang name: ")
        add_members(name,age,gang)
        print("add member success")
    elif choices == "2":
        print(gang_member)
    else:
        print("Quitting...")
        break