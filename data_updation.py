import scrapingfile
from scrapingfile import get_val 
data=get_val

import openpyxl
#data=[[["Andhra Pradesh", "Anantapur"],"MURDER"],[["Andhra Pradesh","Guntur"],"MISSING"]]
dataset=openpyxl.load_workbook('Base Dataset.xlsx')
sheet=dataset.active
cell=""

def sheetsval(element):

	for row in range(1, sheet.max_row + 1):
        #print(row)
		for column in "B":  # Here you can add or reduce the columns
			cell_name = "{}{}".format(column, row)
            #print(cell_name)
			#print(element[0])
			if(sheet[cell_name].value==element[0]):
				print("found")
				#return sheet[cell_name]
				print(cell_name)
				return cell_name
		#break	
'''
	MISSING-C
	FORGERY-D
	SUICIDE-E
	NON VIOLANCE-F
	HARRASMENT-G
	MURDER-H
	MURDER ATTEMPT-I
	SMUGGLING-J
'''
def update(value,cell_no):

	if value=="MISSING":
		column="C"

		#print(cell_no)
		val=column+cell_no
		update_val(val)
	elif value=="FORGERY":
		column="D"
		#print(cell_no)
		val=column+cell_no
		update_val(val)
	elif value=="SUICIDE":
		column="E"
		#print(cell_no)
		val=column+cell_no
		update_val(val)
	elif value=="NONVIOLANCE":
		column="F"
		#print(cell_no)
		val=column+cell_no
		update_val(val)
	elif value=="HARRASMENT":
		column="G"
		#print(cell_no)
		val=column+cell_no
		update_val(val)
	elif value=="MURDER":
		column="H"
		print(cell_no)

		val=column+cell_no
		update_val(val)
	elif value=="MURDER ATTEMPT":
		column="I"
		#print(cell_no)
		val=column+cell_no
		update_val(val)
	elif value=="SMUGGLING":
		column="J"
		#print(cell_no)
		val=column+cell_no
		update_val(val)
	else:
		print("Error")
	return
	
	

def update_val(val):
	cell_value=sheet[val].value
	print(val)
	print("___________________")
	print(sheet[val].value)	
	cell_value=cell_value+1
	print(cell_value)
	sheet[val]=cell_value
	print("-------------Updated------------")
#print(data)


for element,value in data:
	print("EXECUTING ______________________")
	print(element,value)
	print("EXECUTING ______________________")
	valueupper=value.upper()
	
	cellname=sheetsval(element)
	if cellname!=None:
		strv=str(cellname)
		for letter in strv:

			if letter.isdigit():
				cell+=str(letter)
		update(valueupper,cell)
	cell=""
	dataset.save('Base Dataset.xlsx')
	