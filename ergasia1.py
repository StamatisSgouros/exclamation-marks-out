print "Dwse mia protasi"
text=raw_input()
mhkos=len(text)
i=mhkos
flag=1
mhkos2=mhkos

while (i>0) and (flag==1):
	i=i-1
	if text[i]!=("!"):
		mhkos2=i
		flag=0
mhkos2=mhkos2+1	
newtext=text.replace("!","") 
diafora=len(text)-mhkos2
newtext=newtext + diafora*"!"
print newtext
	 
