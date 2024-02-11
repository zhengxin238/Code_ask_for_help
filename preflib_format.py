import gurobipy as gp
from gurobipy import *
import graphCode_Coefficient_MinAvg
import prefLibParse
from function_code import borda_score_df_func
import numpy as np



def dict_to_preflib_format(approval_data, directory, filename):
    full_path = os.path.join(directory, filename)
    with open(full_path, 'w') as f:
        for candidate, approval in approval_data.items():
            if approval == 1:
                f.write(candidate + '\n')
    return None


