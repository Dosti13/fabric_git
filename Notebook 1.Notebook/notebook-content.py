# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "8c0c9121-64e1-4920-bac7-f032092f74f4",
# META       "default_lakehouse_name": "practclakehouse",
# META       "default_lakehouse_workspace_id": "0c6ed14a-ad74-4f7d-b82e-b1451582e8f6",
# META       "known_lakehouses": [
# META         {
# META           "id": "8c0c9121-64e1-4920-bac7-f032092f74f4"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

import pandas as pd

wrangler_sample_df = pd.read_csv("https://aka.ms/wrangler/titanic.csv")
display(wrangler_sample_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark",
# META   "editable": true
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
import pandas as pd 

df = pd.read_excel()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
