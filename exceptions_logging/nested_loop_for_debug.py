num_list = [500, 600, 700]
alpha_list = ['x', 'y', 'z']


def nested_loop():
    for number in num_list:
        print(number)
        for letter in alpha_list:
            print(letter)

if __name__ == '__main__':
    nested_loop()

# to debug this execute
# python -m pdb <python file>
# this will open up the pdb shell
# we can type the command list in order to get context around the current line
# The current line is indicated with the characters ->
# Without providing arguments, the list command provides 11 lines around the current line, but you can also specify which lines to include
# list 3, 7
# To move through the program line by line, we can use step or next:
