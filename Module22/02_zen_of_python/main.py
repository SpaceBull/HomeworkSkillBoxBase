file_zen = open('zen.txt', 'r')
roster = [word for word in file_zen]
print(roster[::-1])
file_zen.close()
