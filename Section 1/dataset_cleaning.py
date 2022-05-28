## importing files
import os
import pandas as pd
import numpy as np

# setting up base dir and base setting of codes
path_of_files = r"C:\Users\Darren\Documents\GitHub\dataeng_test\\"
output_path = r"C:\Users\Darren\Documents\GitHub\dataeng_test\Section 1\\"

pd.set_option('display.float_format', lambda x: '%.3f' % x)


# name cleaning function
def nameClean(series):
    df_name = series.str.split(expand= True)
    
    # count number of filled columns in name to know how should we handle the name
    df_name['filled_columns'] = np.sum(df_name.applymap(lambda x: 1 if isinstance(x, str) else 0), axis=1)
    
    # if name is 2 parts we don't need to do anything as it can seperate to firstname and lastname
    
    # for name with 4 parts, it means it contains both a prefix and a suffix that is at the start and end
    # therefore, to remove it we can just remove the first and last column
    df_name[0] = np.where(df_name['filled_columns'] == 4, np.nan, df_name[0])
    df_name[3] = np.where(df_name['filled_columns'] == 4, np.nan, df_name[3])
    
    # for name with 3 parts, the code will need to find whether the name contain a prefix or suffix to remove
    # notice that for prefix, there will be a '.' in the field except for Miss, therefore we can exploit it to remove the entire prefix
    havePrefix = np.where((df_name[0].str.contains('\.', na=False)) &
                 (df_name['filled_columns']==3), True,False)
    havePrefix = np.where((df_name[0].str.contains('Miss', na=False)) &
                 (df_name['filled_columns']==3), True,havePrefix)
    
    df_name.loc[havePrefix,0] = None
    
    # for suffix, theres no major indicator of which is suffix in the name, but now that prefix is remove, we can just remove
    # suffix since it is place at the back of their name
    df_name.drop(['filled_columns'], axis = 1, inplace = True)
    df_name['filled_columns'] = np.sum(df_name.applymap(lambda x: 1 if isinstance(x, str) else 0), axis=1)
    
    haveSuffix = df_name['filled_columns'] == 3
    df_name.loc[haveSuffix,2] = None
    df_name.drop(['filled_columns'], axis = 1, inplace = True)
    
    
    # name is now clean so need to seperate to first name last name format.
    df_name['full_name_clean'] = df_name[df_name.columns].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
    
    first_name = df_name['full_name_clean'].str.split(' ').str[0]
    last_name = df_name['full_name_clean'].str.split(' ').str[-1]
    
    return first_name, last_name

# function to remove letters and prepended 0 from the price field
def priceClean(price):
    df_cleanPrice = price.astype(str).str.replace(r'[A-z]', '', regex =True).str.lstrip("0")
    
    return df_cleanPrice

# function to return a series which contains True for values larger than 100
def above100(price):
    price = price.astype(float)
    above_100 = np.where(price > 100, True,False)
    return above_100


# main function containing steps from reading data to uploading clean data
def main():
    # reading both dataset
    os.chdir(path_of_files)
    dataset1 = pd.read_csv("dataset1.csv")
    dataset2 = pd.read_csv("dataset2.csv")
    # dropping if name is missing
    dataset1.dropna(subset = ['name'], inplace = True)
    dataset2.dropna(subset = ['name'], inplace = True)
    
    # cleaning name column to first name, last name
    dataset1['first_name'], dataset1['last_name'] = nameClean(dataset1['name'])
    dataset2['first_name'], dataset2['last_name'] = nameClean(dataset2['name'])
    
    # cleaning price to remove prepending 0 and strings
    dataset1['price_clean']= priceClean(dataset1['price'])
    dataset2['price_clean']= priceClean(dataset2['price'])
    
    # appending both dataset together
    full_dataset = pd.concat([dataset1,dataset2], ignore_index = True)
    
    # adding column for price above 100
    full_dataset['above_100'] = above100(full_dataset['price_clean'])
    
    # reindex columns to needed columns only
    full_dataset = full_dataset.reindex(columns = ['first_name', 'last_name','price_clean', 'above_100'])
    
    # exporting dataset
    full_dataset.to_csv(output_path + "cleaned.csv", index = False)
    
if __name__ == "__main__":
    main()