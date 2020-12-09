import pandas as pd
import numpy as np

def make_views_coefficient(df):
    """ Takes DataFrame with column 'views' as input """
    views_coefficient = 1 - 1/df['views']

    # clean of infinities
    print(views_coefficient[views_coefficient == np.NINF])
