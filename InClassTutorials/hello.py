#test Driven approch
### LOok into inport unittest
import sys
def hello():
    return 'Hello World!'
def test_hello():
    assert hello() == 'Hello World!'
    print('all test casses passed... :)')

def main():
    if len(sys.argv) >= 2 and sys.argv[1] == 'test': 
        test_hello()
    else:
        print(hello())
     
if __name__ == "__main__":
    main() 