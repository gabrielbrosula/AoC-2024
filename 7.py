import itertools

day = "7"
test = f"{day}-small"
real = f"{day}"

pdebug = True

def pr(obj):
    if pdebug:
        print(obj)
    else:
        pass

def eval_op(operand1, operand2, op):
    if op == 'mul':
        return operand1 * operand2
    elif op == 'add':
        return operand1 + operand2
    elif op == 'c':
        op_1_s = str(operand1)
        op_2_s = str(operand2)
        concat_s = op_1_s + op_2_s
        return int(concat_s)

def base(part):
    with open(f'./input/{real}.txt', 'r') as f:
        sum = 0
        for line in f:
            colon = line.index(':')
            test_val = int(line[:colon])
            nums = [int(x) for x in line[colon + 1:].strip().split(' ')]

            ops = ['mul', 'add']

            if part == 2:
                # Concatenation operator
                ops.append('c')

            ops_enum = [p for p in itertools.product(ops, repeat=len(nums) - 1)]

            # Loop through all the possible combinations of operations
            for opset in ops_enum:
                # Evaluate at the operation level
                cur_val = nums[0]
                for idx, op in enumerate(opset):
                    cur_val = eval_op(cur_val, nums[idx + 1], op)

                if cur_val == test_val:
                    sum += test_val
                    break
        print(sum)

def p1():
    base(1)

def p2():
    base(2)

p1()
p2()