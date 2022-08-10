greeting = """Welcome to Text-Based Wordle
It can be played offline and is console based"""
answer="WHINE"
import json
import time
class File():
    def __init__(self, file_name):
        self.file_obj = open(file_name,"r")
        self.file_2_obj=open(file_name,"w")
    def __enter__(self):
        return (self.file_obj,self.file_2_obj)
    def __exit__(self, type, value, traceback):
        self.file_obj.close()
        self.file_2_obj.close()

def load_guess(info):
    return info["guess_num"]
def load_prev_outputs(info):
    return info["prev_outputs"]

def timet():
    r=time.localtime()
    return [r.tm_year,r.tm_mon,r.tm_mday]
def init(data):
    cur_time=timet()
    for i in data:
        #print(i)
        if data[i]["timet"]==cur_time:
            r=data[i]
            q=i
            break
    else:
        return len(data)
    return r,q
def guess(guess):
    green = "🟩"
    red="🟥"
    blue = "🟦"
    output=""
    for i,(letter1,letter2) in enumerate(zip(guess,answer)):
        if letter1 == letter2:
            output+=green
            continue
            
        if (letter1 not in answer) or (letter1 in guess[:i] and len(list(filter(lambda x:x==letter1,answer)))==2):
            output+=red
            continue
        if not (letter1 == letter2) and (letter1 in answer):
            output+=blue
    return output
def main(data,f,g):
    info1=init(data)
    if isinstance(info1,int):
        r=info1
        data+=[{}]
        data[r]["curr_guess"]=0
        data[r]["prev_outputs"]=[]
        idx=r
    else:
        info,idx=info1

    saved=True
    if isinstance(info1,int):
        saved=False
    if saved:
        guess_num=load_guess(info)
        prev_outputs=load_prev_outputs(info)
    else:
        guess_num=0
        prev_outputs=[]
    #print(info)
    if not saved:
        print(greeting)
    prefix=["st","nd","rd","th","th","th"]
    for i in range(guess_num,6):
        guessf=input(f'Enter your {i+1}{prefix[i]} guess: ')
        data[idx]["curr_guess"]=guess_num+1
        data[idx]["prev_outputs"]+=[guess(guessf)]
        d=json.dumps(data)
        #print(d)
        g.write(d)
        print(guess(guessf))
        if guessf == answer:
            print("You won!")
            break
if __name__ == "__main__":
    print(open("/home/otisheggem/WordleHelp.json","r").read())
    with open("/home/otisheggem/WordleHelp.json","r") as f:
        print(f.read())
        print(f.read())

        with open("/home/otisheggem/WordleHelp.json","w") as g:
            print(f.read())
            main(json.load(f),f,g)










