import io
from contextlib import redirect_stdout
import warnings
import re

from pgmpy.factors.discrete.CPD import TabularCPD
from pgmpy.factors.discrete.DiscreteFactor import DiscreteFactor

import pandas as pd
import numpy as np


def print_full(cpd: TabularCPD) -> None:
    """
    Print the full CPD table in pgmpy.

    Parameters
    ----------
    cpd : TabularCPD
        The CPD to print.

    Returns
    -------
    None
        CPD table is printed to stdout and no value is returned.
    """
    # Temporarily change the truncation setting
    backup = TabularCPD._truncate_strtable
    TabularCPD._truncate_strtable = lambda self, x: x
    print(cpd)
    # Restore the original setting
    TabularCPD._truncate_strtable = backup

    return None