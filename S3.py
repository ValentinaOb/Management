import tkinter as tk
from tkinter import filedialog, scrolledtext
from tkinter import ttk



def start(v):
    global a,b,small,k,key,text
    if v==1:
        try:
            a= int(a_entry.get())
        except:
            a=3
        try:
            b=int(b_entry.get())
        except:
            b=5 
        text=input_text.get("1.0", tk.END)
    
    elif v==2:
        try:
            k= int(k_entry.get())
        except:
            k=12
        try:
            key=int(key_text.get())
        except:
            key='DIPLOMAT'

        text=input_text1.get("1.0", tk.END)

    elif v==3:
        try:
            a= int(a_entry.get())
        except:
            a=3
        try:
            b=int(b_entry.get())
        except:
            b=5 
        text=input_text2.get("1.0", tk.END)
    
    else:
        try:
            k= int(k_entry.get())
        except:
            k=12
        try:
            key=int(key_text.get())
        except:
            key='DIPLOMAT'

        text=input_text3.get("1.0", tk.END)
        
    small = alphabet.lower().split(' ')


def alphab_code(v):
    size=len(small)
    k=-1
    new_el.clear()
    
    for i in small:
        k+=1
        new = a*small.index(i)+b
        if new>=size:
            new=new%size
        new_el.append(small[new])   #get char
        #new_el.append(new)   #get index

    
    if v==1:
        letters.set('   '.join(new_el).upper())
        new_alphabet_label.config(text=letters.get())
    else:
        letters2.set('   '.join(new_el).upper())
        new_alphabet_label2.config(text=letters2.get())

def coder():
    start(1)
    alphab_code(1)
    output(new_el,1)

def key_alphab(v):
    alph=alphabet.lower().split(' ')
    new_el.clear()

    key_arr=list(dict.fromkeys(key.lower()))
    
    for i in key_arr:
        alph.remove(i)

    #print('S: ',alph)
        
    last_elts = alph[-k:]
    new_el.extend(last_elts)
    for i in last_elts:
        alph.remove(i)

    #print('L: ',last_elts)
    new_el.extend(key.lower())
    new_el.extend(alph)
    #print("N: ",new_el)

    if v==2:
        letters1.set('   '.join(new_el).upper())
        new_alphabet_label1.config(text=letters1.get())
    else:
        letters3.set('   '.join(new_el).upper())
        new_alphabet_label3.config(text=letters3.get())


def key_coder():
    start(2)
    key_alphab(2)
    output(new_el,2)
    

def de_coder():
    start(3)
    alphab_code(3)
    de_output(new_el,1)

def de_key_coder():
    start(4)
    key_alphab(4)
    de_output(new_el,2)

def de_output(new_el,v):
    #alphabet    
    global small, text      
    new_txt.clear()

    #CODER  result
    for char in text:
        if char.isalpha():
            indx=new_el.index(char)
            new_txt.append(small[indx])
        else:
            new_txt.append(char)
    
    # Update output text widget
    if v==1:
        output_text2.delete("1.0", tk.END)
        output_text2.insert("1.0", ''.join(new_txt))

    else:
        output_text3.delete("1.0", tk.END)
        output_text3.insert("1.0", ''.join(new_txt))
    
    return ''.join(new_txt)



def output(new_el,v):
    #alphabet    
    global small, text      
    new_txt.clear()
    '''count=-1
    for i in small:
        count+=1
        print(i,' - ', new_el[count])'''

    #CODER  result
    for char in text:
        if char.isalpha():
            '''indx1=new_el[indx]
            new_txt.append(small[indx1])''' #if get inx
            indx=small.index(char)
            new_txt.append(new_el[indx])
        else:
            new_txt.append(char)
    
    # Update output text widget
    if v==1:
        output_text.delete("1.0", tk.END)
        output_text.insert("1.0", ''.join(new_txt))

    else:
        output_text1.delete("1.0", tk.END)
        output_text1.insert("1.0", ''.join(new_txt))
    
    return ''.join(new_txt)


new_el=[]
new_txt=[]
text=""
k=0
key=""
a=0
b=0
small=[]

'''
#text="Hello World! This task was performed for the discipline related to information security"
text='night'
'''
alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"

''' 
key = 'diplomat'
k=5
text='SEND MORE MONEY'

text = text.lower()'''

#coder()
#key_coder()


def open_file():
    #global text
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            #text = file.read().lower()
            input_text.delete("1.0", tk.END)
            input_text.insert(tk.END, file.read().lower())

def open_file1():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            input_text1.delete("1.0", tk.END)
            input_text1.insert(tk.END, file.read().lower())
