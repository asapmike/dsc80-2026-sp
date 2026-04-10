# lab.py


import os
import io
from pathlib import Path
import pandas as pd
import numpy as np


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


<<<<<<<< HEAD:labs/lab02/lab.py
def trick_me():
    ...


def trick_bool():
    ...
========
def median_vs_mean(nums):
    if len(nums) == 0:
        return None

    mean = sum(nums) / len(nums)
    sorted_nums = sorted(nums)
    n = len(nums)

    if n % 2 == 1:
        median = sorted_nums[n // 2]
    else:
        median = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2

    if median < mean:
        return True
    elif median == mean:
        return True
    else:
        return False
>>>>>>>> a2bc51fdb425c900a527f96f685a5e2f130f4a11:labs/lab01/lab.py


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


<<<<<<<< HEAD:labs/lab02/lab.py
def population_stats(df):
    ...
========
def n_prefixes(s, n):
    result = ''
    for j in range(n, 0, -1):
        result += s[:j]
    return result
>>>>>>>> a2bc51fdb425c900a527f96f685a5e2f130f4a11:labs/lab01/lab.py


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


<<<<<<<< HEAD:labs/lab02/lab.py
def most_common(df, N=10):
    ...
========
def exploded_numbers(ints, n):
    width = len(str(max(ints) + n))
    out = []

    for x in ints:
        nums = []
        for v in range(x - n, x + n + 1):
            nums.append(str(v).zfill(width))
        out.append(' '.join(nums))

    return out
>>>>>>>> a2bc51fdb425c900a527f96f685a5e2f130f4a11:labs/lab01/lab.py


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


<<<<<<<< HEAD:labs/lab02/lab.py
def super_hero_powers(powers):
    ...
========
def last_chars(fh):
    out = ''
    for line in fh:
        line = line.rstrip('\n')
        if line != '':
            out += line[-1]
    return out
>>>>>>>> a2bc51fdb425c900a527f96f685a5e2f130f4a11:labs/lab01/lab.py


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


<<<<<<<< HEAD:labs/lab02/lab.py
def clean_heroes(heroes):
    ...
========
def add_root(A):
    return A + np.sqrt(np.arange(len(A)))



def where_square(A):
    return np.sqrt(A) == np.floor(np.sqrt(A))
>>>>>>>> a2bc51fdb425c900a527f96f685a5e2f130f4a11:labs/lab01/lab.py


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


<<<<<<<< HEAD:labs/lab02/lab.py
def super_hero_stats():
    ...
========
def filter_cutoff_loop(matrix, cutoff):
    # Build each kept column as a list, then transpose back to row format.
    rows = len(matrix)
    cols = len(matrix[0])
    kept_cols = []

    for c in range(cols):
        col_vals = []
        for r in range(rows):
            col_vals.append(matrix[r][c])
        if sum(col_vals) / rows > cutoff:
            kept_cols.append(col_vals)

    if len(kept_cols) == 0:
        return np.empty((rows, 0), dtype=matrix.dtype)

    out_rows = []
    for r in range(rows):
        row = []
        for col in kept_cols:
            row.append(col[r])
        out_rows.append(row)
    return np.array(out_rows)


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def filter_cutoff_np(matrix, cutoff):
    col_means = matrix.mean(axis=0)
    return matrix[:, col_means > cutoff]
>>>>>>>> a2bc51fdb425c900a527f96f685a5e2f130f4a11:labs/lab01/lab.py


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


<<<<<<<< HEAD:labs/lab02/lab.py
def clean_universities(df):
    ...

def university_info(cleaned):
    ...

========
def growth_rates(A):
    return np.round((A[1:] - A[:-1]) / A[:-1], 2)



def with_leftover(A):
    daily_leftover = 20 - np.floor(20 / A) * A
    total_leftover = np.cumsum(daily_leftover)
    can_buy = total_leftover >= A

    if np.any(can_buy):
        return int(np.argmax(can_buy))
    return -1


# ---------------------------------------------------------------------
# QUESTION 8
# ---------------------------------------------------------------------


def salary_stats(salary):
    num_players = len(salary)
    num_teams = salary['Team'].nunique()
    total_salary = salary['Salary'].sum()

    highest_salary = salary.loc[salary['Salary'].idxmax(), 'Player']

    avg_los = round(
        salary.loc[salary['Team'] == 'Los Angeles Lakers', 'Salary'].mean(),
        2
    )

    fifth_row = salary.nsmallest(5, 'Salary').iloc[-1]
    fifth_lowest = f"{fifth_row['Player']}, {fifth_row['Team']}"

    # Remove common suffixes before extracting last names.
    cleaned_names = salary['Player'].str.replace(
        r'\s+(Jr\.?|Sr\.?|II|III|IV|V)$',
        '',
        regex=True
    )
    last_names = cleaned_names.str.split().str[-1]
    duplicates = last_names.duplicated().any()

    highest_paid_team = salary.loc[salary['Salary'].idxmax(), 'Team']
    total_highest = salary.loc[salary['Team']
                               == highest_paid_team, 'Salary'].sum()

    return pd.Series({
        'num_players': num_players,
        'num_teams': num_teams,
        'total_salary': total_salary,
        'highest_salary': highest_salary,
        'avg_los': avg_los,
        'fifth_lowest': fifth_lowest,
        'duplicates': duplicates,
        'total_highest': total_highest
    })

# ---------------------------------------------------------------------
# QUESTION 9
# ---------------------------------------------------------------------


def parse_malformed(fp):

    rows = []

    with open(fp) as fh:
        header = next(fh, None)
        for line in fh:
            # Remove stray quotes and split by commas.
            # Keep non-empty tokens to handle accidental extra commas.
            parts = [p.strip() for p in line.strip().replace(
                '"', '').split(',') if p.strip() != '']

            if len(parts) < 6:
                continue

            first = parts[0]
            last = parts[1]
            weight = float(parts[2])
            height = float(parts[3])
            geo = ','.join(parts[4:])

            rows.append({
                'first': first,
                'last': last,
                'weight': weight,
                'height': height,
                'geo': geo
            })

    return pd.DataFrame(rows, columns=['first', 'last', 'weight', 'height', 'geo'])
>>>>>>>> a2bc51fdb425c900a527f96f685a5e2f130f4a11:labs/lab01/lab.py
