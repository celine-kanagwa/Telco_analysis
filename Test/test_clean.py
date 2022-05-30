import unittest
import pandas as pd
import sys

sys.path.append("..")

from utils.cleanning import CleanData

df = pd.read_csv('../data/Week1_challenge_data_source.csv')

class TestCleanData(unittest.TestCase):
	def setUp(self)->pd.DataFrame:
		self.obj = CleanData(df) 

	def test_fill_with_mean(self):
		# column to test it on
		column = 'TCP DL Retrans. Vol (Bytes)'

		# getting the data before testing
		before = self.obj.df.isnull()
		
		# mean for the column before filling
		mean = self.obj.df[column].mean()

		# testing if all are filled
		self.obj.fill_with_mean(fill_columns = [column])
		self.assertEqual(self.obj.df[column].isnull().sum(), 0)
		
		# test if the mean is the one that filled it
		after = self.obj.df.loc[0,[column]].values[0]
		self.assertEqual(after, mean)

		# assert if mean before and after are different
		self.assertNotEqual(self.obj.df[column].mean(), mean)

	def test_fill_with_mode(self):
		# column to test it on
		column = 'TCP UL Retrans. Vol (Bytes)'

		# getting the data before testing
		before = self.obj.df.isnull()
		
		# mode for the column before filling
		mode = self.obj.df[column].mode()[0]

		# testing if all are filled
		self.obj.fill_with_mode(fill_columns = [column])
		self.assertEqual(self.obj.df[column].isnull().sum(), 0)
		
		# test if the mode is the one that filled it
		after = self.obj.df.loc[0,[column]].values[0]
		self.assertEqual(after, mode)

	def test_fill_with_median(self):
		# column to test it on
		column = 'HTTP DL (Bytes)'

		# getting the data before testing
		before = self.obj.df.isnull()
		
		# median for the column before filling
		median = round(self.obj.df[column].median(),1)

		# testing if all are filled
		self.obj.fill_with_median(fill_columns = [column])
		self.assertEqual(self.obj.df[column].isnull().sum(), 0)
		
		# test if the median is the one that filled it
		after = self.obj.df.loc[0,[column]].values[0]
		self.assertEqual(after, median)


if __name__ == '__main__':
	unittest.main()
