
import pandas as pd

df = pd.read_csv('../Data/Week1_challenge_data_source.csv')

def get_for_data(data, list_, secondary_top):
	temp = list()
	for x in list_.index:
		if len(temp)>=secondary_top:
			break
		if x[0] == data:
			temp.append(x[1])
	return temp

def advanced_groupby(df:pd.DataFrame,main,secondary,top=5, secondary_top=5):
	top_data = list(df[main].value_counts()[:top].keys())

	# get only the data with those columns
	group_data = df.loc[df[main].isin(top_data)]

	# group the data by secondary
	grouped_data = group_data[[main,secondary]].groupby([main, secondary]).count()

	# creating a dictionary to hold the data
	groups = dict()

	# looping through to get top 5 only
	for data in top_data:
		groups[data] = get_for_data(data, grouped_data, secondary_top)

	return groups


