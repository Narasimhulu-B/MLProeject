from itertools import groupby
from copy import deepcopy

def get_oddstr(strinput):
    try:
        print(strinput)
        status=True
        ref_str= deepcopy(strinput)
        while status:
            length=0
            cout=0
            strinput=deepcopy( ref_str)
            ref_str=''
            for k, g in groupby(strinput):
                l=list((k for _ in g))
                #print(k,l)
                length=len(l)
                if length%2==0:
                    cout=cout+1
                else:
                    ref_str=ref_str+''.join(l)
            if cout==0:
                status=False

        print(ref_str)
    except Exception as ex :
        pass

if __name__=="__main__":
    get_oddstr("aaabbbaaabbabddccc")
    get_oddstr("yyybbzzzbuiioop")
