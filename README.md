# Variance Metric Appender

## Description
A tool to append metrics from previously generated data to a list of genes.

## Quick Start
Download or clone the repository to start. 

```
git clone https://github.com/bryantcao/variance-metric-appender.git
cd variance-metric-appender
```

Verify that the requirements are met.

Execute the main script `run_VMM.sh` to start.

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

