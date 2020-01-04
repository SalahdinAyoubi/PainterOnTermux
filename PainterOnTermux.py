import  os , time , sys



D_prog="""
{}                         ''~``
                        ( o o )
{}+------------------{}.oooO{}--{}(_){}--{}Oooo{}.--------------------+
{}             _____      _       _            
            |  __ \    (_)     | |           
            | |__) |_ _ _ _ __ | |_ ___ _ __ 
            |  ___/ _` | | '_ \| __/ _ \ '__|
{}  __^__ {}    | |  | (_| | | | | | ||  __/ |       {} __^__{}
 ( ___ ){}    |_|   \__,_|_|_| |_|\__\___|_|   {}    ( ___ )
  | / | {}          Painter on Termux   {}            | / |
  | / |  {}           Version 0.001    {}             | / |
  | / |                                           | / |
  |___|             .oooO                         |___|
 (_____)             (   )   Oooo.               (_____) 
{}+---------------------{}\ ({}----{}(   ){}----------------------+
 {}[Creat by:Python Dz] {} \_)    ) /  
                             (_/   
"""
# Colors
g ='\033[92m'
r ='\033[91m'
b ='\033[94m'
y ='\033[93m'
w = '\033[0m'
m = '\033[95m'
bl  = '\033[96m'

me = D_prog.format(y, r, y, r, y, r, y, r, g, y, g, y, w, g, w, bl, w, b, w, r, w, r, w, r, y, w)


###########################
# Path and write command
path ="/data/data/com.termux/files/usr/etc/"
bash ="""
clear
#cmatrix -s
figlet -f big Name #| lolcat -s
PS1='\=$> '"""

# function About
def about():
	os.system("clear")
	print(me)
	abou = bl+"   Creat by :  Python Dz  \n   Github   :  SalahdinAyoubi \n   Facebook :  sami.rabih.925\n   update   :  05-01-2020\n   Version  :  V 0.001\n\n"
	
	for i in abou:
	    time.sleep(0.1)
	    sys.stdout.write(i)
	    sys.stdout.flush()
	time.sleep(2.5)
	print(w)
	os.system("clear")	

#  function choice 
def choice():
	ch="""{}
  01{}  - Creat your Name on termux
  {}02 {} - change your Name on termux
  {}03{}  - About 
  {}04{}  - Exit
"""
	print(ch.format(y, g, y, g, y, g, y, g))
	choice = input("  - Enter your choice : "+w)
	if choice == "1" or choice == "01":
		creat_name()
	elif choice == "2" or choice == "02":
		print(y+" - Sorry, this option is not available"+w)
		time.sleep(2.5) 	    
	elif  choice == "3" or choice == "03":
		about()
	elif choice == "4" or choice == "04":
		os.system("clear")
		print(me)
		print("\n"*3)
		print(g+"                Good bey   ^__^  "+w)
		print("\n"*2)
		exit()
		
	else:
		print(r+" !!  Plz Enter choice number !! "+w)
		time.sleep(2)

		

# function Creat Name 	
def creat_name():
	os.system("clear")
	print(me)	
	
	nam = input(" - Enter your Name : ")
	name = input(" - Confirm your Name : ")
	if nam == name:
		key = bash.replace("Name" ,  name)		
		print(y+"\n......    Loading ....…... "+w)
		os.system("pkg install figlet")
		os.system("clear")
		print(me)
		print(g+" - [√] Save Name Successfully!"+w)
		
		cm = input(" - Are you add cmatrix [y/n] ? : ")
		if cm == "Y" or cm == "y":
			os.system("clear")
			print(me)
			print(y+"....   Loading  ............ "+w)
			os.system("pkg install cmatrix")
			key = key.replace("#cmatrix -s" ,"cmatrix -s")
			os.system("clear")
			print(me)
			print(g+" - [√] Add Cmatrix Successfully! "+w)
			print("\n\n")
			
	
	
			
		lol = input(" -  Are you Add Colors  [n\y] : ")
		if lol =="Y"  or lol == "y":
			os.system("clear")
			print(me)
			print(y+"..........  Loading  ............... "+w)
			time.sleep(0.5)
			os.system("pkg install ruby")
			os.system("gem install lolcat")
			key = key.replace("#| lolcat -s" ,"| lolcat -s")
			os.system("clear")
			print(me)
			print(g+" [√] Add Cloros Successfully!\n"+w)
			
	elif nam != name:
		print(r+" -!!  The name does not match"+w)
		time.sleep(2.5)
		creat_name()
		
	else:
		pass
	
	
			
	f = open(path+"bash.bashrc" , "w")
	f.write(key)
	f.close()
	print(g+" [√] The operation ended successfully\n ")
	print(" [√]  Open a new session to see this"+w)
	time.sleep(10)
    
	
		
		
			
	       

 


while True:
	print(me)
	choice()
	os.system("clear") 
