

```python
import nltk
```


```python
from nltk.corpus import wordnet
nltk.download('wordnet')
```

    [nltk_data] Downloading package wordnet to
    [nltk_data]     C:\Users\Tony\AppData\Roaming\nltk_data...
    [nltk_data]   Package wordnet is already up-to-date!
    




    True




```python
word_list1 = ["boot", "raincoat", "shoe", "shirt"]
word_list2 = ["clothing", "suit", "pin", "hair"]
```


```python
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
```

    -----------------------------------------------------------------------
    組合 1 : boot vs. clothing
    boot 的語意 1:
    footwear that covers the whole foot and lower leg, 
    
    clothing 的語意 1:
    a covering designed to be worn on a person's body, 
    
    相似度0.800000
    共同祖先 : [Synset('covering.n.02')] 
    
    
    -----------------------------------------------------------------------
    組合 2 : raincoat vs. suit
    raincoat 的語意 1:
    a water-resistant coat, 
    
    suit 的語意 1:
    a set of garments (usually including a jacket and trousers or skirt) for outerwear all of the same fabric and color, 
    
    相似度0.818182
    共同祖先 : [Synset('garment.n.01')] 
    
    
    -----------------------------------------------------------------------
    組合 3 : shoe vs. pin
    shoe 的語意 4:
    a restraint provided when the brake linings are moved hydraulically against the brake drum to retard the wheel's rotation, 
    
    pin 的語意 9:
    a small slender (often pointed) piece of wood or metal used to support or fasten or attach things, 
    
    相似度0.842105
    共同祖先 : [Synset('restraint.n.06')] 
    
    
    -----------------------------------------------------------------------
    組合 4 : shirt vs. hair
    shirt 的語意 1:
    a garment worn on the upper half of the body, 
    
    hair 的語意 5:
    cloth woven from horsehair or camelhair; used for upholstery or stiffening in garments, 
    
    相似度0.625000
    共同祖先 : [Synset('artifact.n.01')] 
    
    
    
