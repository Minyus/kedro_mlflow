from kedro.extras.datasets.pandas import CSVDataSet
from kedro.extras.datasets.pickle import PickleDataSet

catalog_dict = {
    "train_df": CSVDataSet(
        filepath="data/input/train.csv",
        load_args={"float_precision": "high"},
        # save_args={"float_format": "%.16e"},  # You can set save_args for future use
    ),
    "model": PickleDataSet(filepath="data/model/model.pkl"),
    "test_df": CSVDataSet(
        filepath="data/input/test.csv",
        load_args={"float_precision": "high"},
        # save_args={"float_format": "%.16e"},  # You can set save_args for future use
    ),
    "pred_df": CSVDataSet(
        filepath="data/load/pred.csv",
        # load_args={"float_precision": "high"},  # You can set load_args for future use
        save_args={"float_format": "%.16e"},
    ),
}
