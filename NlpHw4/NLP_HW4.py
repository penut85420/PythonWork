
# coding: utf-8

# In[1]:


import nltk


# In[2]:


from nltk.corpus import wordnet
nltk.download('wordnet')


# In[3]:


word_list1 = ["boot", "raincoat", "shoe", "shirt"]
word_list2 = ["clothing", "suit", "pin", "hair"]


# In[4]:


for k in range(0, 4):
    print("-----------------------------------------------------------------------")
    print("組合", k+1, ":", word_list1[k], "vs.", word_list2[k])
    len1 = len(wordnet.synsets(word_list1[k],'n'))
    len2 = len(wordnet.synsets(word_list2[k],'n'))
    
    str1 = word_list1[k] + ".n."
    str2 = word_list2[k] + ".n."
    
    i_max = 0
    j_max = 0
    similarity_max = 0
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            d = wordnet.synset(str1 + str(i))
            g = wordnet.synset(str2 + str(j))
            if(d.wup_similarity(g) > similarity_max):
                i_max = i
                j_max = j
                similarity_max = d.wup_similarity(g)
    
    
    print("%s 的語意 %d:\n%s, \n\n%s 的語意 %d:\n%s, \n\n相似度%6f" %(word_list1[k], i_max, wordnet.synset(str1 + str(i_max)).definition(), word_list2[k], j_max, wordnet.synset(str2 + str(j_max)).definition(), similarity_max))
    print("共同祖先 :", wordnet.synset(str1 + str(i_max)).lowest_common_hypernyms(wordnet.synset(str2 + str(j_max))), "\n\n")

