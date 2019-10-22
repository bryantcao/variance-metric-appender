# table merging for highlighting a list of genes

# modules to import

import argparse
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# __config__
parser = argparse.ArgumentParser(description = 'Variance Metric Append')
parser.add_argument('input_list', type = str, help = 'A list of genes with a proper header')
parser.add_argument('grouped_data', type = str, help = 'Grouped data from BV and BC')
arguments = parser.parse_args()


# functions
# a hybrid merge function from PASCAF as well as from Visualizations
def gene_data_merge(input_table, PASCAF_gene):
    up_path = os.path.abspath('.')
    base_name = input_table.split('/')[-1].split('.')[0]
    
    try:
         specific = pd.read_csv(input_table)
    except:
         specific = pd.read_excel(input_table)
            
    pascaf = pd.read_csv(PASCAF_gene, index_col = 0)
    
    specific['SYMBOL'] = specific['Gene_list']
    
    gene_merge = pd.merge(specific, pascaf, how = 'left', on = ['SYMBOL'])
    gene_merge = gene_merge.drop(columns = ['SYMBOL'], axis = 1)
    gene_merge = gene_merge[['Gene_list', 'RefSeq', 'calc_AF', 'PC1', 'Omega', 'GOBiologicalProcess']]
    gene_merge = gene_merge.rename(columns = {'calc_AF': 'gene_AF'})
    gene_merge = gene_merge.drop_duplicates()
    gene_merge = gene_merge.sort_values('gene_AF', ascending=False).drop_duplicates('Gene_list').sort_index()

    pascaf = pascaf.dropna(axis = 0, subset = ['calc_AF']) # drop blanks
    pascaf = pascaf[pascaf['calc_AF'] != 0] # drops 0
    pascaf = pascaf.rename(columns = {'calc_AF': 'gene_AF'})
    pascaf = pascaf.sort_values('gene_AF', ascending=False).drop_duplicates('SYMBOL').sort_index()
    pascaf['gene_AF (log10)'] = np.log10(pascaf['gene_AF']) #log the data first before plotting it
    gene_merge['gene_AF (log10)'] = np.log10(gene_merge['gene_AF']) #log the data first before plotting it
    gene_merge = gene_merge[['Gene_list', 'RefSeq', 'gene_AF', 'gene_AF (log10)', 'PC1', 'Omega', 'GOBiologicalProcess']]
    gene_merge.to_csv(up_path + '/' + base_name + '_VMA' + '.csv')

    plt.rcParams["figure.figsize"] = [12,8]; plt.draw()
    plt.xlabel('PC1'); plt.ylabel('Human allele frequency (log10)');
    plt.scatter(pascaf['PC1'], pascaf['gene_AF (log10)'], alpha = .35, s = 3)
    plt.scatter(gene_merge['PC1'], gene_merge['gene_AF (log10)'], alpha = 1, s = 10, c = 'red')
    
    plt.savefig(up_path + '/' + base_name + '_VMA_highlight' + '.png', dpi = 300)
    
gene_data_merge(arguments.input_list, arguments.grouped_data)
