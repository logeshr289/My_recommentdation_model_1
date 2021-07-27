import numpy as np
import pandas as pd

def model(Item_Id):
    df=pd.read_csv("Recommendtation_system\pre_modcloth.csv")


    df.groupby('item_id')['rating'].mean().sort_values(ascending=False).head()

    df.groupby('item_id')['rating'].count().sort_values(ascending=False).head()

    ratings = pd.DataFrame(df.groupby('item_id')['rating'].mean())


    ratings['num of ratings'] = pd.DataFrame(df.groupby('item_id')['rating'].count())
  



    len(pd.unique(df['item_id']))

    prod= df.pivot_table(index='user_id',columns='item_id',values='rating')


    ratings.sort_values('num of ratings',ascending=False).head(10)
    
    item_user_ratings = prod[int(Item_Id)]
    
    similar_to_item = prod.corrwith(item_user_ratings)
    
    corr_item = pd.DataFrame(similar_to_item,columns=['Correlation'])
    corr_item.dropna(inplace=True)
    
    corr_item.sort_values('Correlation',ascending=False)
    
    corr_item = corr_item.join(ratings['num of ratings'])
    
    item=corr_item[corr_item['num of ratings']>100].sort_values('Correlation',ascending=False).head(5)
    index_list = item.index.tolist()
    list_string = map(str, index_list) 
    joined_string = ",".join(list_string)

    return (joined_string)