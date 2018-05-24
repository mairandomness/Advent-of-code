"""--- Part Two ---

As you congratulate yourself for a job well done, you notice that the documentation has been on the back of the tablet this entire time. While you actually got most of the instructions correct, there are a few key differences. This assembly code isn't about sound at all - it's meant to be run twice at the same time.

Each running copy of the program has its own set of registers and follows the code independently - in fact, the programs don't even necessarily run at the same speed. To coordinate, they use the send (snd) and receive (rcv) instructions:

snd X sends the value of X to the other program. These values wait in a queue until that program is ready to receive them. Each program has its own message queue, so a program can never receive a message it sent.
rcv X receives the next value and stores it in register X. If no values are in the queue, the program waits for a value to be sent to it. Programs do not continue to the next instruction until they have received a value. Values are received in the order they are sent.
Each program also has its own program ID (one 0 and the other 1); the register p should begin with this value.

For example:

snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d
Both programs begin by sending three values to the other. Program 0 sends 1, 2, 0; program 1 sends 1, 2, 1. Then, each program receives a value (both 1) and stores it in a, receives another value (both 2) and stores it in b, and then each receives the program ID of the other program (program 0 receives 1; program 1 receives 0) and stores it in c. Each program now sees a different value in its own copy of register c.

Finally, both programs try to rcv a fourth time, but no data is waiting for either of them, and they reach a deadlock. When this happens, both programs terminate.

It should be noted that it would be equally valid for the programs to run at different speeds; for example, program 0 might have sent all three values and then stopped at the first rcv before program 1 executed even its first instruction.

Once both of your programs have terminated (regardless of what caused them to do so), how many times did program 1 send a value?"""



def do_instruction(variables, other_variables, input_lst,terminate , i, count):
    line = input_lst[i]
    instruction = line[0]
    key = line[1]
    if instruction == "set":
        try:
            value = int(line[2])
            variables[key] = value
        except ValueError:
            key2 = line[2]
            if key2 not in variables:
                variables[key2] = variables["id"]
            variables[key] = variables[key2]


    elif instruction == "add":
        try:
            variables[key] += int(line[2])
        except ValueError:
            key2 = line[2]
            if key2 not in variables:
                variables[key2] = variables["id"]
            variables[key] += variables[key2]

    elif instruction == "mul":
        if key not in variables:
            variables[key] = variables["id"]
        try:
            variables[key] *= int(line[2])
        except ValueError:
            key2 = line[2]
            if key2 not in variables:
                variables[key2] = variables["id"]

            variables[key] *= variables[key2]

    elif instruction == "mod":
        try:
            variables[key] %= int(line[2])
        except ValueError:
            key2 = line[2]
            if key2 not in variables:
                variables[key2] = variables["id"]
            variables[key] %= variables[key2]

    elif instruction == "jgz":
        try:
            value2 = int(line[2])
        except ValueError:
            value2 = variables[line[2]]
        try:
            value1 = int(key)
        except ValueError:
            value1 = variables[key]

        if value1 > 0:
            i += value2 - 1
    elif instruction == "snd":
        try:
            value = int(key)
        except ValueError:
            if key not in variables:
                variables[key] = variables["id"]
            value = variables[key]
        if variables["id"] == 0:
            other_variables["queue"].append(value)
        else:
            other_variables["queue"].append(value)
            count+=1
    elif instruction == "rcv":
        try:
            variables[key] = variables["queue"][0]
            variables["queue"] = variables["queue"][1:]
            terminate = 0
        except IndexError:
            terminate +=1
            i -= 1


    i += 1

    return (i, count, terminate)


def main():
    f = open("input", "r")
    text = f.read()[:-1].split("\n")
    input_lst = [line.split(" ") for line in text]
    variables0 = {"id":0, "queue": []}
    variables1 = {"id":1, "queue": []}
    terminate0 = 0
    terminate1 = 0
    count = 0
    i = 0
    j = 0

    while 0 <= i < len(input_lst) or 0 <= j < len(input_lst):
        if 0 <= i < len(input_lst):
            (i, count, terminate0) = do_instruction(variables0,variables1, input_lst,terminate0, i, count)
        if 0 <= j < len(input_lst):
            (j, count, terminate1) = do_instruction(variables1, variables0, input_lst,terminate1, j, count)
        if terminate1 >= 4 and terminate0 >= 4:
            j = len(input_lst)
            i = len(input_lst)
    print(count)










if __name__ == "__main__":
    main()
