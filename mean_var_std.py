import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  else:
    # Converting the list into a np array.
    Array = np.array(list)

    # Reshaping the array into a 3X3 Matrix.
    matrix = Array.reshape((3,3))
    
    # AXISES:
    # Rows = Axis 2
    # Columns = Axis 1

    # Using numpy.transpose to convert my column values into my row values so that i can do calculations easier.
    # Source: https://www.geeksforgeeks.org/python-numpy-numpy-transpose/
    transposed_matrix = np.transpose(matrix)

    # Means for Columns:
    column_means = []
    # Variance for Columns:
    column_variances = []
    # Standard deviation for Columns:
    column_deviations = []
    # Maxes of Columns:
    column_maxes = []
    # Mins of Columns:
    column_mins = []
    # Sums of Columns:
    column_sums = []

    # Columns of the orginal matrix, thats why im calling the iteration column.
    # Calculations for all the Columns:
    for column in transposed_matrix:
      column_means.append(np.mean(column))
      column_variances.append(np.var(column))
      column_deviations.append(np.std(column))
      column_maxes.append(np.max(column))
      column_mins.append(np.min(column))
      column_sums.append(np.sum(column))

    # Means for Rows:
    row_means = []
    # Variance for Rows:
    row_variances = []
    # Standard deviation for Rows:
    row_deviations = []
    # Maxes of Rows:
    row_maxes = []
    # Mins of Rows:
    row_mins = []
    # Sums of Rows:
    row_sums = []

    # Calculations for all the Rows:
    for row in matrix:
      row_means.append(np.mean(row))
      row_variances.append(np.var(row))
      row_deviations.append(np.std(row))
      row_maxes.append(np.max(row))
      row_mins.append(np.min(row))
      row_sums.append(np.sum(row))

    # Calculations for flattened matrix:
    # Means for flats:
    flat_means = np.mean(Array)
    # Variance for flats:
    flat_variances = np.var(Array)
    # Standard deviation for flats:
    flat_deviations = np.std(Array)
    # Maxes of flats:
    flat_maxes = np.max(Array)
    # Mins of flats:
    flat_mins = np.min(Array)
    # Sums of flats:
    flat_sums = np.sum(Array)

    # Organising all my data into a list so i can add it to the dictionary easier
    # All Means:
    means = [column_means,row_means,flat_means]
    # All Variances:
    variances = [column_variances,row_variances,flat_variances]
    # All Standard deviation:
    deviations = [column_deviations,row_deviations,flat_deviations]
    # All Maxes:
    maxes = [column_maxes,row_maxes,flat_maxes]
    # All Mins:
    mins = [column_mins,row_mins,flat_mins]
    # All Sums:
    sums = [column_sums,row_sums,flat_sums]

    Dictionary = {
      'mean': means,
      'variance': variances,
      'standard deviation': deviations,
      'max': maxes,
      'min': mins,
      'sum': sums
    }
    calculations = Dictionary
    return calculations
