calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(my_text):
    count_calls()
    a = (len(my_text))
    b = (my_text.upper())
    c = (my_text.lower())
    my_tuple = (a, b, c)
    print(my_tuple)


def is_contains(my_text, my_list):
    count_calls()
    for i in my_list:
        if my_text.lower() == i.lower():
            print(True)
            break
    else:
        print(False)


string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)