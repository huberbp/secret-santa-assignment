import random

def random_partition(names, lcaptain, rcaptain):
    l_list = list()
    r_list = list()

    names.remove(lcaptain)
    names.remove(rcaptain)

    l_list.append(lcaptain)
    r_list.append(rcaptain)
    
    iterations = int(len(names) / 2)
    for i in range (0, iterations):
        rand_item = random.choice(names)
        names.remove(rand_item)
        l_list.append(rand_item)

    for i in range (0, len(names)):
        rand_item = random.choice(names)
        names.remove(rand_item)
        r_list.append(rand_item)

    return [l_list, r_list]

def make_assignments(names):
    giving = names.copy()
    recieving = names.copy()

    output = list()

    while len(giving) != 0 and len(recieving) != 0:
        draw = random.choice(giving)
        draw2 = random.choice(recieving)
        loop_check = 0
        while draw == draw2:
            draw = random.choice(giving)
            draw2 = random.choice(recieving)
            loop_check = loop_check + 1
            if loop_check > 99:
                return "ERROR"
        
        giving.remove(draw)
        recieving.remove(draw2)

        output.append(str(draw + " ==> " + draw2))
    
    return output

# File should be opened before hand
def write_names_to_file(names, file):
    for name in names:
        file.write(name + "\n")

def main():
    usr_input = input("File location (relative to cd): ")
    try:
        f = open(usr_input)
    except FileNotFoundError:
        print("The name file specified isn't correct or doesn't exist")
        return
    
    names = f.readlines()
    
    for index in range(0, len(names) - 1):
        names[index] = names[index][0: len(names[index]) - 1]
    
    if names[len(names) - 1][len(names[len(names) - 1]) - 1] == "\n":
        names[len(names) - 1] = names[len(names) - 1][0: len(names[len(names) - 1]) - 1]
    
    names = [x for x in names if len(x) > 1]

    cap1 = input("Enter first \"captain\" name: ")
    cap2 = input("Enter second \"captain\" name: ")

    try:
        split_lists = random_partition(names, cap1, cap2)
    except ValueError:
        print("One of your captains ", cap1, " and ", cap2, " are not in the list")
        return
    
    group1 = make_assignments(split_lists[0])
    while group1 == "ERROR":
        group1 = make_assignments(split_lists[0])
    group2 = make_assignments(split_lists[1])
    while group2 == "ERROR":
        group2 = make_assignments(split_lists[1])

    left_group_file = open(cap2 + "_group.txt", "w")
    right_group_file = open(cap1 + "_group.txt", "w")

    write_names_to_file(group1, left_group_file)
    write_names_to_file(group2, right_group_file)

if __name__ == "__main__":
    main()