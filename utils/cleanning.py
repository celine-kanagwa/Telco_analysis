import pandas as pd

class CleanData:
	def __init__(self, df:pd.DataFrame):
		self.df = df
		print(' Authomatic action.!!!')

	def fill_with_zero(self, fill_columns=[])->pd.DataFrame:
		for columns in fill_columns:
			self.df[column].fillna(value=0, inplace=True)
		return self.df


	def fill_with_ffill(self, fill_columns)->pd.DataFrame:
		# fill null values with forward fill
		for column in fill_columns:
			self.df[column] = self.df[column].fillna(method='ffill')
		
		return self.df

	def fill_with_bfill(self, fill_columns)->pd.DataFrame:
		# fill null values with backward fill
		for column in fill_columns:
			self.df[column] = self.df[column].fillna(method='bfill')
		return self.df

	def fill_with_mean(self, fill_columns)->pd.DataFrame:
		# fill null values with mean
		for column in fill_columns:
			column_mean = self.df[column].mean()
			self.df[column].fillna(value=column_mean, inplace=True)
		return self.df

	def fill_with_mode(self, fill_columns)->pd.DataFrame:
		# fill null values with mode
		for column in fill_columns:
			column_mode = self.df[column].mode()[0]
			self.df[column].fillna(value=column_mode, inplace=True)
		return self.df

	def fill_with_median(self, fill_columns)->pd.DataFrame:
		# fill null values with mode
		for column in fill_columns:
			column_median = round(self.df[column].median(),1)
			self.df[column].fillna(value=column_median, inplace=True)
		return self.df

	def drop_rows(self, drop_in_columns=[])->pd.DataFrame:
		# drop rows for certain columns or all of them
		if drop_in_columns:
			self.df.dropna(subset=drop_in_columns, inplace=True)
		else:
			self.df.dropna(inplace=True)
		return self.df

	def drop_unwanted_column(self, unwanted_columns)->pd.DataFrame:
		# drop columns in the list unwanted_columns
		self.df.drop(unwanted_columns, axis=1, inplace=True)
		return self.df

	def drop_duplicate(self)->pd.DataFrame:
		# drop all duplicates
		self.df.drop_duplicates(inplace=True)
		return self.df

	def convert_to_datetime(self, datetime_columns)->pd.DataFrame:
		# convert a list of columns to datetime format
		for column in datetime_columns:
			self.df[column] = pd.to_datetime(self.df[column], format='%Y%m%d : %H%M%S')
		return self.df






         
