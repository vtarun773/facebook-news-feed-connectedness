from tkinter import *
from tkinter import ttk
from datetime import datetime

height = 0
LikeScore = 44721359
CommentScore = 77777377
LikeButton=[]
CommentButton=[]
#m=[["Hello",4,2,'2020-11-20 12:40:33',0],["This is a post",3,2,'2017-1-1 11:44:33',0],["Wanna see more?",5,1,'2017-12-20 23:40:33',0],["timestamp() function return the ",15,3,'2018-11-20 12:40:33',0]]

my_list=[]
for line in open("sachin_file.txt",encoding='utf8'):
    # print(line.split('|'))
     temp = line.split('|')
     temp[1]=int(temp[1])
     temp[2]=int(temp[2])
     temp[4]=int(temp[4])
     my_list.append(temp)

m=my_list

def insertsort():
    for i in range(1, len(m)):

        key = m[i][4]
        temp = m[i]

        j = i - 1
        while j >= 0 and key > m[j][4]:
            m[j + 1] = m[j]
            j -= 1
        m[j + 1] = temp

def stamp():
    timestamp = datetime.timestamp(datetime.now())
    for i in m:
        if type(i[3]) is str:
            i[3] = datetime.timestamp(datetime.strptime(i[3], '%Y-%m-%d %H:%M:%S'))

def edgerank():
    stamp()
    timestamp=datetime.timestamp(datetime.now())
    for i in m:
        i[4] = ((i[1]*LikeScore + i[2]*CommentScore) / (timestamp-i[3]))
    insertsort()
    print(m)



root = Tk()

root.geometry("550x500")
root.maxsize(550,2000)
root.minsize(550,100)
root.title("EDGERANK algorithm on posts")




f1 = Frame(root)
f1.pack(fill=BOTH,expand=1)

f2 = Canvas(f1)
f2.pack(side=LEFT,fill=BOTH,expand=1)

my_scrollbar = ttk.Scrollbar(f1,orient=VERTICAL,command=f2.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)

f2.configure(yscrollcommand=my_scrollbar.set)
f2.bind('<Configure>',lambda e:f2.configure(scrollregion = f2.bbox("all")))

new_root=Frame(f2)



f2.create_window((0,0),window=new_root,anchor="nw")

new_canvas=Canvas(new_root,width=500,height=2000)
new_canvas.pack()

#update number of likes
def LIKE(id):
    m[id][1]+=1


#comment window
def COMMENT(id):
    comment=Tk()
    comment.geometry("270x100")
    comment.title("Comment")
    entry = Entry(comment)
    entry.pack(pady=15)
    f1 = Frame(comment, bg="white", borderwidth=0, relief=FLAT)
    f1.pack(side=BOTTOM)

    Button(f1,text="comment",command=lambda a=id:COMMENT2(a), relief=FLAT).pack()

    comment.mainloop()
#update the number of comments
def COMMENT2(id):
        m[id][2]+=1


def mylist():
    Clear()
    edgerank()
    j=0
    for i in m:
        function(i[0],i[1],i[2],j)
        j+=1

def mylist2():
    Clear()
    mylist()

def test1():
    return "hello"

def Clear():
    global height
    LikeButton.clear()
    CommentButton.clear()
    new_canvas.delete("all")
    height=0

def NewPost(post):
    timestamp = datetime.timestamp(datetime.now())
    m.append([post,1,1,timestamp,0])
    print("NEW POST UPDATED SUCCESSFULLY")
#post window
def Post():
    post = Tk()
    post.geometry("300x100")
    post.title("What's in your mind?")
    entry = Entry(post,width=45,borderwidth=2)
    entry.pack(pady=20)

    f1 = Frame(post, bg="white", borderwidth=0, relief=FLAT)
    f1.pack(side=BOTTOM)

    Button(f1, text="post",command=lambda :NewPost(entry.get()), relief=FLAT).pack()

    post.mainloop()

def function(string,like,comment,j):
    #f2 is canvas
    global height
    new_canvas.create_rectangle(0,height,500,height+50,outline="#f5f5f2")
    new_canvas.create_text(10,height+20, text=string,anchor='w')
    
    LikeButton.append(Button(f2, text="LIKE("+str(like-1)+")",command=lambda l=j:LIKE(l) , anchor=W))
    LikeButton[j].configure(width=8, activebackground="#33B5E5", relief=FLAT)
    button1_window = new_canvas.create_window(10,height+51, anchor=NW, window=LikeButton[j])

    CommentButton.append(Button(f2, text="comment("+str(comment-1)+")",command=lambda c=j:COMMENT(c), anchor=W))
    CommentButton[j].configure(width=15, activebackground="#33B5E5", relief=FLAT)
    button2_window = new_canvas.create_window(70, height+51, anchor=NW, window=CommentButton[j])

    height = height+80

#f1 is frame
Button(f1,text="Refresh",command=mylist,relief=FLAT).pack(side=RIGHT,anchor="ne")

Button(f1,text="Clear",command=Clear,relief=FLAT).pack(side=RIGHT,anchor="ne")

Button(f1,text="New Post",command=Post,relief=FLAT).pack(side=RIGHT,anchor="ne")

root.mainloop()

