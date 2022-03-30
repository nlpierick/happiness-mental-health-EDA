import unittest
from main import *
from data import *

class TestProject(unittest.TestCase):
    def testMeanSquaredError(self):
        meanSquaredError = metrics.mean_squared_error([21, 8, 5, 13, 2],
                                                      [7, 11, 3, 16, 1])
        self.assertEqual(round(meanSquaredError, 3), 43.8)

    @unittest.expectedFailure
    def testMeanSquaredFail(self):
        meanSquaredError = metrics.mean_squared_error([21, 8, 5, 13, 2],
                                                      [7, 11, 3, 16, 1])
        self.assertEqual(round(meanSquaredError, 3), 50.0)

    def testCoeffDetermination(self):
        X = np.array([21, 8, 5, 13, 2]).reshape(-1, 1)
        Y = np.array([7, 11, 3, 16, 1]).reshape(-1, 1)
        model = LinearRegression().fit(X, Y)
        coeffDetermination = model.score(X, Y)
        self.assertEqual(round(coeffDetermination, 3), 0.234)

    @unittest.expectedFailure
    def testCoeffDetFail(self):
        X = np.array([21, 8, 5, 13, 2]).reshape(-1, 1)
        Y = np.array([7, 11, 3, 16, 1]).reshape(-1, 1)
        model = LinearRegression().fit(X, Y)
        coeffDetermination = model.score(X, Y)
        self.assertEqual(round(coeffDetermination, 3), 0.123)

    def testMeanAbsoluteError(self):
        meanAbsError = metrics.mean_absolute_error([21, 8, 5, 13, 2],
                                                   [7, 11, 3, 16, 1])
        self.assertEqual(round(meanAbsError, 3), 4.600)

    @unittest.expectedFailure
    def testMeanAbsoluteFail(self):
        meanAbsError = metrics.mean_absolute_error([21, 8, 5, 13, 2],
                                                   [7, 11, 3, 16, 1])
        self.assertEqual(round(meanAbsError, 3), 0.000)

    def testMeanRootError(self):
        meanRootError = np.sqrt(metrics.mean_squared_error([21, 8, 5, 13, 2],
                                                           [7, 11, 3, 16, 1]))
        self.assertEqual(round(meanRootError, 3), 6.618)

    @unittest.expectedFailure
    def testMeanRootFail(self):
        meanRootError = np.sqrt(metrics.mean_squared_error([21, 8, 5, 13, 2],
                                                           [7, 11, 3, 16, 1]))
        self.assertEqual(round(meanRootError, 3), 1.111)


if __name__ == '__main__':
    unittest.main()

