#vrinda joshi
#ics208
#gui assigment

#this program is game where the user is assigned the role of santa claus. santa's sleigh can only take 5/9 reindeer, and therefore the user has to choose the right 5 \
#for the situation. the user plays 3 rounds

import tkinter as tk
import tkinter.messagebox as mb

#assign a variable to repeated colours
green = "#1E792C"
red = "#C30F16"

#create challenge variables
global challenges_completed
challenges_completed = 0
global reputation
reputation = 100
    
#reindeer message box functions

def about_rudolph():
    mb.showinfo('About Rudolph', "Rudolph takes his Vitamin C!! He's always glowing! Rudolph's super power is that his nose glows so bright, one can see in the \
darkest of places!! The only issue is that he isn't the fastest, but- he's working on that!")
    
def about_prancer():
    mb.showinfo('About Prancer', "Prancer's specialty is her super high jumps! She can get over mountains easy peasy! Except her appetite can \
sometimes get annoying..")
    
def about_dancer():
    mb.showinfo('About Dancer', "Our dearest Dancer is a bundle of energy, and can motivate the team to keep going.")
    
def about_dasher():
    mb.showinfo('About Dasher', "Our local Usain Bolt, Dasher can run almost as fast as the speed of light!! His stamina could use some work, but hey, he's a \
sprinter!")
    
def about_comet():
    mb.showinfo('About Comet', "Comet, like her name, can withstand the coldest of temperatures!")
    
def about_vixen():
    mb.showinfo('About Vixen', "Vixen, our very own beauty pagent winner, has the power to make anything heat up.")
    
def about_blixem():
    mb.showinfo('About Blixem', "Blixem has a knack for all sports, including swimming, running, tennis, basketball, weightlifting- you name it!")
    
def about_cupid():
    mb.showinfo('About Cupid', "Cupid can reassure anyone and everyone that its gonna be okay.")
    
def about_dunder():
    mb.showinfo('About Dunder', "Dunder always gives the best advice, and his super smarts and resourcefulness always come in handy")


#wipe main window function
def refresh():
    window.destroy()
    window.__init__()

#seperate key functions + variables from proram code
#####################################################################################################################################################################

#define game over
def game_over():

    #set window as needed
    window.title("Filling in the Spirit")
    window.configure(bg = "#FEFBEA")
    window.geometry("400x175")

    #make first frame
    letter_h_frame = tk.Frame(window, bg = "#FEFBEA")

    #make space on top (format)
    letter_h_label = tk.Label(letter_h_frame, text = "   ", fg = green, bg = "#FEFBEA", font=("Garamond", 18))
    letter_h_label.pack()

    #code message
    letter_t_frame = tk.Frame(window, bg = "#FEFBEA")
    winletm = ("Dear", name,",") #.get didnt work for me in this case
    letter_t_label = tk.Label(letter_t_frame, text = winletm, fg = green, bg = "#FEFBEA", font=("Garamond", 10)) 
    letter_t_label1 = tk.Label(letter_t_frame, text = "We're afraid you've caused too much harm, and your", fg = green, bg = "#FEFBEA", font=("Garamond", 10))
    letter_t_label2 = tk.Label(letter_t_frame, text = "gig as Santa will have to be terminated immediately.", fg = green, bg = "#FEFBEA", font=("Garamond", 10))
    letter_t_label3 = tk.Label(letter_t_frame, text = "P.S. You'll probably find yourself on the naughty ", fg = green, bg = "#FEFBEA", font=("Garamond", 9))
    letter_t_label4 = tk.Label(letter_t_frame, text = "list this year.", fg = green, bg = "#FEFBEA", font=("Garamond", 9))

    #pack message label
    letter_t_label.pack()
    letter_t_label1.pack()
    letter_t_label2.pack()
    letter_t_label3.pack()
    letter_t_label4.pack()

    #pack frames
    letter_h_frame.pack()
    letter_t_frame.pack()

