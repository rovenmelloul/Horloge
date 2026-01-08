# main.py
from horloge import InputChecker, Horloge

if __name__ == '__main__':

    h = Horloge()
    h.take_all_inputs()        
    h.start()

    input_check = InputChecker(h)
    input_check.start()        

    h.join()
    input_check.join()
