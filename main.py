from automatas.dfa import check_robot
from automatas.tm import move_robot

if __name__ == '__main__':
    robot = input("Roboter String eingeben: ")
    print("Ist valide (DFA):", check_robot(robot))
    print("Ist möglich (TM):", move_robot(robot) and check_robot(robot))