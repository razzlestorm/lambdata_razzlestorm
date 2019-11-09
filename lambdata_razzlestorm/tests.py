import unittest
from df_utils import get_info
import pandas as pd


class Dataframe_Tests(unittest.TestCase):

    def test_type(self):
        self.assertTrue(isinstance(self, pd.DataFrame))

if __name__ == '__main__':
    unittest.main()