def open_file2():
    #global text
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            #text = file.read().lower()
            input_text2.delete("1.0", tk.END)
            input_text2.insert(tk.END, file.read().lower())
def open_file3():
    #global text
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            #text = file.read().lower()
            input_text3.delete("1.0", tk.END)
            input_text3.insert(tk.END, file.read().lower())
            

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(output_text.get("1.0", tk.END))
def save_file1():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(output_text1.get("1.0", tk.END))
def save_file2():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(output_text2.get("1.0", tk.END))
def save_file3():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(output_text3.get("1.0", tk.END))


#
root = tk.Tk()
root.title("Coder")
root.geometry("1000x500")

tabControl = ttk.Notebook(root) 
  
tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 
tab3 = ttk.Frame(tabControl) 
tab4 = ttk.Frame(tabControl) 
  
tabControl.add(tab1, text ='Coder') 
tabControl.add(tab2, text ='Key Coder')
tabControl.add(tab3, text ='DE Coder') 
tabControl.add(tab4, text ='DE Key Coder')
tabControl.pack(expand = 1, fill ="both")  

ttk.Label(tab1, text ="Welcome").grid(column = 0, row = 0, padx = 30, pady = 30)  
ttk.Label(tab2, text ="Lets ").grid(column = 0, row = 0, padx = 30, pady = 30)  


alph_numbers = tk.StringVar()
numbers = '  '.join(map(str, (lambda: range(26))()))
alph_numbers.set(numbers)

alph_letters = tk.StringVar()
alph_letters.set(alphabet.replace(' ', '   '))

letters = tk.StringVar(value="")
# create a label widget
numb_label = tk.Label(tab1, textvariable = alph_numbers).grid(row=4, column=2, sticky='e')
alphabet_label = tk.Label(tab1, textvariable = alph_letters).grid(row=5, column=2, sticky='e')
new_alphabet_label = tk.Label(tab1, textvariable = letters)
new_alphabet_label.grid(row=6, column=2, sticky='e')


tk.Label(tab1, text="Number of symbols").grid(row=0, column=0, padx=5, pady=5, sticky='w')
tk.Entry(tab1, width=5, justify='center', state='disabled', textvariable=tk.StringVar(value='26')).grid(row=0, column=1, padx=5, pady=5)

tk.Label(tab1, text="Parameters").grid(row=0, column=2, columnspan=2, padx=5, pady=5, sticky='w')
tk.Label(tab1, text="a=").grid(row=0, column=2, padx=2, pady=5, sticky='e')
a_entry = tk.Entry(tab1, width=3, justify='center')
a_entry.grid(row=0, column=3, padx=5, pady=5)
tk.Label(tab1, text="b=").grid(row=0, column=4, padx=2, pady=5, sticky='e')
b_entry = tk.Entry(tab1, width=3, justify='center')
b_entry.grid(row=0, column=5, padx=5, pady=5)


tk.Button(tab1, text="Select file", command=open_file).grid(row=1, column=0, padx=5, pady=5)
tk.Button(tab1, text="Coder", command=coder).grid(row=1, column=1, padx=5, pady=5)
tk.Button(tab1, text="Save file", command=save_file).grid(row=1, column=2, padx=5, pady=5)

input_text = scrolledtext.ScrolledText(tab1, width=50, height=10)
input_text.grid(row=2, column=0, columnspan=3, padx=5, pady=5)


output_text = scrolledtext.ScrolledText(tab1, width=40, height=10)
output_text.grid(row=2, column=3, columnspan=3, padx=5, pady=5)
output_text.insert("1.0", '')
#output_text.config(state='disabled')


tk.Label(tab2, text="Parameters").grid(row=0, column=2, columnspan=2, padx=5, pady=5, sticky='w')

tk.Label(tab2, text="k=").grid(row=0, column=2, padx=2, pady=5, sticky='e')
k_entry = tk.Entry(tab2, width=3, justify='center')
k_entry.grid(row=0, column=3, padx=5, pady=5)

tk.Label(tab2, text="key=").grid(row=0, column=4, padx=2, pady=5, sticky='e')

key_text = scrolledtext.ScrolledText(tab2, width=12, height=1)
key_text.grid(row=0, column=5, columnspan=1, padx=5, pady=5)
#key_entry = tk.Entry(tab2, width=3, justify='center')
#key_entry.grid(row=0, column=6, padx=5, pady=5)

letters1 = tk.StringVar(value="")

numb_label1 = tk.Label(tab2, textvariable = alph_numbers).grid(row=4, column=2, sticky='e')
alphabet_label1 = tk.Label(tab2, textvariable = alph_letters).grid(row=5, column=2, sticky='e')
new_alphabet_label1 = tk.Label(tab2, textvariable = letters1)
new_alphabet_label.grid(row=6, column=2, sticky='e')


