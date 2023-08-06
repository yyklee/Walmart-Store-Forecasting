# python data_processor.py store.csv train.csv features.csv in command line
## import libraries

# data manipulation
import argparse
import numpy as np
import pandas as pd

## data preprocessing
class DataProcessor:
    def __init__(self):
        self.df_store = None
        self.df_feature = None
        self.df_train = None
        self.merged_df = None

    # extract data
    def extract_data(self, csv):
        '''
        a function that drops unnecessary columns
        '''
        df = pd.read_csv(csv)
        df.columns = df.columns.str.replace(' ', '_').str.lower()
        return df
    
    def merge_data(self, df1, df2, df3):
        '''
        a function that merge three dataframe and cleans errors
        '''
        self.df_store = self.extract_data(df1)
        self.df_feature = self.extract_data(df2)
        self.df_train = self.extract_data(df3)

        self.df_store.drop(columns = ['type'], inplace= True)
        self.df_feature.drop(columns = ['markdown1', 'markdown2', 'markdown3', 
                                        'markdown4', 'markdown5', 'temperature'], inplace = True)

        train_store = self.df_train.groupby(['store','date','isholiday'])['weekly_sales'].mean().reset_index()
        # ensure that date in both table are same data type so that it can merge 
        train_store['date'] = pd.to_datetime(train_store['date'])
        self.df_feature['date'] = pd.to_datetime(self.df_feature['date'])
        
        # merge data
        merged_df = train_store.merge(self.df_store, on = ['store'], how = 'left').merge(self.df_feature, 
                                    on = ['store', 'date'], how = 'left')

        # clean inappropriate data 
        merged_df = merged_df[merged_df['weekly_sales'] > 0]
        
        return merged_df


## export data
def main():
    parser = argparse.ArgumentParser(description= 'Process CSV data using pandas')
    parser.add_argument('csv1', type=str, help='Path to the store CSV file')
    parser.add_argument('csv2', type=str, help='Path to the features CSV file')
    parser.add_argument('csv3', type=str, help='Path to the train CSV file')

    args = parser.parse_args()
    data_processor = DataProcessor()
    clean_df = data_processor.merge_data(args.csv1, args.csv2, args.csv3)

    # clean check
    clean_df = clean_df.drop(columns = 'isholiday_y')
    clean_df = clean_df.rename({'isholiday_x':'isholiday'}, axis = 1)

    clean_df.to_csv('cleaned_data.csv', index=False)
                 
if __name__ == "__main__":
    main()
