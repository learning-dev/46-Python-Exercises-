def generate_n_character(num, char):
    temp_str = ''
    for i in range(num):
        temp_str += char
    print temp_str


num_of_times = raw_input("No of times:")
character = raw_input("character:")
generate_n_character(int(num_of_times), character)
