from Color_Detection import Color_Detection


def _in_Robot():
    Color_Detection()
    
def Robot():
    try:
        while True:
            _in_Robot()
    except StopIteration:
        pass
        
if __name__ == "__main__":
    Robot()