{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b21cf645-5025-4d31-ab53-151aac668c66",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Using this script to save csv files into database with their filename as tablename\n",
    "\n",
    "#importing required lib\n",
    "import pandas as pd\n",
    "import os\n",
    "from sqlalchemy import create_engine\n",
    "import logging\n",
    "import time\n",
    "\n",
    "#adding a logger\n",
    "logging.basicConfig(\n",
    "    filename=\"logs/ingestion_db.log\", \n",
    "    level=logging.DEBUG,\n",
    "    format=\"%(asctime)s - %(levelname)s - %(message)s\", \n",
    "    filemode=\"a\"  \n",
    ")\n",
    "\n",
    "#creating an engine\n",
    "engine = create_engine('sqlite:///inventory1.db')\n",
    "\n",
    "\n",
    "#defining function to injest data to db\n",
    "def ingest_db(df, table_name, engine):\n",
    "    '''this function will ingest the dataframe into database table'''\n",
    "    df.to_sql(table_name, con = engine, if_exists = 'replace', index = False)\n",
    "\n",
    "# defining function to load the data\n",
    "def load_raw_data():\n",
    "    '''this function will load the CSVs as dataframe and ingest into db'''\n",
    "    start = time.time()\n",
    "    for file in os.listdir('data'):\n",
    "        if '.csv' in file:\n",
    "            df = pd.read_csv('data/'+file)\n",
    "            logging.info(f'Ingesting {file} in db')\n",
    "            ingest_db(df, file[:-4], engine)\n",
    "            \n",
    "        except Exception as e:\n",
    "            logging.error(f\"-------------------Failed to ingest {file}: {e}-------------------\")\n",
    "            logging.debug(traceback.format_exc()) #full trace\n",
    "        \n",
    "    end = time.time()\n",
    "    total_time = (end - start)/60\n",
    "    logging.info('--------------Ingestion Complete------------')\n",
    "    \n",
    "    logging.info(f'\\nTotal Time Taken: {total_time} minutes')\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    load_raw_data()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
