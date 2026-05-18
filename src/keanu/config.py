import sys
from szxxx.config import Config, configure
pck_name = 'keanu'
configure(pck_name, __name__)

def main():
    Config(set_current=True, pck_name=pck_name)
    print(f'''
DATA_STORE_DIR: {DATA_STORE_DIR}
TEST_DATA_DIR: {TEST_DATA_DIR}
''')

# python -m keanu.config
if __name__ == '__main__':
    main()