#define win 
def win():

    #set window as needed
    window.title("Filling in the Spirit")
    window.configure(bg = "#FEFBEA")
    window.geometry("400x230")

    #make space on top (format)
    letter_h_frame = tk.Frame(window, bg = "#FEFBEA")
    letter_h_label = tk.Label(letter_h_frame, text = "   ", fg = red, bg = "#FEFBEA", font=("Garamond", 18))
    letter_h_label.pack()

    #make space on top (format)
    letter_t_frame = tk.Frame(window, bg = "#FEFBEA")
    winletm = ("Dear", name,"x")
    letter_t_label = tk.Label(letter_t_frame, text = winletm, fg = red, bg = "#FEFBEA", font=("Garamond", 10))
    letter_t_label1 = tk.Label(letter_t_frame, text = "From everyone at the North Pole, we'd like", fg = red, bg = "#FEFBEA", font=("Garamond", 10))
    letter_t_label2 = tk.Label(letter_t_frame, text = "to give you a big thanks for your hard work!!", fg = red, bg = "#FEFBEA", font=("Garamond", 10))
    letter_t_label3 = tk.Label(letter_t_frame, text = "Santa has recovered fully after 3 years of ", fg = red, bg = "#FEFBEA", font=("Garamond", 10))
    letter_t_label4 = tk.Label(letter_t_frame, text = "rest, and will be forever grateful!", fg = red, bg = "#FEFBEA", font=("Garamond", 10))
    letter_t_label5 = tk.Label(letter_t_frame, text = "xoxo The North Pole, (much love from Rudolph,", fg = red, bg = "#FEFBEA", font=("Garamond", 9))
    letter_t_label6 = tk.Label(letter_t_frame, text = "Dasher, Dancer, Prancer, Comet, Vixen, Blixem,", fg = red, bg = "#FEFBEA", font=("Garamond", 9))
    letter_t_label7 = tk.Label(letter_t_frame, text = "Cupid, and Dunder)", fg = red, bg = "#FEFBEA", font=("Garamond", 9))

    #pack labels
    letter_t_label.pack()
    letter_t_label1.pack()
    letter_t_label2.pack()
    letter_t_label3.pack()
    letter_t_label4.pack()
    letter_t_label5.pack()
    letter_t_label6.pack()
    letter_t_label7.pack()

    #pack frames
    letter_h_frame.pack()
    letter_t_frame.pack()
    
#def whats next function
def whats_next():

    #call global var
    global challenges_completed

    #wipe window
    refresh()

    #determine whther player wins loses or has another round
    if reputation == 0:
        game_over()
    elif challenges_completed == 3:
        win()
    else:
        challenges_completed += 1
        challenge()

        
#define results window
def results():

    #wipe window
    refresh()

    #set window as needed
    window.title("Filling in the Spirit")
    window.configure(bg = "#FEFBEA")
    window.geometry("450x150")

    #calc result
    uv = 0
    if rd1.get()== 1:
        uv += 1
    if rd2.get() == 1:
        uv += 2
    if rd3.get() == 1:
        uv += 3
    if rd4.get() == 1:
        uv += 4
    if rd5.get() == 1:
        uv += 5
    if rd6.get() == 1:
        uv += 6
    if rd7.get() == 1:
        uv += 7
    if rd8.get() == 1:
        uv += 8
    if rd9.get() == 1:
        uv += 9

    #tv represents the difference in user value of the reindeer and the real value
    tv = uv-rv

    #global whats needed
    global ch_result
    global reputation

    #determine message
    if tv == 0:
        ch_result = "win"
    elif (tv <= 2) and (tv >= -2):
        ch_result = "awin"
    else:
        ch_result = "lose"
        reputation -= 50

    #message header
    re_header_frame = tk.Frame(window, bg = "#FEFBEA")
    re_header_label = tk.Label(re_header_frame, text="Christmas Morning Update!", fg = red, bg = "#FEFBEA", font=("Garamond", 16))
    re_header_label.pack()

    #conditinal messages
    if ch_result == "win":
        re_info_frame = tk.Frame(window, bg = "#FEFBEA")
        re_info_label = tk.Label(re_info_frame, text="Yay!! all went smoothly!", fg = red, bg = "#FEFBEA", font=("Garamond", 13))
        re_info_label.pack()
    elif ch_result == "awin":
        re_info_frame = tk.Frame(window, bg = "#FEFBEA")
        re_info_label = tk.Label(re_info_frame, text="You faced a few challenges,", fg = red, bg = "#FEFBEA", font=("Garamond", 13))
        re_info1_label = tk.Label(re_info_frame, text="but no real harm done!", fg = red, bg = "#FEFBEA", font=("Garamond", 13))
        re_info_label.pack()
        re_info1_label.pack()
    elif ch_result == "lose":
        re_info_frame = tk.Frame(window, bg = "#FEFBEA")
        re_info_label = tk.Label(re_info_frame, text="My, that was a disaster", fg = red, bg = "#FEFBEA", font=("Garamond", 13))
        re_info_label.pack()
        
    #make + pack button
    re_cont_button = tk.Button(re_info_frame, text = "CONTINUE", command = whats_next)
    re_cont_button.pack()

    #pack frames
    re_header_frame.pack()
    re_info_frame.pack()

