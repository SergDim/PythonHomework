calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    info = (len(string), string.upper(), string.lower())
    return info

def is_contains(string, list_to_search):
    count_calls()
    for string_from_list in list_to_search:
        if  string_from_list.lower().find(string.lower()) != -1:
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)