tk.Button(tab2, text="Select file", command=open_file1).grid(row=1, column=0, padx=5, pady=5)
tk.Button(tab2, text="Coder", command=key_coder).grid(row=1, column=1, padx=5, pady=5)
tk.Button(tab2, text="Save file", command=save_file1).grid(row=1, column=2, padx=5, pady=5)

input_text1 = scrolledtext.ScrolledText(tab2, width=50, height=10)
input_text1.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

output_text1 = scrolledtext.ScrolledText(tab2, width=40, height=10)
output_text1.grid(row=2, column=3, columnspan=3, padx=5, pady=5)
output_text1.insert("1.0", '')





#Decoder
letters2 = tk.StringVar(value="")

numb_label = tk.Label(tab3, textvariable = alph_numbers).grid(row=4, column=2, sticky='e')
alphabet_label = tk.Label(tab3, textvariable = alph_letters).grid(row=5, column=2, sticky='e')
new_alphabet_label2 = tk.Label(tab3, textvariable = letters2)
new_alphabet_label2.grid(row=6, column=2, sticky='e')


tk.Label(tab3, text="Number of symbols").grid(row=0, column=0, padx=5, pady=5, sticky='w')
tk.Entry(tab3, width=5, justify='center', state='disabled', textvariable=tk.StringVar(value='26')).grid(row=0, column=1, padx=5, pady=5)

tk.Label(tab3, text="Parameters").grid(row=0, column=2, columnspan=2, padx=5, pady=5, sticky='w')
tk.Label(tab3, text="a=").grid(row=0, column=2, padx=2, pady=5, sticky='e')
a_entry2 = tk.Entry(tab3, width=3, justify='center')
a_entry2.grid(row=0, column=3, padx=5, pady=5)
tk.Label(tab3, text="b=").grid(row=0, column=4, padx=2, pady=5, sticky='e')
b_entry2 = tk.Entry(tab3, width=3, justify='center')
b_entry2.grid(row=0, column=5, padx=5, pady=5)


tk.Button(tab3, text="Select file", command=open_file2).grid(row=1, column=0, padx=5, pady=5)
tk.Button(tab3, text="Coder", command=de_coder).grid(row=1, column=1, padx=5, pady=5)
tk.Button(tab3, text="Save file", command=save_file2).grid(row=1, column=2, padx=5, pady=5)

input_text2 = scrolledtext.ScrolledText(tab3, width=50, height=10)
input_text2.grid(row=2, column=0, columnspan=3, padx=5, pady=5)


output_text2 = scrolledtext.ScrolledText(tab3, width=40, height=10)
output_text2.grid(row=2, column=3, columnspan=3, padx=5, pady=5)
output_text2.insert("1.0", '')


#

tk.Label(tab4, text="Parameters").grid(row=0, column=2, columnspan=2, padx=5, pady=5, sticky='w')

tk.Label(tab4, text="k=").grid(row=0, column=2, padx=2, pady=5, sticky='e')
k_entry = tk.Entry(tab4, width=3, justify='center')
k_entry.grid(row=0, column=3, padx=5, pady=5)

tk.Label(tab4, text="key=").grid(row=0, column=4, padx=2, pady=5, sticky='e')

key_text = scrolledtext.ScrolledText(tab4, width=12, height=1)
key_text.grid(row=0, column=5, columnspan=1, padx=5, pady=5)
#key_entry = tk.Entry(tab2, width=3, justify='center')
#key_entry.grid(row=0, column=6, padx=5, pady=5)

letters3 = tk.StringVar(value="")

numb_label = tk.Label(tab4, textvariable = alph_numbers).grid(row=4, column=2, sticky='e')
alphabet_label = tk.Label(tab4, textvariable = alph_letters).grid(row=5, column=2, sticky='e')

new_alphabet_label3 = tk.Label(tab4, textvariable = letters3)
new_alphabet_label3.grid(row=6, column=2, sticky='e')


tk.Button(tab4, text="Select file", command=open_file3).grid(row=1, column=0, padx=5, pady=5)
tk.Button(tab4, text="Coder", command=de_key_coder).grid(row=1, column=1, padx=5, pady=5)
tk.Button(tab4, text="Save file", command=save_file3).grid(row=1, column=2, padx=5, pady=5)

input_text3 = scrolledtext.ScrolledText(tab4, width=50, height=10)
input_text3.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

output_text3 = scrolledtext.ScrolledText(tab4, width=40, height=10)
output_text3.grid(row=2, column=3, columnspan=3, padx=5, pady=5)
output_text3.insert("1.0", '')






root.mainloop()