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

#Written by: Danah-Alamro (Task 7)
def count_vowels(name):
vowels = "aeiou"
count = 0
for letter in name.lower():
    if letter in vowels:
        count += 1

return count

#Written by: Deema-Almanea (Task 2)
def search_name(names,name):
    return name in names
    
def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Number of names:", count_names(names))
    print("Names in uppercase:", to_upper(names))
    for name in names:
    print(name, count_vowels(name))
    
    print("Search For Sara:", search_name(names, "Sara"))
 
    # Each student calls her function here, for example:
    # print("Number of names:", count_names(names))


main()
