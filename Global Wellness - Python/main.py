# importing the required modules
import glob
import pandas as pd

# specifying the path to csv files
path = "./data"

# csv files in the path
files = glob.glob(path + "/*.csv")

# defining an empty list to store
# content

content = []

# checking all the csv files in the
# specified path
for filename in files:
    # reading content of csv file
    # content.append(filename)
    df = pd.read_csv(filename, index_col=1)
    df.reset_index(drop=True)
    # You don't want to append the data, you will want
    # to merge each set on country
    content.append(df)

# converting content to data frame
full_df = pd.concat(content, axis=0)

print(full_df)
