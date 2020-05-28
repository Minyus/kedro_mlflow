from kedro.extras.datasets.text import TextDataSet

catalog_dict = {"my_output_dataset": TextDataSet(filepath="data/load/my_output.txt")}
