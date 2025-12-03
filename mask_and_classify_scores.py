import numpy as np

def mask_and_classify_scores(arr):
    if type(arr) != np.ndarray:
        return None
    if arr.ndim != 2:
        return None
    
    rows= arr.shape[0]
    cols= arr.shape[1]
    if rows != cols:
        return None
    if rows < 4:
        return None

#Part A: cleaning scores
    cleaned = arr.copy()
    mask_low =cleaned < 0
    cleaned[mask_low] = 0
    mask_high = cleaned > 100
    cleaned[mask_high] = 100

#Part B: Classifying scores
    levels = np.zeros((rows,cols), dtype=int)
    mask_medium= (cleaned >= 40) & (cleaned < 70)
    levels[mask_medium]= 1
    mask_high_scores = cleaned >= 70
    levels[mask_high_scores] = 2

#Part c: Counting passing scores per row
    row_pass_counts = np.zeros(rows, dtype=int)
    for i in range(rows):
        count = 0 
        for j in range(cols):
            if cleaned[i, j] >= 50:
                count = count + 1
        row_pass_counts[i] = count
    return (cleaned, levels, row_pass_counts)

