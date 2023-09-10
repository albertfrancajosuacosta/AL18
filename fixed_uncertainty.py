""" 
Active Learning 18

@author: Albert França Josuá Costa
@email: albertfrancajosuacosta@gmail.com
"""


from .base import ActiveLearningBase



class FixedUncertainty(ActiveLearningBase):

    """Strategy of Active Learning to select instances more significative based on uncertainty.

    The fixed uncertainty sampler selects samples for labeling based on the uncertainty of the prediction.
    The higher the uncertainty, the more likely the sample will be selected for labeling. The uncertainty
    measure is compared with a fixed uncertainty limit.


    References
    ----------
    [^1]: I. Zliobaite, A. Bifet, B.Pfahringer, G. Holmes. “Active Learning with Drifting Streaming Data”, IEEE Transactions on Neural Netowrks and Learning Systems, Vol.25 (1), pp.27-39, 2014.

"""

    def __init__(self, theta: float = 0.95, seed=None):
        super().__init__()
        self.theta = theta


    def describe(self):
        print('Strategy of Active Learning to select instances more significative based on uncertainty.'+
              'The fixed uncertainty sampler selects samples for labeling based on the uncertainty of the prediction.'+
              'The higher the uncertainty, the more likely the sample will be selected for labeling. The uncertainty'+
              'measure is compared with a fixed uncertainty limit.'+
              'References [^1]: I. Zliobaite, A. Bifet, B.Pfahringer, G. Holmes. “Active Learning with Drifting Streaming Data”, IEEE Transactions on Neural Netowrks and Learning Systems, Vol.25 (1), pp.27-39, 2014.')
     
    def isSignificative(self, x, y_pred) -> bool:
        """Ask for the label of a current instance.

        Based on the uncertainty of the base classifier, it checks whether the current instance should be labeled.

        Parameters
        ----------
        x
            Instance

        y_pred

       Arrays of predicted labels


        Returns
        -------
        selected
            A boolean indicating whether a label is needed.
            True for selected instance.
            False for not selecte instance.

        """
        maximum_posteriori = max(y_pred.values())
        selected = False
        if maximum_posteriori < self.theta:
            selected = True
        return selected