#check whether user has checked 5 reindeer or not
def check():
    #var to rep # of reindeer
    y = 0
    if rd1.get() == 1:
        y +=1
    if rd2.get() == 1:
        y +=1
    if rd3.get() == 1:
        y +=1
    if rd4.get() == 1:
        y +=1
    if rd5.get() == 1:
        y +=1
    if rd6.get() == 1:
        y +=1
    if rd7.get() == 1:
        y +=1
    if rd8.get() == 1:
        y +=1
    if rd9.get() == 1:
        y +=1

    #if condition not met
    if y != 5:
        #redo challenge
        challenge()
        mb.showinfo("alert!","You can MUST choose exactly 5 reindeer.")
    else:
        #move one
        results()
    
#define challenge function
def challenge():

    #set window
    window.title("Filling in the Spirit")
    window.configure(bg = "#1E792C")
    window.geometry("900x375")

    #global need
    global rv
    
    #reset real value
    rv = 0
    
    #make header
    ch_header_frame = tk.Frame(window)
    ch_header_frame.grid(row=0, column=0, padx=9, pady=9)
    chheader = "CHALLENGE", challenges_completed
    ch_header_label = tk.Label(ch_header_frame, text=chheader, fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 30))
    ch_header_label.pack()
    
    #make repuation label
    rep_frame = tk.Frame(window)
    rep_frame.grid(row=0, column=1, padx=9, pady=9)
    replabel = "REPUTATION:", reputation
    rep_label = tk.Label(rep_frame, text = replabel, fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 20))
    rep_label.pack()
    
    #make challenge frame
    ch_info_frame = tk.Frame(window, bg = "#1E792C")
    ch_info_frame.grid(row=1, column=0, padx=9, pady=9)   

    #choose situation
    if challenges_completed == 1:

        #set rv
        rv = 30
        
        #make situation label
        in1lan = ("As","Christmas","approaches,","get","ready","to","be","busy", name,'!')

        ch_info1_label = tk.Label(ch_info_frame, text = in1lan, fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))
        ch_info2_label = tk.Label(ch_info_frame, text = "The time has arrived for us to complete our job, ", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))
        ch_info3_label = tk.Label(ch_info_frame, text = "and spread the magic of Christmas. Except this ", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))
        ch_info4_label = tk.Label(ch_info_frame, text = "year, we're facing some trouble. Approximately 20", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))
        ch_info5_label = tk.Label(ch_info_frame, text = "miles away from the North Pole is Pengui, a local ", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))
        ch_info6_label = tk.Label(ch_info_frame, text = "resident. Pengui went on fishing trip, and has gotten ", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))
        ch_info7_label = tk.Label(ch_info_frame, text = "himself stuck underwater. It's our mission to save him!!. ", fg = "#FFFFFF", bg = "#1E792C", \
                                  font=("Garamond", 13))
        ch_info8_label = tk.Label(ch_info_frame, text = "We wont have time to return back before going off to ", fg = "#FFFFFF", bg = "#1E792C", \
                                  font=("Garamond", 13))
        ch_info9_label = tk.Label(ch_info_frame, text = "deliver presents, so be sure to choose the best crew for", fg = "#FFFFFF", bg = "#1E792C",
                                  font=("Garamond", 13))
        ch_info10_label = tk.Label(ch_info_frame, text = "the situation!!", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))

        #pack labels
        ch_info1_label.pack()
        ch_info2_label.pack()
        ch_info3_label.pack()
        ch_info4_label.pack()
        ch_info5_label.pack()
        ch_info6_label.pack()
        ch_info7_label.pack()
        ch_info8_label.pack()
        ch_info9_label.pack()
        ch_info10_label.pack()

    elif challenges_completed == 2:

        #set rv
        rv = 21
    
        #make situation label
        in1lan = "It's","almost","Christmas", name,"!","The","time","has","come","to","do"
        ch_info1_label = tk.Label(ch_info_frame, text = in1lan, fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))
        ch_info2_label = tk.Label(ch_info_frame, text = "our long awaited job, spreading the magic of ", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))
        ch_info3_label = tk.Label(ch_info_frame, text = "Christmas. We're running low on magic this year,", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))
        ch_info4_label = tk.Label(ch_info_frame, text = "as our elves have gotten exhausted and are unable", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))
        ch_info5_label = tk.Label(ch_info_frame, text = "to make all the needed presents. Therefore, we'll  ", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))
        ch_info6_label = tk.Label(ch_info_frame, text = "need to stop at Toys R' Us, to pick up some last ", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))
        ch_info7_label = tk.Label(ch_info_frame, text = "minute presents (and wrap them!!)!", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))

        #pack labels
        ch_info1_label.pack()
        ch_info2_label.pack()
        ch_info3_label.pack()
        ch_info4_label.pack()
        ch_info5_label.pack()
        ch_info6_label.pack()
        ch_info7_label.pack()

    elif challenges_completed == 3:

        #set rv
        rv = 29
        
        #make situation label
        in1lan = "Happy","Chirstmas","Eve", name,"!","The","time","has","come","to","deliver"
        ch_info1_label = tk.Label(ch_info_frame, text = in1lan, fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))
        ch_info2_label = tk.Label(ch_info_frame, text = "presents to the boys and girls of the world, and", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))
        ch_info3_label = tk.Label(ch_info_frame, text = "make this Christmas once again merry. However this", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))
        ch_info4_label = tk.Label(ch_info_frame, text = "year, a large blizzard has came upon the North Pole.", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))
        ch_info5_label = tk.Label(ch_info_frame, text = "Our sleigh runs on magic, so theres no engine to", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))
        ch_info6_label = tk.Label(ch_info_frame, text = "worry about! What's worrysome, is the fact that our ", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))
        ch_info7_label = tk.Label(ch_info_frame, text = "sleigh has been snowed in. The snow has fallen faster", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))
        ch_info8_label = tk.Label(ch_info_frame, text = "than we've been able to clean it! Even when we get it", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))
        ch_info9_label = tk.Label(ch_info_frame, text = "up and running, there are fears that the sleigh may once", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))
        ch_info10_label = tk.Label(ch_info_frame, text = "again get snowed on when delivering presents, causing ", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))
        ch_info11_label = tk.Label(ch_info_frame, text = "much delays and unhappiness :(", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 13))

        #pack labels
        ch_info1_label.pack()
        ch_info2_label.pack()
        ch_info3_label.pack()
        ch_info4_label.pack()
        ch_info5_label.pack()
        ch_info6_label.pack()
        ch_info7_label.pack()
        ch_info8_label.pack()
        ch_info9_label.pack()
        ch_info10_label.pack()
        ch_info11_label.pack()
            
    #make choice frame
    ch_choose_frame = tk.Frame(window)
    ch_choose_frame.grid(row=1, column=1, padx=9, pady=9)
    ch_cheader_label = tk.Label(ch_choose_frame, text = "Choose Reindeer", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 16))
    ch_cheader_label.pack()

    #make checkbuttons global
    global rd1
    global rd2
    global rd3
    global rd4
    global rd5
    global rd6
    global rd7
    global rd8
    global rd9
    
    #create intvar
    rd1 = tk.IntVar()
    rd2 = tk.IntVar()
    rd3 = tk.IntVar()
    rd4 = tk.IntVar()
    rd5 = tk.IntVar()
    rd6 = tk.IntVar()
    rd7 = tk.IntVar()
    rd8 = tk.IntVar()
    rd9 = tk.IntVar()
    
    #set to 0
    rd1.set(0)
    rd2.set(0)
    rd3.set(0)
    rd4.set(0)
    rd5.set(0)
    rd6.set(0)
    rd7.set(0)
    rd8.set(0)
    rd9.set(0)

    #make checkbuttons
    rd_1 = tk.Checkbutton(ch_choose_frame, text='Rudolph', variable=rd1, command = about_rudolph)
    rd_2 = tk.Checkbutton(ch_choose_frame, text='Dancer', variable=rd2, command = about_dancer)
    rd_3 = tk.Checkbutton(ch_choose_frame, text='Dasher', variable=rd3, command = about_dasher)
    rd_4 = tk.Checkbutton(ch_choose_frame, text='Prancer', variable=rd4, command = about_prancer)
    rd_5 = tk.Checkbutton(ch_choose_frame, text='Comet', variable=rd5, command = about_comet)
    rd_6= tk.Checkbutton(ch_choose_frame, text='Vixen', variable=rd6, command = about_vixen)
    rd_7 = tk.Checkbutton(ch_choose_frame, text='Blixem', variable=rd7, command = about_blixem)
    rd_8 = tk.Checkbutton(ch_choose_frame, text='Cupid', variable=rd8, command = about_cupid)
    rd_9 = tk.Checkbutton(ch_choose_frame, text='Dunder', variable=rd9, command = about_dunder)

    #pack buttons
    rd_1.pack()
    rd_2.pack()
    rd_3.pack()
    rd_4.pack()
    rd_5.pack()
    rd_6.pack()
    rd_7.pack()
    rd_8.pack()
    rd_9.pack()

    #button
    ch_choose_button = tk.Button(ch_choose_frame, text = "CONTINUE", command = check)
    ch_choose_button.pack()        

