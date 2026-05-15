import random 
from string import   punctuation 
from collections import  defaultdict 

class MarkovChain: 
    def __init__(self): 
        self.graph = defaultdict(list) 

    def _tokenize(self, text): 
        return(
            text.translate(str.maketrans("","", punctuation + "1234567890"))
            .replace("\n", " ")
            .split(  )
        )
    def train(self, text): 
        tokens = self._tokenize(text) 
        for i, token in enumerate(tokens): 
            if(len(tokens) - 1) == i: 
                break 
            self.graph[token].append(tokens[i + 1]) 
    
    def generate(self, prompt , length =10):
        # get the last token form the prompt 
        current = self._tokenize(prompt) [-1] 
        #initialize the output 
        output = prompt 
        for i in range(length): 
            #look up the options in the graph dictionary 
           options = self.graph.get(current , []) 
           if not options: 
               break 
           # use random.choice method to pick a current option 
           current = random.choice(options)
           #add the random choice to output the string 
           output += f" {current}"
        return output   
        # This is how your code will be called.
# Your answer should be the largest value in the numbers list.
# You can edit this code to try different testing cases.

text = """ [Verse 1]
Party girls don't get hurt
Can't feel anythin', when will I learn?
I push it down, I push it down
I'm the one for a good time call
Phone's blowin' up, ringin' my doorbell
I feel the love, I feel the love

[Pre-Chorus]
One, two, three, one, two, three, drink
One, two, three, one, two, three, drink
One, two, three, one, two, three, drink
Throw 'em back 'til I lose count

[Chorus]
I'm gonna swing from the chandelier
From the chandelier
I'm gonna live like tomorrow doesn't exist
Like it doesn't exist
I'm gonna fly like a bird through the night
Feel my tears as they dry
I'm gonna swing from the chandelier
From the chandelier

[Post-Chorus]
But I'm holdin' on for dear life
Won't look down, won't open my eyes
Keep my glass full until mornin' light
'Cause I'm just holdin' on for tonight
Help me, I'm holdin' on for dear life
Won't look down, won't open my eyes
Keep my glass full until mornin' light
'Cause I'm just holdin' on for tonight, on for tonight  

[Verse 1]
You only see what your eyes want to see
How can life be what you want it to be?
You're frozen when your heart's not open
You're so consumed with how much you get
You waste your time with hate and regret
You're broken when your heart's not open

[Chorus]
Mmm-mmm, if I could melt your heart
Mmm-mmm, we'd never be apart
Mmm-mmm, give yourself to me
Mmm-mmm, you hold the key

[Verse 2]
Now there's no point in placing the blame
And you should know I suffer the same
If I lose you, my heart will be broken
Love is a bird, she needs to fly
Let all the hurt inside of you die
You're frozen, when your heart's not open

[Chorus]
Mmm-mmm, if I could melt your heart
Mmm-mmm, we'd never be apart
Mmm-mmm, give yourself to me
Mmm-mmm, you hold the key
"""

chain = MarkovChain()   #chain = MarkovChain()  
chain.train(text)        #chain.train(text)      #sample_prompt = "I was"
print(chain.generate("I ", 4 ) )   #print(chain.generate(sample_prompt))

result = chain.generate("I'm gonna")   #result = chain.generate(sample_prompt)
