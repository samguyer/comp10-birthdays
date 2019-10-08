
# -- Function to read in the birthday file
def read_birthday_file(filename):
    # -- Open the file and read all the lines into a big list
    with open(filename) as f:
        lines = [line.rstrip() for line in f]

    # -- Collect a list of birthdays
    birthdays = []
    for line in lines:
        # -- Each line has three parts, separated by spaces
        parts = line.split(' ')
        name = parts[0]
        month = int(parts[1])
        day = int(parts[2])
        # -- Make a birthday tuple and append it to the list
        birthday = (name, month, day)
        birthdays.append(birthday)

    return birthdays

# -- Main program
bdays = read_birthday_file('birthdaydata.txt')
for b in bdays:
    (name, month, day) = b
    print(b)
