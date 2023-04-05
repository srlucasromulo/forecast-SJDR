import pandas as pd


def unidecode_dataframe(df: pd.DataFrame):
	from unidecode import unidecode
	for column in df.columns:
		try:
			df[column] = df[column].apply(lambda x: unidecode(x))
		except AttributeError:
			pass
