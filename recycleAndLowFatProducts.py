import pandas as pd

def find_products(Products: pd.DataFrame) -> pd.DataFrame:
    return Products[(Products['low_fats'] =='Y') & (Products['recyclable']== 'Y')][["ProductID"]]


   
Products={
    "ProductID":[11,12,13,14,15],
    "low_fats": ['Y','N','N','Y','Y'],
    "recyclable": ['N','Y','N','Y','Y']
}
df=pd.DataFrame(Products)
print(find_products(df).to_string(index=False))