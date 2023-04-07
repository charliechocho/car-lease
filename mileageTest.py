from os.path import exists

if exists('mileage.db'):
    print('File Exists')
    with open('mileage.db', 'r') as f:
        result = f.readline()
        print(result)
else:
    print('creating file!')
    with open('mileage.db', 'w+') as f:
        f.seek(0)
        f.write('First Line')

with open('mileage.db', 'w') as f:
    f.seek(0)
    f.write('26943 km to date!')
