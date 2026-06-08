from mlProject import logger
import os
import pandas as pd
from src.mlProject.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__ (self,config : DataValidationConfig):
        self.config = config

    def validate_cols(self)->bool:
            try:
                valid_status = None
                data = pd.read_csv(self.config.unzip_data_dir)

                cols_to_drop = ["Id"]
                data = data.drop(columns=cols_to_drop, errors='ignore')  
                all_cols = list(data.columns)

                all_schema = self.config.all_schema.keys()

                for col in all_cols:
                    if col not in all_schema:
                        valid_status = False
                        with open(self.config.STATUS_FILE, 'w') as f:
                            f.write(f"Validation Status: {valid_status}")
                    else:
                        valid_status = True
                        with open(self.config.STATUS_FILE , 'w') as f:
                            f.write(f"Verification Status: {valid_status}")
                
                data.to_csv(self.config.unzip_data_dir, index=False)
                return valid_status
            except Exception as e:
                raise e


