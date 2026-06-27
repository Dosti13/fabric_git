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
# META     },
# META     "warehouse": {
# META       "default_warehouse": "29e3c4ff-c4b4-449c-ba54-db99f899317f",
# META       "known_warehouses": [
# META         {
# META           "id": "29e3c4ff-c4b4-449c-ba54-db99f899317f",
# META           "type": "Lakewarehouse"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

table_name = "dbo.order"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
from pyspark.sql.functions import *

# Read the new sales data
df = spark.read.format("csv").option("header","true").load("Files/sample_datasets/*order.csv")
df.head()
## Add month and year columns
df = df.withColumn("Year", year(col("OrderDate"))).withColumn("Month", month(col("OrderDate")))

# Derive FirstName and LastName columns
df = df.withColumn("FirstName", split(col("CustomerName"), " ").getItem(0)).withColumn("LastName", split(col("CustomerName"), " ").getItem(1))

# Filter and reorder columns
df = df["SalesOrderNumber", "SalesOrderLineNumber", "OrderDate", "Year", "Month", "FirstName", "LastName", "EmailAddress", "Item", "Quantity", "UnitPrice", "TaxAmount"]
df.printSchema()
# Load the data into a table
df.write.format("delta").mode("append").saveAsTable(table_name)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
