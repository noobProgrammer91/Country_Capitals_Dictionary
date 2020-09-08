# Countries & Capitals Encyclopedia

This is a small python project that creates a mini encyclopedia of countries and their capitals. When an user inputs the name of a country the capital is received as an output.
## Setup
Create a text file with the names of countries and capitals. Place it inside a folder together with the python file.



## Usage

```#creating an empty dictionary
emptyDict ={} 

#reading a text file from a folder that consists of a list of countries and their capitals.

def dict_engine():
    with open('E:/python/country_capitals/lst.txt','r') as src:
        file = src.readlines()
        # newFile = file.split('\t')

    for items in file:
        keyVal = items.strip('\n').split('\t')
        emptyDict[keyVal[0]] =keyVal[1]

#main part of the encyclopedia that takes the country name as user input and returns the capital

def main():

    while True:
        ask = input("Enter a country: ").upper()

        if ask not in emptyDict.keys():
            print("Please check your spelling")
            ask = input("Enter a country: ").upper()
        else:
            ans = (f'The capital of {ask} is {emptyDict.get(ask)}')
            print(ans)
            
            
dict_engine()
main()
    
    
```

## Contributing
I am a beginner and I would like suggestions regarding any changes to my code. Do let me know if the code can be modified in any other way.

## Licencing & Copyright
MIT License

Copyright (c) [2020] [Swastik Sarkar]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

