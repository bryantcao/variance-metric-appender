#!/bin/sh

echo "===================================="
echo "      Variance Metric Appender      "
echo "===================================="
echo ""
echo "This script will append PC1, Omega, and gene_AF from previously generated data to any given list of genes."
echo ""
echo "The list of genes must be a single column of gene symbols split by line breaks."
echo "The header of this column should be 'Gene_list'."
echo ""
echo "Accepted table formats:"
echo "   .csv"
echo "   .txt"
echo "   .xlsx"
echo ""


echo "Drag the gene list table onto this window and press Return to start. Press ⌘Q to cancel."
sleep 1
while :
do
	read -p "Table location: " table_location
	echo ""
	echo "Checking input..."
	export exten="."
	export exten+=`echo ${table_location} | awk -F '.' '{ print $NF }'`
	export base=`basename -s ${exten} ${table_location} 2>&1` 
	if [ ${exten} = ".csv" ] || [ ${exten} = ".txt" ] || [ ${exten} = ".xlsx" ]
	then
		echo "Accepted format found."
		sleep 1
		break
	else
		echo "An accepted table format was not found. Try again."
	fi
done

if [ ${exten} = ".xlsx" ]
then
	echo "Warning: Excel will autocorrect certain gene symbols to dates."
	echo "Warning: Fixes to convert dates back to gene symbols are currently broken." 
	echo "Warning: Verify that the gene list does not contain dates."
	sleep 2
	echo "Running script..."
        python required/VMA.py ${table_location} "required/chrALL_grouped_data_with_GO_terms.csv"  
        wait
        echo "Run completed. This window can be closed now."
else
	echo "Running script..."
	python required/VMA.py ${table_location} "required/chrALL_grouped_data_with_GO_terms.csv" 
	wait
	echo "Run completed. This window can be closed now."
fi;

