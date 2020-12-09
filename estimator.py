from .helpers import make_views_coefficient


class RaningsEstimator:
    
    def __init__(self, data=None):
        self.data=data
    
    def fit(self, data):
        """
            This method takes pandas DataFrame as input. It must consist of four columns (pandas Series) = ('views', 'likes', 'dislikes', 'days_ago').
            Then computes corresponding coefficients.
        """

        # views coefficient
        view_coeff = make_views_coefficient(data)

        
        # likes coefficient


        # dislikes coefficient


        # likes to dislikes coefficient


        # time coefficient
