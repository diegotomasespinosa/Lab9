# Diego Espinosa
def encode(input):
    my_list = []

    for number in input:
        my_list.append(int(number) + 3)

    my_string = ''

    for item in my_list:
        my_string += str(item)

    return my_string

def main():
    while True:

        print('''
Menu
-------------
1. Encode
2. Decode
3. Quit
        ''')

        option = int(input('Please enter an option: '))

        if option == 1:
            original_password = input('Please enter your password to encode: ')
            encoded_password = encode(original_password)
            print('Your password has been encoded and stored!')
            continue

        elif option == 2:
            print(f'The encoded password is {encoded_password} and the original password is {original_password}')
            continue

        else:
            break

if __name__ == '__main__':
    main()