import a

print('top-level b.py')
a.func()

if __name__ == '__main__':
    print('b.py가 직접 실행')
else:
    print('b.py가 import 되어 실행')