def execute_assembly(program_text):
    registers = {}
    lines = program_text.replace("#", "").replace(",", " ").split('\n')
    result = None

    for line in lines:
        line = line.strip()
        if line.startswith('MV'):
            parts = line.split(' ')
            if len(parts) == 3:
                register = parts[1]
                value = int(parts[2])
                registers[register] = value
            else:
                return None
        elif line.startswith('ADD'):
            parts = line.split(' ')
            if len(parts) == 3:
                register1 = parts[1]
                operand = parts[2]
                if operand.startswith('REG'):
                    register2 = operand
                    if register1 in registers and register2 in registers:
                        registers[register1] += registers[register2]
                    else:
                        return None
                else:
                    try:
                        constant = int(operand)
                        if register1 in registers:
                            registers[register1] += constant
                        else:
                            return None
                    except ValueError:
                        return None
            else:
                return None
        elif line.startswith('SHOW'):
            parts = line.split(' ')
            if len(parts) == 2:
                register = parts[1]
                if register in registers:
                    result = registers[register]
                else:
                    return None
            else:
                return None

    return result
