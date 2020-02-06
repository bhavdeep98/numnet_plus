#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd
import json


# In[42]:


snli_train_list = []
with open("snli_1.0/snli_1.0_dev.jsonl") as train_file:
    snli_train_list = list(train_file)


# In[43]:


# snli_train_list


# In[44]:


snli_train_data = []
for item in snli_train_list:
    snli_train_data.append(json.loads(item))


# In[45]:


# snli_train_data


# In[46]:


data = pd.DataFrame()


# In[47]:


passages = {}
qa_dict = {}

for item in snli_train_data:
    qa_pair = {}
    answer = {}
    key = item['captionID']
    passages[key] = item['sentence1']
#     temp_current['passage']  = item['sentence1']
    qa_pair['question'] = item['sentence2'] + "entailment or contradiction or neutral?"
    answer['number'] = ""
    answer['date'] = dict.fromkeys({'day','month','year'},"")
    if item['gold_label'] in ['entailment','neutral','contradiction']:
        answer['spans'] = [item['gold_label']]
    else:
        continue
    qa_pair['answer'] = answer
#     qa_pair['validated_answers'] = [answer,answer]
    qa_pair['query_id'] = item['pairID']
    if key in qa_dict.keys():
        qa_dict[key].append(qa_pair)
    else:
        qa_dict[key]=[qa_pair]


# In[48]:


temp_dict = {}
for key in passages.keys():
    unified_dict = {}
    unified_dict['passage'] = passages[key]
    if len(qa_dict[key])!=0:
        unified_dict['qa_pairs'] = qa_dict[key]
    else:
        print(qa_dict)
        print(key)
        print(passages[key])
    unified_dict['wiki_url'] = ""
    temp_dict[key] = unified_dict


# In[49]:


# temp_dict


# In[50]:


with open("drop_dataset/drop_dataset_dev.json",'w') as train_file:
    json.dump(temp_dict,train_file)


# In[ ]:




