# Variance Metric Appender
A tool to append metrics from previously generated data to a list of genes.

## Quick Start
Download or clone the repository to start. 

```
git clone https://github.com/bryantcao/variance-metric-appender.git
cd variance-metric-appender
```

Verify that the requirements are met.

Double-click or execute the main script `run_VMM.command` to start.

```
./run_VMM.command
```
 __Note:__ Issues with Gatekeeper in macOS can be bypassed by right-clicking the main script and pressing Open.

## Requirements
- Provide the file `chrALL_grouped_data_with_GO_terms.csv`.
  - This is the final output file from the [Variance Model](https://github.com/bryantcao/variance-model) repository (currently private).
  - Copy this file to the `required` subdirectory.
  
- Provide a properly formatted gene list input.
  -  Gene symbols need to be in a single column and separated by line breaks.
  - __Gene_list__ needs to be the header of the list.
  - This file needs to be in an accepted format.
    - .csv
    - .txt
    - .xlsx
  - __Warning__: Other columns are allowed with the gene list input table but the tool will break if the names of the other columns match the exact headers of the grouped_data table (Gene, SYMBOL, RefSeq, full_RefSeq, Raw Counts, Total Intersects, Unique Intersects, ratio-AMS, sum-gnomADe_AC, calc_sum-AN, calc_AF, PC1, Omega, GOBiologicalProcess). 
    - A solution is to change the names of the input table headers or remove them (keeping only the Gene_list column).

