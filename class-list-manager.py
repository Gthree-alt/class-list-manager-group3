# Class List Manager - Group 3
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]


# ===== Each student adds her function BELOW this line =====

# Written by: Shaden-Al-Tuwaym (Task 1)
def count_names(names):
    return len(names)

#Written by: ATYAF-ALANAZI (Task 6)
def to_upper(names):
    return [name.upper() for name in names]



def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Number of names:", count_names(names))
    print("Names in uppercase:", to_upper(names))
 
    # Each student calls her function here, for example:
    # print("Number of names:", count_names(names))


main()
