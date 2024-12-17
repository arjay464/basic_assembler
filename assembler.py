import tables
import sys
import os
import re

def binary(d: int) -> str:
    b = bin(d)[2:]
    return b.zfill(16)


def translate_a(l: str, symbol_table: dict) -> str:
    l = l[1:]
    try:
        num = int(l)
    except ValueError:
        num = symbol_table[l]
    return binary(num)


def translate_c(l: str) -> str:
    if "=" in l:
        dest = l.split("=")[0]
        l = l.split("=")[1]
    else:
        dest = ""
    if ";" in l:
        jump = l.split(";")[1]
        comp = l.split(";")[0]
    else:
        comp = l
        jump = ""

    return f"111{tables.Comp(comp)}{tables.Dest(dest)}{tables.Jump(jump)}"


def clean(l: list[str]) -> list[str]:
    clean_lines = []
    for i in l:
        i = i.replace(" ", "")
        i = i.replace("\t", "")
        i = i.replace("\n", "")
        i = i.split("//")[0]
        if i == "":
            pass
        else:
            clean_lines.append(i)
    return clean_lines


def add_flags(l: list[str], symbol_table: dict) -> dict:
    line_num = 0
    for line in l:
        if re.search('^\(', line):
            line = line[1:-1]
            symbol_table[line] = line_num
        else:
            line_num += 1
    return symbol_table


def add_vars(l: list[str], symbol_table: dict) -> dict:
    reg = 16
    for line in l:
        if re.search('^@/D', line):
            line = line[1:]
            if line in symbol_table:
                pass
            else:
                symbol_table[line] = reg
                reg += 1
    return symbol_table


def assembler() -> None:
    filepath = sys.argv[1]
    cwd = os.getcwd()
    input_name = f"{cwd}/{filepath}"
    try:
        with open(input_name, 'r') as f:
            lines = f.readlines()
    except Exception as e:
        print(e)
    ml = []
    symbol_table = tables.initializeSymbol()
    clean_lines = clean(lines)
    symbol_table = add_flags(clean_lines, symbol_table)
    symbol_table = add_vars(clean_lines, symbol_table)
    for line in clean_lines:
        if line[0] == '@':
            ml.append(translate_a(line, symbol_table))
        elif line[0] == '(':
            pass
        else:
            ml.append(translate_c(line))
    filepath = sys.argv[2]
    output_name = f"{cwd}/{filepath}"
    
    ml = "\n".join(ml)
    try:
        with open(output_name, 'w') as output:
            output.writelines(ml)
    except Exception as e:
        print(e)


assembler()
















