import pandas as pd
import requests
import json
#from pandas.io.json import json_normalize
import pickle

class MLdrive:
        def get_dataset(endpoint, key, return_type=None):
            """Retrieve data from the user given endpoint. All endpoints can be retrieved by using this function with 'datasets'
            as the endpoint parameter. 
            
            :param endpoint: the name of the endpoint you want to hit (string)
            :param key:  your API key (string)
            :param return_type: type of return object (DataFrame, array, or dictionary). Default = DataFrame.  
            :return:  data from given endpoint
            """
            try:
                r = requests.get('http://34.231.99.140/api/' + endpoint + '/' + key)
                if return_type == None:
                    return pd.read_json(r.json()['result'])
                elif return_type.lower() == 'array':
                    return pd.read_json(r.json()['result']).to_numpy()
                elif return_type.lower() == 'dict':
                    return pd.read_json(r.json()['result']).to_dict()
            except(json.decoder.JSONDecodeError):
                return 'Error: Invalid API Key or Endpoint'
            except Exception as exception:
                return exception

        def save_dataframe(df, email, key):
            """Save the given dataframe to the server.  Note, your previously saved dataset will be overwritten.  
            
            :param df: dataframe that is being saved (dataframe)
            :param email: email used for registration that corresponds with API key (string)
            :param key:  your API key (string)
            :return: post response
            """
            try:
                return requests.post('http://34.231.99.140/api/save_dataset/'+email+'/'+key, json=df.to_dict(orient='records') )
            except(requests.exceptions.ChunkedEncodingError):
                return 'Error: Invalid API Key or Email'
            except(AttributeError):
                return 'Error: First Parameter is not a DataFrame'
            except Exception as exception:
                return exception            

        def get_my_dataset(email, key):
            """Load your last saved dataset.
            
            :param email: email used for registration that corresponds with API key (string)
            :param key:  your API key (string)
            :return: dataframe
            """
            try:
                r = requests.get('http://34.231.99.140/api/get_dataset/'+email+'/'+key)
                return pd.DataFrame.from_dict(r.json()['result'])  
            except(json.decoder.JSONDecodeError):
                return 'Error: Invalid API Key or Email'
            except Exception as exception:
                return exception
            
            
        def post_model(email, key, model):
            """Save your scikit-learn model.
            
            :param email: email used for registration that corresponds with API key (string)
            :param key:  your API key (string)
            :param model:  your machine learning model (Model)
            :return: post response
            """
            try:
                files = {'file': pickle.dumps(model)}
                if requests.post('http://34.231.99.140/api/save_model/{}/{}'.format(email, key), files=files):
                    return 'ok!'
                else:
                    return 'Failed, check email-key combo. Make sure you are passing in a model object.'
            except Exception as exception:
                return exception    
            
        def get_model(email, key):
            """Load your last saved model.
            
            :param email: email used for registration that corresponds with API key (string)
            :param key:  your API key (string)
            :return: Model
            """
            try:
                return pickle.loads(requests.get('http://34.231.99.140/api/load_model/{}/{}'.format(email,key)).content)
            except Exception as exception:
                return exception

        def send_dataset(email,key,exchange_key, df):
            """Send your dataframe to another user via their exchange_key
            
            :param email: email used for registration that corresponds with API key (string)
            :param key:  your API key (string)
            :param exchange_key:  the recepients exchange key (string)
            :param df:  the dataframe you want to send (dataframe)
            :return: post response
            """
            try:
                requests.post('http://34.231.99.140/api/send_dataset/{}/{}/{}'.format(key,email,exchange_key), json=df.to_dict(orient='records'))
            except Exception as exception:
                return exception

        def dataset_inbox(email,key):
            """Load dataframes that were sent to your inbox.
            
            :param email: email used for registration that corresponds with API key (string)
            :param key:  your API key (string)
            :return: dataframe (dataframe)
            """
            try:
                r = requests.get('http://34.231.99.140/api/dataset_inbox/{}/{}'.format(email,key))
                return pd.DataFrame(r.json()['result'])
            except Exception as exception:
                return exception
            
            
        def send_model(email,key,exchange_key, model):
            """Send your model to another user via their exchange_key
            
            :param email: email used for registration that corresponds with API key (string)
            :param key:  your API key (string)
            :param exchange_key:  the recepients exchange key (string)
            :param model:  the model you want to send (dataframe)
            :return: post response
            """
            try:
                files = {'file': pickle.dumps(model)}
                return requests.post('http://34.231.99.140/api/send_model/{}/{}/{}'.format(key,email,exchange_key), files=files)
            except Exception as exception:
                return exception
            
        def model_inbox(email,key):
            """Load models that were sent to your inbox.
            
            :param email: email used for registration that corresponds with API key (string)
            :param key:  your API key (string)
            :return: model (model)
            """
            try:
                return pickle.loads(requests.get('http://34.231.99.140/api/model_inbox/{}/{}'.format(email,key)).content)
            except Exception as exception:
                return exception
            
        def change_exchange_key(email,key,exchange_key, new_exchange_key):
            """Change your exchange key
            
            :param email: email used for registration that corresponds with API key (string)
            :param key:  your API key (string)
            :param exchange_key:  current exchange key (string)
            :param new_exchange_key:  new exchange key (string)
            :return: post response
            """
            try:
                requests.post('http://34.231.99.140/api/change_exchange_key/{}/{}/{}/{}'.format(email,key,exchange_key, new_exchange_key))
            except Exception as exception:
                return exception               
