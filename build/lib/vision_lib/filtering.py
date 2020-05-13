import numpy as np



def longer_than (lines, min_length) :
    """permet de filtrer sur la taille des segments
    lines:nx8 numpy array
    min_length: float
    voir exemple2
    """
    lines=list(lines)
    lines=[line for line in lines if line[7]>min_length]
    return lines 

def intersect(lines):
    """donne toutes les intersections des lignes
    lines:nx8 numpy array
    voir exemple2
    """ 
    intersections = []
    for i, si in enumerate(lines):
        for sj in lines[i+1:]:
            cross_product = np.cross(si[4:6], sj[4:6]) # [a1,b1] ^ [a2, b2]
            if cross_product != 0:
                coeff = 1.0 / cross_product

                intersections.append([coeff * np.cross(si[5:7]   , sj[5:7]), # [b1, c1] ^ [b2, c2]
                                      coeff * np.cross(sj[[4, 6]], si[[4, 6]])]) # -[a1, c1] ^ [a2, c2]
    return np.array(intersections)