#define break before challenge
def break1():

    #wipe
    refresh()

    #global needed
    global challenges_completed
    challenges_completed += 1
    challenge()

#define step 3 function
def step3():

    #gloabl needed
    global name

    #use var to use entry
    name = user_name.get()
    
    #reset window
    refresh()
    window.title("Filling in the Spirit")
    window.configure(bg = "#C30F16")
    window.geometry("1090x275")

    #make header
    rdheader_frame = tk.Frame(window)
    rdheader_frame.grid(row=0, column=0, padx=9, pady=9)
    rdheader_label = tk.Label(rdheader_frame, text="GET TO KNOW YOUR REINDEER!!", fg = "#FFFFFF", bg = "#C30F16", font=("Garamond", 30))
    rdheader_label.pack(side = "left")

    #intro
    rdintro_frame = tk.Frame(window, bg = "#C30F16")
    rdintro_frame.grid(row=2, column=0, padx=9, pady=9)
    rdin1n =  "Hi", name, ".","Your","job","as","Santa\'s","replacement","will","require","you","to","choose","the","best","group","of","reindeer","to","fly","\
on","Christmas","Eve.",
    rdintro_label1 = tk.Label(rdintro_frame, text = rdin1n, fg = "#FFFFFF", bg = "#C30F16", font=("Garamond", 13))
    rdintro_label3 = tk.Label(rdintro_frame, text='The day before Christmas is always unpredictable, and we need the best crew to face it. Each reindeer has their own', fg = "#FFFFFF", bg = "#C30F16", font=("Garamond", 13))
    rdintro_label5 = tk.Label(rdintro_frame, text='set of strengths and weaknesses, so we\'d like you to get to know them! (Press on each button to learn more!)', fg = "#FFFFFF", bg = "#C30F16", font=("Garamond", 13))
    rdintro_label1.pack()
    rdintro_label3.pack()
    rdintro_label5.pack()

    #reindeer info
    rdinfo_frame = tk.Frame(window)
    rdinfo_frame.grid(row=3, column=0, padx=9, pady=9)

    r1 = tk.Button(rdinfo_frame, text="RUDOLPH", command=about_rudolph)
    r2 = tk.Button(rdinfo_frame, text="PRANCER", command=about_prancer)
    r3 = tk.Button(rdinfo_frame, text="DASHER", command=about_dasher)
    r4 = tk.Button(rdinfo_frame, text="DANCER", command=about_dancer)
    r5 = tk.Button(rdinfo_frame, text="COMET", command=about_comet)
    r6 = tk.Button(rdinfo_frame, text="VIXEN", command=about_vixen)
    r7 = tk.Button(rdinfo_frame, text="BLIXEM", command=about_blixem)
    r8 = tk.Button(rdinfo_frame, text="CUPID", command=about_cupid)
    r9 = tk.Button(rdinfo_frame, text="DUNDER", command=about_dunder)

    #pack buttons
    r1.pack(side = "left")
    r2.pack(side = "left")
    r3.pack(side = "left")
    r4.pack(side = "left")
    r5.pack(side = "left")
    r6.pack(side = "left")
    r7.pack(side = "left")
    r8.pack(side = "left")
    r9.pack(side = "left")

    #continue button
    rdbutton_frame=tk.Frame(window)
    rdbutton_frame.grid(row=4, column=0, padx=9, pady=9)
    continue3_button = tk.Button(rdbutton_frame, text="CONTINUE", command=break1)
    continue3_button.pack()


