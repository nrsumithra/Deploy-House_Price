#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.outliers_influence import variance_inflation_factor
from scipy.stats import zscore,iqr,probplot
import pylab
import re
import warnings
warnings.filterwarnings('ignore')


#Each time Matplotlib loads, it defines a runtime configuration (rc) containing the default styles
#for every plot element you create. This configuration can be adjusted at any time using the plt.
np.random.seed(42)
#  Jupyter will display the variable without the need for a print statement
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
plt.rcParams['figure.figsize']=(10,8)
#%config IPCompleter.greedy=True
#%matplotlib inline
pd.set_option('display.max_rows',1000)
pd.set_option('display.max_columns',1000)
pd.set_option('display.max_colwidth',1000)
#Load the File
df=pd.read_csv("C:/Users/NANDAKUMAR/Desktop/SUMITHRA/DATASCIENCE/Data set/House_Data.csv")
df.head()
#Get the total number of rows and columns in a file
df.shape
# Get the column names ,columns without null values and its datatype
df.info()
#Get the unique values and it count from a column
df['area_type'].value_counts()
#Drop irrelevant features from the file
df=df.drop(['area_type','availability','society','balcony'],axis=1)
df.head(2)
#Check for null values
df.isna().sum()
#Drop null values
df.dropna(inplace=True)
df.shape
def sqft_split(x):
    
    if ('-' in x):
        return x.split('-')
    else:
        return x
    
###############################################

def sqft_avg(x):
    
    if len(x)==2:
        return (float(x[0])+float(x[1]))/2
    else:
        try:
            return float(x)
        except:
            return x
#################################################

def conversion_to_sqft(x):
    if ('Sq. Meter' in str(x)):
        reg=re.findall(r'\d+' ,str(x))
        return float(reg[0])*10.764
    elif 'Sq. Yards' in str(x):
        reg=re.findall(r'\d+' ,str(x))
        return float(reg[0])*9
    elif 'Perch' in str(x):
        reg=re.findall(r'\d+' ,str(x))
        return float(reg[0])*272
    elif 'Acres' in str(x):
        reg=re.findall(r'\d+' ,str(x))
        return float(reg[0])*43560
    elif 'Cents' in str(x):
        reg=re.findall(r'\d+' ,str(x))
        return float(reg[0])*435.6
    elif 'Guntha' in str(x):
        reg=re.findall(r'\d+' ,str(x))
        return float(reg[0])*1089
    elif 'Grounds' in str(x):
        reg=re.findall(r'\d+' ,str(x))
        return float(reg[0])*2400
    else:
        return float(x) 

df['final_sqft']=df['total_sqft'].apply(sqft_split)
df['final_sqft']=df['final_sqft'].apply(sqft_avg)
df['final_sqft']=df['final_sqft'].apply(conversion_to_sqft)
df['size'].unique()
#Function to split number alone from the series
def bedroom(x):
    bhk=x.split(" ")
    return float(bhk[0])

df['BHK']=df['size'].apply(bedroom)
df['bath'].unique()
df=df[df['bath']<=(df['BHK']+1)]
df['Bath']=df['bath'].apply(lambda x:int(x))
df.drop(['bath','size','total_sqft'],axis=1,inplace=True)
df.head(2)
df.info()
df.describe(include='all')
#sns.countplot(df['Bath'])
#sns.pairplot(df)
#sns.histplot(df['price'],bins=40,kde=True,color='Red')
# number of records under each location
Houses_in_location=(df['location'].value_counts()).sort_values(ascending =False)
Houses_in_location
df['location'].nunique()
#Number of locations having less than 10 records are filtered out
other_location=Houses_in_location[Houses_in_location <=10]
type(other_location)
other_location
#'Number of locations having less than 10 records that are grouped under 'Other Location'
#are marked as 'Other'
df['House_location']=df['location'].apply(lambda x:'Other' if x in other_location else x )
#remove spaces from the 'House Location' column
df['House_location']=df['House_location'].apply(lambda x:x.strip())
df['House_location'].nunique()
df.drop('location',axis=1,inplace=True)
#Using Price feature derive price per square foot
df['price/sqft']=(df['price']*100000)/df['final_sqft']
print(df.shape)
df.head(2)
#Minimum square foot per BHK should be >=300
df_validsqft=df[df['final_sqft']/df['BHK']>=300]
print(df_validsqft.shape)
df_validsqft.head()
for_location='Rajaji Nagar'
#sns.lmplot(x='final_sqft', y='price',data=df_validsqft[df_validsqft['House_location']==for_location],hue='BHK',markers='o',fit_reg=False,legend=False)
plt.legend(title='BHK',loc='lower right')
def rmoutliers_ppsqft(df):
    loc_groups=df.groupby('House_location')
    final_df=pd.DataFrame()
    for loc_key,per_location in loc_groups:
        mean=[]
        bhk_no=[]
        i=0
        bhk_groups=per_location.groupby('BHK')
        for bhk_key,bhk in bhk_groups:
            mean.append(round(bhk['price/sqft'].mean(),6))
            bhk_no.append(bhk_key)
        mean.append(mean[-1])    

        for bhk_key,bhk in bhk_groups:
            if (bhk_key==bhk_no[0]):
                final_df=pd.concat([final_df,bhk],ignore_index=True) 
                continue 
            elif bhk.shape[0]>5:
                clean=bhk[(bhk['price/sqft'] > mean[i])] # & (bhk['price/sqft'] <= mean[(i+2)])
                final_df=pd.concat([final_df,clean],ignore_index=True) 
                i=i+1
                continue        
            else:
                final_df=pd.concat([final_df,bhk],ignore_index=True)    
                i=i+1 
              
    return final_df  
