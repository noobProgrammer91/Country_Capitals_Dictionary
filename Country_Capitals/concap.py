#creating an empty dictionary
emptyDict ={} 

#reading a text file from a folder that consists of a list of countries and their capitals.

def dict_engine():
    with open('E:/python/country_capitals/lst.txt','r') as src:
        file = src.readlines()
        # newFile = file.split('\t')

    for items in file:
        keyVal = items.strip('\n').split('\t')
        emptyDict[keyVal[0]] =keyVal[1]

#main part of the encyclopedo

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
    
    




