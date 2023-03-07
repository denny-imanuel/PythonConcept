import pandas as pd
import numpy as np


class DataFrame:

    def create_from_list(self):
        data = [['aaa', 'aaa', 'aaa'],
                ['bbb', 'bbb', 'bbb'],
                ['ccc', 'ccc', 'ccc']]
        cols = ['col1','col2','col3']
        rows = ['row1','row2','row3']
        frame = pd.DataFrame(data, columns=cols, index=rows)
        print(frame)

    def create_from_map(self):
        data = {'col1': ['aaa', 'bbb', 'ccc'],
                'col2': ['aaa', 'bbb', 'ccc'],
                'col3': ['aaa', 'bbb', 'ccc']}
        rows = ['row1','row2','row3']
        frame = pd.DataFrame(data, index=rows)
        print(frame)

    def append_by_col(self):
        frame = pd.DataFrame()
        frame['col1'] = ['aaa','bbb','ccc']
        frame['col2'] = ['aaa','bbb','ccc']
        frame['col3'] = ['aaa','bbb','ccc']
        print(frame)

    def append_by_row1(self):
        cols = ['col1','col2','col3']
        frame = pd.DataFrame(columns=cols)
        frame = frame.append({'col1': 'aaa', 'col2': 'bbb', 'col3': 'ccc'}, ignore_index=True)
        frame = frame.append({'col1': 'aaa', 'col2': 'bbb', 'col3': 'ccc'}, ignore_index=True)
        frame = frame.append({'col1': 'aaa', 'col2': 'bbb', 'col3': 'ccc'}, ignore_index=True)
        print(frame)

    def append_by_row2(self):
        cols = ['col1', 'col2', 'col3']
        rows = ['row1', 'row2', 'row3']
        frame = pd.DataFrame(columns=cols, index=rows)
        frame.loc['row1'] = ['aaa','aaa','aaa']
        frame.loc['row2'] = ['bbb','bbb','bbb']
        frame.loc['row3'] = ['ccc','ccc','ccc']
        print(frame)

    def index_data_frame(self):
        data = {'col1': ['aaa', 'bbb', 'ccc'],
                'col2': ['aaa', 'bbb', 'ccc'],
                'col3': ['aaa', 'bbb', 'ccc']}
        rows = ['row1','row2','row3']
        frame = pd.DataFrame(data, index=rows)
        print(frame)
        # indexing by name
        col1 = frame['col1']; print(col1)               # select first col
        row1 = frame[:'row1']; print(row1)              # select first row
        cel11 = frame['col1']['row1']; print(cel11)     # select first cel
        # indexing by loc
        col1 = frame.loc[:,'col1']; print(col1)         # select first col
        row1 = frame.loc['row1',:]; print(row1)         # select first row
        cel11 = frame.loc['row1','col1']; print(cel11)  # select first cell
        # indexing by iloc
        col1 = frame.iloc[:,0]; print(col1)             # select first col
        row1 = frame.iloc[0,:]; print(row1)             # select first row
        cel11 = frame.iloc[0,0]; print(cel11)           # select first cell

    def loop_data_frame(self):
        data = {'col1': ['aaa', 'bbb', 'ccc'],
                'col2': ['aaa', 'bbb', 'ccc'],
                'col3': ['aaa', 'bbb', 'ccc']}
        rows = ['row1', 'row2', 'row3']
        frame = pd.DataFrame(data, index=rows)
        # looping by name
        for row in frame.index:
            for col in frame.columns:
                cell = frame[col][row]
                print(cell, end=',')
        print('\n')
        # looping by loc
        for row in frame.index:
            for col in frame.columns:
                cell = frame.loc[row,col]
                print(cell, end=',')
        print('\n')
        # looping by iloc
        for r in range(len(frame.index)):
            for c in range(len(frame.columns)):
                cell = frame.iloc[r,c]
                print(cell, end=',')

    # data frame filter will only select specified axis (row/col)
    def filter_data_frame(self):
        data = {'col1': [96, 99, 102],
                'col2': [97, 100, 103],
                'col3': [98, 101, 104]}
        rows = ['row1', 'row2', 'row3']
        frame = pd.DataFrame(data, index=rows)
        print(frame)
        filter1 = frame.filter(['row1', 'row3'], axis=0)
        filter2 = frame.filter(['col1', 'col3'], axis=1)
        print(filter1)
        print(filter2)

    # data frame select will only select the row that matches the condition and remove the others
    def select_data_frame(self):
        data = {'col1': [96, 99, 102],
                'col2': [97, 100, 103],
                'col3': [98, 101, 104]}
        rows = ['row1', 'row2', 'row3']
        frame = pd.DataFrame(data, index=rows)
        print(frame)
        filter1 = frame[frame['col2'] < 100]
        filter2 = frame[frame['col2'] == 100]
        filter3 = frame[frame['col2'] > 100]
        print(filter1)
        print(filter2)
        print(filter3)

    # data frame where will keep the row that matches the condition and replace the others with nan
    def where_data_frame(self):
        data = {'col1': [96, 99, 102],
                'col2': [97, 100, 103],
                'col3': [98, 101, 104]}
        rows = ['row1', 'row2', 'row3']
        frame = pd.DataFrame(data, index=rows)
        print(frame)
        filter1 = frame.where(frame.col2 < 100)
        filter2 = frame.where(frame.col2 == 100)
        filter3 = frame.where(frame.col2 > 100)
        print(filter1)
        print(filter2)
        print(filter3)
        
    # data frame filter will run query similar to filter, select matches rows and remove others
    def query_data_frame(self):
        data = {'col1': [96, 99, 102],
                'col2': [97, 100, 103],
                'col3': [98, 101, 104]}
        rows = ['row1', 'row2', 'row3']
        frame = pd.DataFrame(data, index=rows)
        print(frame)
        value = 100
        filter1 = frame.query("col2 < @value")
        filter2 = frame.query("col2 == @value")
        filter3 = frame.query("col2 > @value")
        print(filter1)
        print(filter2)
        print(filter3)

    # data frame map is used to map single column to an operator or function or dictionary
    def map_data_frame(self):
        def my_func(x):
            return 3*x
        my_dict = {98:'ninety eight', 101:'one hundred one', 104:'one hundred four'}
        data = {'col1': [96, 99, 102],
                'col2': [97, 100, 103],
                'col3': [98, 101, 104]}
        rows = ['row1', 'row2', 'row3']
        frame = pd.DataFrame(data, index=rows)
        print(frame)
        result1 = frame['col1'].map(lambda x: 2*x)
        result2 = frame['col2'].map(lambda x: my_func(x))
        result3 = frame['col3'].map(my_dict)
        print(result1)
        print(result2)
        print(result3)

    # data frame apply is used to apply multiple columns to an operator or function (no dictionary)
    def apply_data_frame(self):
        def my_func(x):
            return 3*x
        my_dict = {98:'ninety eight', 101:'one hundred one', 104:'one hundred four'}
        data = {'col1': [96, 99, 102],
                'col2': [97, 100, 103],
                'col3': [98, 101, 104]}
        rows = ['row1', 'row2', 'row3']
        frame = pd.DataFrame(data, index=rows)
        print(frame)
        result1 = frame.apply(lambda x: 2*x)
        result2 = frame[['col1','col2']].apply(lambda x: my_func(x))
        result3 = frame['col3'].apply(np.square)
        result4 = frame.apply(my_func)
        print(result1)
        print(result2)
        print(result3)
        print(result4)

    def sort_data_frame(self):
        data = {'col3': [3, 2, 1],
                'col2': [6, 5, 4],
                'col1': [9, 8, 7]}
        rows = ['row3', 'row2', 'row1']
        frame = pd.DataFrame(data, index=rows)
        print(frame)
        sort1 = frame.sort_index()                          # sort by row name
        sort2 = frame.sort_index(axis=1)                    # sort by col name
        sort3 = frame.sort_values(['col1','col2','col3'])   # sort by value on col1, col2, col3
        print(sort1)
        print(sort2)
        print(sort3)

    def group_data_frame(self):
        data = [['aaa', 'ccc', 10, 50],
                ['aaa', 'ccc', 20, 40],
                ['aaa', 'ddd', 30, 30],
                ['bbb', 'ccc', 40, 20],
                ['bbb', 'ddd', 50, 10]]
        cols = ['col1', 'col2', 'num3', 'num4']
        rows = ['row1', 'row2', 'row3', 'row4', 'row5']
        frame = pd.DataFrame(data, columns=cols, index=rows)
        print(frame)
        frame1 = frame.groupby('col1').sum(); print(frame1)
        frame2 = frame.groupby(['col1','col2']).sum(); print(frame2)
        frame3 = frame.groupby(['col1','col2']).agg({'num3':['sum'],'num4':['sum']}); print(frame3)
        frame4 = frame.groupby(['col1','col2']).agg({'num3':['sum','count'],'num4':['sum','count']}); print(frame4)

    # it is used to concatenate two data frame without column indexing so will result in duplicated row/column
    def concat_data_frame(self):
        data1 = [['a', 'aa', 'aaa'],
                 ['b', 'bb', 'bbb'],
                 ['c', 'cc', 'ccc']]
        cols1 = ['idx', 'col1', 'col2']
        rows1 = [1, 2, 3]
        frame1 = pd.DataFrame(data1, columns=cols1, index=rows1)
        print(frame1)
        data1 = [['c', 'ccc', 'cccc'],
                 ['d', 'ddd', 'dddd'],
                 ['e', 'eee', 'eeee']]
        cols2 = ['idx', 'col2', 'col3']
        rows2 = [3, 4, 5]
        frame2 = pd.DataFrame(data1, columns=cols2, index=rows2)
        print(frame2)
        frame3 = pd.concat([frame1, frame2]); print(frame3)
        frame3 = pd.concat([frame1, frame2], join='inner', axis=1); print(frame3)
        frame3 = pd.concat([frame1, frame2], join='outer', axis=1); print(frame3)

    # it is used to join two data frame on a column with overlapping column shown with different suffix
    def join_data_frame(self):
        data1 = [['a', 'aa', 'aaa'],
                ['b', 'bb', 'bbb'],
                ['c', 'cc', 'ccc']]
        cols1 = ['idx','col1','col2']
        rows1 = [1,2,3]
        frame1 = pd.DataFrame(data1, columns=cols1, index=rows1)
        print(frame1)
        data1 = [['c', 'ccc', 'cccc'],
                 ['d', 'ddd', 'dddd'],
                 ['e', 'eee', 'eeee']]
        cols2 = ['idx','col2','col3']
        rows2 = [3,4,5]
        frame2 = pd.DataFrame(data1, columns=cols2, index=rows2)
        print(frame2)
        frame3 = frame1.set_index('idx').join(frame2.set_index('idx'), how='inner', lsuffix='_l', rsuffix='_r'); print(frame3)
        frame3 = frame1.set_index('idx').join(frame2.set_index('idx'), how='left', lsuffix='_l', rsuffix='_r'); print(frame3)
        frame3 = frame1.set_index('idx').join(frame2.set_index('idx'), how='right', lsuffix='_l', rsuffix='_r'); print(frame3)
        frame3 = frame1.set_index('idx').join(frame2.set_index('idx'), how='outer', lsuffix='_l', rsuffix='_r'); print(frame3)

    # it is use to merge two data frame on a column with overlapping column merged as single column and idx column not shown
    def merge_data_frame(self):
        data1 = [['a', 'aa', 'aaa'],
                 ['b', 'bb', 'bbb'],
                 ['c', 'cc', 'ccc']]
        cols1 = ['idx', 'col1', 'col2']
        rows1 = [1, 2, 3]
        frame1 = pd.DataFrame(data1, columns=cols1, index=rows1)
        print(frame1)
        data1 = [['c', 'ccc', 'cccc'],
                 ['d', 'ddd', 'dddd'],
                 ['e', 'eee', 'eeee']]
        cols2 = ['idx', 'col2', 'col3']
        rows2 = [3, 4, 5]
        frame2 = pd.DataFrame(data1, columns=cols2, index=rows2)
        print(frame2)
        frame3 = frame1.set_index('idx').merge(frame2.set_index('idx'), how='inner'); print(frame3)
        frame3 = frame1.set_index('idx').merge(frame2.set_index('idx'), how='left'); print(frame3)
        frame3 = frame1.set_index('idx').merge(frame2.set_index('idx'), how='right'); print(frame3)
        frame3 = frame1.set_index('idx').merge(frame2.set_index('idx'), how='outer'); print(frame3)