data_final=rmoutliers_ppsqft(df_validsqft)
data_final.shape
for_location='Rajaji Nagar'
#sns.lmplot(x='final_sqft', y='price',data=data_final[data_final['House_location']==for_location],hue='BHK',markers='o',fit_reg=False,legend=False)
plt.legend(title='BHK',loc='lower right')
#sns.histplot(data_final['price/sqft'],kde=True,bins=30)
dff=data_final[['House_location','BHK','Bath','final_sqft','price']]
print(dff.shape)
dff.head()
#sns.heatmap(dff.corr(),annot=True)
print(dff['House_location'].nunique())
Location=pd.get_dummies(dff['House_location']) # we can use 'drop_first=True',if we want to drop the first column
Location.drop(['Other'],axis=1,inplace=True)  # to avoid dummy variable trap,we are dropping last column.
print(Location.shape)
Location.head(2)
data=pd.concat([dff[['BHK','Bath','final_sqft','price']],Location],axis=1)
print(data.shape)
data.head(2)
data_log=np.log10(data+1)
def plot_prob(dataset,feature):
    plt.subplot(1,2,1)
    dataset[feature].hist()
    plt.subplot(1,2,2)
    probplot(dataset[feature],dist='norm',plot=pylab)
    plt.show() 
#plot_prob(data_log,'price')
#sns.histplot(data_log['price'],bins=25,kde=True)
#split the data into independent and the target variable
X=data_log.drop(['price'],axis=1)
y=data_log['price']
#Import sklearn libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.model_selection import cross_val_score,GridSearchCV,ShuffleSplit,RandomizedSearchCV
from sklearn.linear_model import LinearRegression,Lasso,Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from scipy.stats import probplot
import pylab
#split train and test data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30,random_state=50)

def Hyperparameter_tuning(X,y):
    model_params={
        'LR':{
            
            'model':LinearRegression(),
            'Params':{
                'normalize':[True,False]
            }         
        },
        'RF':{
            'model':RandomForestRegressor(oob_score=True),
            'Params':{
                'n_estimators':[500],
                'max_samples':[200,400,600],
                'max_depth':[7,8,9,10],
            }
        },
        'DT':{
            'model':DecisionTreeRegressor(),
            'Params':{
                'max_depth':[7,8,9,10],
            } 
         },
              
        'Lasso':{
            'model':Lasso(),
            'Params':{
                'alpha':[2,.001,.01],
                'fit_intercept':[True],
            }
            
        },
        'Ridge':{
            'model':Ridge(),
            'Params':{
                'alpha':[2,.01,.001],
                'fit_intercept':[True],
            }
        },
        'KNN':{
            'model':KNeighborsRegressor(),
            'Params':{
                'weights' :['uniform', 'distance'],
                'n_neighbors':[20,40,60]
            }          
        }
        
        }
      
    CV=ShuffleSplit(n_splits=10,test_size=.20,random_state=50)
    scores=[]
    for key,reg in model_params.items():
        rscv=RandomizedSearchCV(reg['model'],reg['Params'],cv=CV)
        reg_fit=rscv.fit(X,y)
        scores.append({
            'Model':key,
            'Best_Param':reg_fit.best_params_,
            'Best_score':round(reg_fit.best_score_,4)
            
        })
    return pd.DataFrame(scores,columns=['Model','Best_Param','Best_score'])

#Hyperparameter Tuning
Hyperparameter_tuning(X_train,y_train)


LR=LinearRegression(normalize=True)
LR.fit(X_train,y_train)
trainscore=LR.score(X_train,y_train)
print(trainscore)
ypred=LR.predict(X_test)
LR.score(X_test,y_test)
#We need to replicate the row values of the independent features(X),as how we used while 
#training the model.
def predict_price(BHK, Bath, final_sqft,location):
    locate=X.columns.get_loc(location)  #get the index value of the location in search  
    x=np.zeros(len(X.columns)) #To replicate'X',fill row values with '0'.Later it can b changed
    x[0]=BHK
    x[1]=Bath
    x[2]=final_sqft
    x[locate]=1
    x_log=np.log10(x+1)
    pred=LR.predict([x_log])
    price=10**pred[0]
    print(price)
    return price # it will be displayed as an array thats why we are displaying 
                                  # the value from the 0th index.
# as we log transformed the target value,to reverse it back we are taking 10^predicted value  
#specify ('No of BHK','No of Bath','House Square feet','Location in Bengaluru')-in the same order
predict_price(2,2,1400,'Indira Nagar')

# Saving model to disk
import pickle
filename= 'house price.sav'
with open(filename,'wb') as f:
    pickle.dump(LR,f)
import json
columns={
        'location_col':[x.lower() for x in X.columns]
}
with open('columns.json','w') as f:
    json.dump(columns,f)
    f.close()

        


        
