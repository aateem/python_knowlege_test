
# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.


def median(number_a, number_b, number_c):
    number_list = sorted(locals().values())
    return number_list[len(number_list) / 2]


# Write a procedure, count_words, which takes as input a string
# and returns the number of words in the string. You may consider words
# as strings of characters separated by spaces.


def count_words(some_string):
    return len(some_string.split(' '))


# Deep Count

# The built-in len operator outputs the number of top-level elements in a List,
# but not the total number of elements. For this question, your goal is to count
# the total number of elements in a list, including all of the inner lists.

# Define a procedure, deep_count, that takes as input a list, and outputs the
# total number of elements in the list, including all elements in lists that it
# contains.
# Hint: You might want to use isinstance in your function.


def deep_count(list_with_deep_hidden_elements):
    el_count = 0
    for el in list_with_deep_hidden_elements:
        if isinstance(el, list):
            el_count += deep_count(el)

        el_count += 1

    return el_count


# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a tuple in the form
# (hours, minutes, seconds)

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).

# Example:
# download_time(1024,'kB', 1, 'Mb')
# download_time(13,'GB', 5.6, 'Mb')


def download_time(file_size, file_units, bandwidth, bandwidth_unit):
    unit_map = {
        'kb': 2 ** 10,
        'kB': 2 ** 10 * 8,
        'Mb': 2 ** 20,
        'MB': 2 ** 20 * 8,
        'Gb': 2 ** 30,
        'GB': 2 ** 30 * 8,
        'Tb': 2 ** 40,
        'TB': 2 ** 40 * 8
    }

    result = (file_size * unit_map[file_units]) / (bandwidth * unit_map[bandwidth_unit])

    hours = int(result / 3600)
    minutes = int((result - 3600 * hours) / 60)
    seconds = result - (3600 * hours + 60 * minutes)

    return (hours, minutes, seconds)


# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.


#def rotate(string_to_rotate, n):
#    if n == 0:
#        return string_to_rotate
#
#    string_to_rotate = list(string_to_rotate)
#    string_to_return = string_to_rotate
#
#    index_changer = n / abs(n)
#
#    import pdb
#    pdb.set_trace()
#
#    for letter in string_to_rotate:
#        index_to_write = string_to_rotate.index(letter)
#        shift_steps = abs(n)
#
#        while shift_steps:
#            if (index_to_write == 0 and n < 0) or (index_to_write == len(string_to_return) - 1 and n > 0):
#                index_to_write = -1 if n < 0 else 0
#                shift_steps -= 1
#                continue
#
#            if string_to_return[index_to_write] == ' ':
#                index_to_write += index_changer
#                continue
#
#            index_to_write += index_changer
#            shift_steps -= 1
#
#        string_to_return[index_to_write] = letter
#        string_to_rotate[string_to_rotate.index(letter)] = None
#
#    return ''.join(string_to_return)

def rotate(string_to_rotate, n):
    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    if n == 0:
        return string_to_rotate

    string_to_rotate = list(string_to_rotate)
    string_to_return = []

    index_changer = n / abs(n)

    for letter in string_to_rotate:
        if letter == ' ':
            string_to_return.append(letter)
            letter = None
            continue

        shift_step = abs(n)
        index = alphabet.index(letter)

        while shift_step:
            if (index == 0 and n < 0) or (index == len(alphabet) - 1 and n > 0):
                index = -1 if n < 0 else 0
                shift_step -= 1
                continue

            index += index_changer
            shift_step -= 1

        string_to_return.append(alphabet[index])

    return ''.join(string_to_return)