#define step2 function
def step2():
    
    #make enter name window
    entername_window = tk.Toplevel()
    entername_window.title("ENTER NAME")
    entername_window.geometry("300x100")
    entername_window.configure(bg = "#1E792C")

    #make header frame
    en_title_frame = tk.Frame(entername_window)
    en_title_label = tk.Label(en_title_frame, text="ENTER YOUR NAME", fg = "#FFFFFF", bg = "#1E792C", font=("Garamond", 18))
    en_title_label.pack()

    #make entry widget frame
    en_enter_frame = tk.Frame(entername_window, bg = "#1E792C")
    global user_name
    user_name = tk.Entry(en_enter_frame, width = 20)
    user_name.pack()

    #make button frame
    en_cont_frame = tk.Frame(entername_window, relief='raised', borderwidth=1)
    continue2_button = tk.Button(en_cont_frame, text="CONTINUE", command=step3)
    continue2_button.pack()                                             

    #pack step2 frames
    en_title_frame.pack()
    en_enter_frame.pack()
    en_cont_frame.pack()
    
    #mainloop
    tk.mainloop()

#define first function (for 1st window) 
def main():
    
    #define root window
    global window
    window = tk.Tk()
    window.title("Filling in the Spirit")
    window.geometry("550x320")
    window.configure(bg = "#C30F16")
            
    #make title frame 
    title_frame = tk.Frame(window)
    title_frame.grid(row=0, column=0, padx=9, pady=9)
    title_label = tk.Label(title_frame, text="FILLING IN THE SPIRIT",fg = "#FFFFFF", bg = "#C30F16", font=("Garamond", 30))
    title_label.pack(side = "left")

    #make intro frame 
    intro_frame = tk.Frame(window, bg = "#C30F16")
    intro_frame.grid(row=1, column=0, padx=9, pady=9)
    intro_label = tk.Label(intro_frame, text="Hello and Welcome! Our dear Santa Claus has fallen ill", fg = "#FFFFFF", bg = "#C30F16", font=("Garamond",13))
    intro_label2 = tk.Label(intro_frame, text="and is sadly unable to perform his duties this Christmas.", fg = "#FFFFFF", bg = "#C30F16", font=("Garamond",13))
    intro_label3 = tk.Label(intro_frame, text="YOU have been given the great honor of fulfilling his duties", fg = "#FFFFFF", bg = "#C30F16", font=("Garamond",13))
    intro_label4 = tk.Label(intro_frame, text="as his temporary replacement. Santa prides himself on his", fg = "#FFFFFF", bg = "#C30F16", font=("Garamond",13))
    intro_label5 = tk.Label(intro_frame, text="world-class reputation, so keep in mind, if you ruin it,", fg = "#FFFFFF", bg = "#C30F16", font=("Garamond",13))
    intro_label6 = tk.Label(intro_frame, text="he'll give you the boot!", fg = "#FFFFFF", bg = "#C30F16", font=("Garamond",13))
    intro_label7 = tk.Label(intro_frame, text = "Santa's reputation is currently at: 100", fg = "#FFFFFF", bg = "#C30F16", font=("Garamond",13))

    #pack labels
    intro_label.pack()
    intro_label2.pack()
    intro_label3.pack()
    intro_label4.pack()
    intro_label5.pack()
    intro_label6.pack()
    intro_label7.pack()

    #make buttons
    userAgreement_frame = tk.Frame(window, relief='raised', borderwidth=1)
    userAgreement_frame.grid(row=4, column=0, padx=9, pady=9)
    userAgreement_button = tk.Button(userAgreement_frame, text="START", command=step2)
    userAgreement_quit_button = tk.Button(userAgreement_frame, text="QUIT", command = window.destroy)
    userAgreement_button.pack(side = "left")
    userAgreement_quit_button.pack(side = "left")

    #mainloop
    tk.mainloop()

#call main function
main()
