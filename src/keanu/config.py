from szxxx.config import *

def main():
    Config(set_current=True)
    print(f'''
DATA_STORE_DIR: {DATA_STORE_DIR}
TEST_DATA_DIR: {TEST_DATA_DIR}
''')

# python -m keanu.config
if __name__ == '__main__':
    main()