#!/usr/bin/env python3
# -*- enconding: utf-8 -*-


# add moudules

import sys
import psutil

from datetime import datetime
from prettytable import PrettyTable


# Get mem info

def mem_info():

	mem = psutil.virtual_memory()

	Total = str(mem.total/1024/1024).split('.')[0] + "MB"
	Used = str(mem.used/1024/1024).split('.')[0] + "MB"
	Available = str(mem.available/1024/1024).split('.')[0] + "MB"

	Mem_table = PrettyTable(["Memory", "values"])
	Mem_table.add_row(["Total", Total])
	Mem_table.add_row(["Used", Used])
	Mem_table.add_row(["Available", Available])
	Mem_table.reversesort = True

	print(Mem_table)


# Get swap info

def swap_info():

	swap = psutil.swap_memory()

	swap_total = str(swap.total/1024/1024).split('.')[0] + "MB"
	swap_used = str(swap.used/1024/1024).split('.')[0] + "MB"
	swap_free = str(swap.free/1024/1024).split('.')[0] + "MB"

	swap_table = PrettyTable(["Swap_info", "values"])
	swap_table.add_row(["Total", swap_total])
	swap_table.add_row(["Used", swap_used])
	swap_table.add_row(["free", swap_free])
	swap_table.reversesort = False

	print(swap_table)


# print system info

try:
    argv = sys.argv[1]
except IndexError:
    print("Invalid parameter value")
    sys.exit(1)   


if argv == "memory":
    mem_info()
elif argv == "swap":
    swap_info()
else:
    print("Usage: %s memory|swap|help"%(sys.argv[0]))

date = datetime.today()

print(str(date).split('.')[0])

