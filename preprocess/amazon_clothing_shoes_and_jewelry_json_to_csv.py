import os
import csv
import shutil
import pandas as pd
from rich.progress import track

DATASET_DIR = (os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir)))+"./datasets"
jsfile = DATASET_DIR + "/Clothing_Shoes_and_Jewelry.json"
csvfile = DATASET_DIR + "/Clothing_Shoes_and_Jewelry_Result_2018.csv"
if not os.path.isfile(csvfile) and not os.path.isfile(DATASET_DIR + '/amazon/Clothing_Shoes_and_Jewelry_Result_2018.csv'):
    dataset_list = [["reviewerID", "asin", "reviewTime", "unixReviewTime"]]
    with open(jsfile, 'rt', buffering=10000, encoding='utf8') as datasets:
        print("Add huge json content to list ...")
        for line in track(datasets):
            trans = eval(line, {"true":True,"false":False,"null":None})
            user_id    = trans['reviewerID']
            product_id = trans['asin']
            reviewTime     = trans['reviewTime']
            unixReviewTime = trans['unixReviewTime']
            # processing time character
            reviewTime = reviewTime.translate({ord(','): None})
            reviewTime = reviewTime.split(' ')
            reviewTime = (f"{reviewTime[0]} {reviewTime[1]}, {reviewTime[2]}")
            dataset_list.append( [user_id, product_id, reviewTime, unixReviewTime] )
    with open(csvfile, 'w') as f:
        print("Write data into csv ...")
        csv_writer = csv.writer(f)
        for line in track(dataset_list):
            csv_writer.writerow(line)
    # Remove blank lines    
    print("Remove blank lines ...")    
    data = pd.read_csv(csvfile)
    data = data.dropna(how="all").to_csv(csvfile, index=False)
# Create amazon folder
isExists_file = os.path.exists(DATASET_DIR + '/amazon')
if not isExists_file: os.makedirs(DATASET_DIR+ '/amazon')
# Move file
if not os.path.isfile(DATASET_DIR + '/amazon/Clothing_Shoes_and_Jewelry_Result_2018.csv'): shutil.move(csvfile, DATASET_DIR + '/amazon')
if not os.path.isfile(DATASET_DIR + '/amazon/Clothing_Shoes_and_Jewelry.json'): shutil.move(jsfile, DATASET_DIR + '/amazon')    
print("Done.")    