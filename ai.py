import os
import openai

def artificalAi(question):
 openai.api_key ='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'
 promp=question
 
 response = openai.Completion.create(
   model="text-davinci-003",
   prompt=question,
   temperature=1,
   max_tokens=256,
   top_p=1,
   frequency_penalty=0,
   presence_penalty=0
 )
 
 print(response.choices[0].text)
 f=open(f'./{promp.split()[-1]}.txt','w')
 f.write("Sorry Can't Contact With ai")
 res=response.choices[0].text
 f.close()
 print("Your Repsonse Has been Saved to ",promp.split()[-1],".txt")
 return res 
