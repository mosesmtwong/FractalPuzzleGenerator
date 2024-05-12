from math import sin
import re

# gosper curve
# axiom = "A"
# ruleA = "A-B--B+A++AA+B-"
# ruleB = "+A-BB--B-A++A+B"
# STEP = 20
# DEGREE = 60

# dragon curve
# axiom = "A"
# ruleA = "A+B"
# ruleB = "A-B"
# STEP = 40
# DEGREE = 90

# twin dragon curve
axiom = "FA+FA+"
ruleA = "A+BF"
ruleB = "FA-B"
STEP = 100
DEGREE = 90


def iter(n):

    seq_two = axiom
    for _ in range(n):
        seq_one = ""
        for chr in seq_two:
            if chr == "A":
                seq_one += ruleA
            elif chr == "B":
                seq_one += ruleB
            else:
                seq_one += chr
        seq_two = seq_one
    return seq_one


def tologo(seq):
    cmd = ""
    for chr in seq:
        if chr.isalnum():
            cmd += f"FORWARD {STEP}\n"
        elif chr == "+":
            cmd += f"LEFT {DEGREE}\n"
        elif chr == "-":
            cmd += f"RIGHT {DEGREE}\n"
    with open("L_system.txt", "w") as f:
        f.write(cmd)


# def roundedlogo(seq):
#     global STEP
#     global DEGREE
#     SIDE = STEP / (1 + 2 * sin(DEGREE / 2))
#     EXTRA = int(STEP * 2 - 2 * SIDE * (1 + sin(DEGREE / 2)))
#     SIDE = int(SIDE)
#     DEGREE = DEGREE // 2

#     cmd = ""
#     for i, chr in enumerate(seq):
#         if chr.isalnum() and not seq[i + 1].isalnum():
#             cmd += f"FORWARD {SIDE}\n"
#         elif chr.isalnum() and seq[i + 1].isalnum():
#             cmd += f"FORWARD {SIDE}\n"
#             cmd += f"FORWARD {EXTRA}\n"
#         elif chr == "+":
#             cmd += f"LEFT {DEGREE}\n"
#             cmd += f"FORWARD {SIDE}\n"
#             cmd += f"LEFT {DEGREE}\n"
#         elif chr == "-":
#             cmd += f"RIGHT {DEGREE}\n"
#             cmd += f"FORWARD {SIDE}\n"
#             cmd += f"RIGHT {DEGREE}\n"
#     with open("L_system.txt", "w") as f:
#         f.write(cmd)


def roundedlogo_normal(seq: str):
    global STEP
    global DEGREE
    SIDE = int(STEP / (1 + 2 * sin(DEGREE / 2)))
    DEGREE = DEGREE // 2

    seq = re.sub(r"[A-Z]+", "f", seq)
    print(seq[1:100])

    cmd = "PENUP\nSETPOS [-1000 2000]\nPENDOWN\n"
    for chr in seq:
        if chr.isalnum():
            cmd += f"FORWARD {SIDE}\n"
        elif chr == "+":
            cmd += f"LEFT {DEGREE}\n"
            cmd += f"FORWARD {SIDE}\n"
            cmd += f"LEFT {DEGREE}\n"
        elif chr == "-":
            cmd += f"RIGHT {DEGREE}\n"
            cmd += f"FORWARD {SIDE}\n"
            cmd += f"RIGHT {DEGREE}\n"
    with open("L_system.txt", "w") as f:
        f.write(cmd)


seq = iter(9)
# tologo(seq)
roundedlogo_normal(seq)
