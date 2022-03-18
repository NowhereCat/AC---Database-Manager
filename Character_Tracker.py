import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter import filedialog, colorchooser, ttk, messagebox

import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())
'''
testVar1 = os.getenv("hostStringEnv")
testVar2 = os.getenv("databaseStringEnv")
testVar3 = os.getenv("userStringEnv")
testVar4 = os.getenv("pswStringEnv")
testVar5 = os.getenv("tblStringEnv")
'''
root = Tk()
root.title("Character Tracker Manager")
root.resizable(False, False)

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/3 - windowHeight/2)
root.geometry("+{}+{}".format(positionRight, positionDown))
#root.geometry("650x650")
#root.eval('tk::PlaceWindow . center')

hostString = os.getenv("hostStringEnv")
databaseString = os.getenv("databaseStringEnv")
userString = os.getenv("userStringEnv")
passwordString = os.getenv("pswStringEnv")
tableString = os.getenv("tblStringEnv")

#Commands
def testConnection():
	queryFrame.grid_forget()
	insertFrame.grid_forget()
	updateFrame.grid_forget()

	try:
		connection = mysql.connector.connect(host=hostString, database=databaseString, user=userString, password=passwordString)

		if connection.is_connected():
			#Comfirm connection
			db_Info = connection.get_server_info()
			#print("Connected to MySQL Server version ", db_Info)
			cursor = connection.cursor()
			cursor.execute("select database();")
			record = cursor.fetchone()
			#print("You are connected to database: ", record)
			messageString = "Connected to MySQL Server version ", db_Info, "\nYou are connected to database: ", record
			messagebox.showinfo("Connection Result", messageString)
			'''
			#Insert
			mySql_insert_query = """INSERT INTO test (id, name)
									VALUES
									(NULL, 'Steve')"""

			cursor.execute(mySql_insert_query)
			connection.commit()
			print("\n", cursor.rowcount, "Record inserted sucessfully into test table")
			'''


	except Error as e:
		errorString = "Unable to Connect: ", e
		messagebox.showerror("Error!", errorString)
		#print("Error while connecting to MySQL", e)
	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()
			#print("MySQL connection is closed")

#testConnection()

def queryAll():
	try:
		connection = mysql.connector.connect(host=hostString, database=databaseString, user=userString, password=passwordString)
		if connection.is_connected():
			insertFrame.grid_forget()
			updateFrame.grid_forget()
			queryFrame.grid(row=1, column=0)

			
			cursor = connection.cursor()
			sql_select_Query = "SELECT * FROM " + tableString
			cursor.execute(sql_select_Query)
			queryRecords = cursor.fetchall()
			outputString = "Results:\n"
			for row in queryRecords:
				outputString += "\nID: " + str(row[0]) + "\n"
				outputString += "Name: " + str(row[1]) + "\n"
				outputString += "Current Act: " + str(row[2]) + "\n"
				outputString += "Species: " + str(row[3]) + "\n"
				outputString += "Blood Color: " + str(row[4]) + "\n"
				outputString += "Username: " + str(row[5]) + "\n"
				outputString += "Hemotyping: " + str(row[6]) + "\n"
				outputString += "Quirk Description: " + str(row[7]) + "\n"
				outputString += "Gender: " + str(row[8]) + "\n"
				outputString += "Age: " + str(row[9]) + "\n"
				outputString += "Heigth: " + str(row[10]) + "\n"
				outputString += "Sign: " + str(row[11]) + "\n"
				outputString += "Classpect: " + str(row[12]) + " of " + str(row[13]) + "\n"
				outputString += "Dreamself: " + str(row[14]) + "\n"
				outputString += "Planet: " + str(row[15]) + "\n"
				outputString += "Consort: " + str(row[16]) + "\n"
				outputString += "Denizen: " + str(row[17]) + "\n"
				outputString += "Strifedeck: " + str(row[18]) + "\n"
				outputString += "Sylladex Modi: " + str(row[19]) + "\n"
				outputString += "Guardian: " + str(row[20]) + "\n"
				outputString += "Title Color: " + str(row[21]) + "\n"
				outputString += "Image URL: " + str(row[22]) + "\n"
				outputString += "Notes: " + str(row[23]) + "\n"
				outputString += "------------------------------- \n"

		#queryTextBox['text'] = (outputString)
		queryTextBox.delete('1.0', END)
		queryTextBox.insert(END, outputString)
	except Error as e:
		errorString = "Unable to Connect: ", e
		messagebox.showerror("Error!", errorString)
	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()

def insertScreen():
	insertFrame.grid(row=1, column=0)
	queryFrame.grid_forget()
	updateFrame.grid_forget()

def updateScreen():
	updateFrame.grid(row=1, column=0)
	queryFrame.grid_forget()
	insertFrame.grid_forget()

def loadQuery(uid):
	try:
		connection = mysql.connector.connect(host=hostString, database=databaseString, user=userString, password=passwordString)
		if connection.is_connected():
			cursor = connection.cursor()
			sql_select_query = """SELECT * FROM character_table WHERE id = %s"""
			cursor.execute(sql_select_query, (uid,))
			record = cursor.fetchall()
			#messagebox.showinfo("Query Info", record)

			for row in record:
				uCharacterName_Entry.insert(0, row[1])
				uCurrentAct_Entry.insert(0, row[2])
				uSpecies_Entry.insert(0, row[3])
				uBloodColor_Entry.insert(0, row[4])
				uUserName_Entry.insert(0, row[5])
				uHemotyping_Entry.insert(0, row[6])
				uQuirkDesc_Entry.insert('1.0', row[7])
				uCharacterGender_Entry.insert(0, row[8])
				uAge_Entry.insert(0, row[9])
				uHeight_Entry.insert(0, row[10])
				uSign_Entry.insert(0, row[11])
				uClass_Entry.insert(0, row[12])
				uAspect_Entry.insert(0, row[13])

				for slot in u_Dreamself_Options:
					if row[14] == slot: u_Dreamself_Var.set(slot)
				uPlanet_Entry.insert(0, row[15])
				uConsort_Entry.insert(0, row[16])
				uDenizen_Entry.insert(0, row[17])
				uStrifedeck_Entry.insert(0, row[18])
				uSylladexModi_Entry.insert(0, row[19])
				uGuardian_Entry.insert(0, row[20])
				uTitleColor_Entry.insert(0, row[21])
				uImageURL_Entry.insert(0, row[22])
				uNotes_TextBox.insert('1.0', row[23])

	except Error as e:
		messagebox.showerror("MySQL Query Error", e)
	except ValueError as e:
		messagebox.showerror("Value Error", e)
	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()


def submitLog():
		try:
			heightFloat = float(iHeight_Entry.get())
			connection = mysql.connector.connect(host=hostString, database=databaseString, user=userString, password=passwordString)
			if connection.is_connected():
				cursor = connection.cursor()
				mySql_insert_query = """INSERT INTO character_table (id, name, currentAct, species, bloodColor, userName, hemotyping, quirkDesc, gender, age, height, sign, class, aspect, dreamself, planet, consort, denizen, strifeDeck, sylladexModi, guardian, titleColor, imagesURL, notes)
										VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
				insertRecord = (None, 
					iCharacterName_Entry.get(),
					iCurrentAct_Entry.get(),
					iSpecies_Entry.get(),
					iBloodColor_Entry.get(),
					iUserName_Entry.get(),
					iHemotyping_Entry.get(),
					iQuirkDesc_Entry.get('1.0', END),
					iCharacterGender_Entry.get(),
					iAge_Entry.get(),
					iHeight_Entry.get(),
					iSign_Entry.get(),
					iClass_Entry.get(),
					iAspect_Entry.get(),
					i_Dreamself_Var.get(),
					iPlanet_Entry.get(),
					iConsort_Entry.get(),
					iDenizen_Entry.get(),
					iStrifedeck_Entry.get(),
					iSylladexModi_Entry.get(),
					iGuardian_Entry.get(),
					iTitleColor_Entry.get(),
					iImageURL_Entry.get(),
					iNotes_TextBox.get('1.0', END))

				cursor.execute(mySql_insert_query, insertRecord)
				connection.commit()
				messagebox.showinfo("Log Inserted", insertRecord)

				iCharacterName_Entry.delete(0, END)
				iCurrentAct_Entry.delete(0, END)
				iSpecies_Entry.delete(0, END)
				iBloodColor_Entry.delete(0, END)
				iUserName_Entry.delete(0, END)
				iHemotyping_Entry.delete(0, END)
				iQuirkDesc_Entry.delete('1.0', END)
				iCharacterGender_Entry.delete(0, END)
				iAge_Entry.delete(0, END)
				iHeight_Entry.delete(0, END)
				iSign_Entry.delete(0, END)
				iClass_Entry.delete(0, END)
				iAspect_Entry.delete(0, END)
				i_Dreamself_Var.set(i_Dreamself_Options[0])
				iPlanet_Entry.delete(0, END)
				iConsort_Entry.delete(0, END)
				iDenizen_Entry.delete(0, END)
				iStrifedeck_Entry.delete(0, END)
				iSylladexModi_Entry.delete(0, END)
				iGuardian_Entry.delete(0, END)
				iTitleColor_Entry.delete(0, END)
				iImageURL_Entry.delete(0, END)
				iNotes_TextBox.delete('1.0', END)
		except Error as e:
			errorString = "Unable to Connect: ", e
			messagebox.showerror("Error!", errorString)
		except ValueError as e:
			messagebox.showerror("Value Error", e)
		finally:
			if connection.is_connected():
				cursor.close()
				connection.close()

def updateQuery():
	try:
		updateID = int(uID_Entry.get())
		heightFloat = float(uHeight_Entry.get())

		connection = mysql.connector.connect(host=hostString, database=databaseString, user=userString, password=passwordString)
		cursor = connection.cursor()

		sql_update_query = """UPDATE character_table SET name = %s, currentAct = %s, species = %s, bloodColor = %s, userName = %s, hemotyping = %s, quirkDesc = %s, gender = %s, age = %s, height = %s, 
							sign = %s, class = %s, aspect = %s, dreamself = %s, planet = %s, consort = %s, denizen = %s, strifeDeck = %s, sylladexModi = %s, guardian = %s, titleColor = %s, 
							imagesURL = %s, notes = %s WHERE id = %s"""

		updateInput = (iCharacterName_Entry.get(),
					iCurrentAct_Entry.get(),
					iSpecies_Entry.get(),
					iBloodColor_Entry.get(),
					iUserName_Entry.get(),
					iHemotyping_Entry.get(),
					iQuirkDesc_Entry.get('1.0', END),
					iCharacterGender_Entry.get(),
					iAge_Entry.get(),
					iHeight_Entry.get(),
					iSign_Entry.get(),
					iClass_Entry.get(),
					iAspect_Entry.get(),
					i_Dreamself_Var.get(),
					iPlanet_Entry.get(),
					iConsort_Entry.get(),
					iDenizen_Entry.get(),
					iStrifedeck_Entry.get(),
					iSylladexModi_Entry.get(),
					iGuardian_Entry.get(),
					iTitleColor_Entry.get(),
					iImageURL_Entry.get(),
					iNotes_TextBox.get('1.0', END),
					updateID)

		cursor.execute(sql_update_query, updateInput)
		connection.commit()

		messagebox.showinfo("Update Executed", "Info updated")

	except Error as e:
		messagebox.showerror("MySQL Error", e)
	except ValueError as e:
		messagebox.showerror("Value Error", e)
	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()


'''
try:
	connection = mysql.connector.connect(host='localhost', database='stock', user='root', password='Orion2014!')

	if connection.is_connected():
		#Comfirm connection
		db_Info = connection.get_server_info()
		print("Connected to MySQL Server version ", db_Info)
		cursor = connection.cursor()
		cursor.execute("select database();")
		record = cursor.fetchone()
		print("You are connected to database: ", record)
'''
'''
		#Insert
		mySql_insert_query = """INSERT INTO test (id, name)
								VALUES
								(NULL, 'Steve')"""

		cursor.execute(mySql_insert_query)
		connection.commit()
		print("\n", cursor.rowcount, "Record inserted sucessfully into test table")
'''
'''
		#Query
		sql_select_Query = "SELECT * FROM test"
		cursor.execute(sql_select_Query)
		queryRecords = cursor.fetchall()
		print("\nRecords")
		for row in queryRecords:
			print("ID: ", row[0])
			print("Name: ", row[1], "\n")

except Error as e:
	print("Error while connecting to MySQL", e)
finally:
	if connection.is_connected():
		cursor.close()
		connection.close()
		print("MySQL connection is closed")
'''

#Buttons GUI
buttonsFrame = LabelFrame(root, padx=10, pady=10)
buttonsFrame.grid(row=0, column=0)

tcButton = Button(buttonsFrame, text="Test Connection", command=testConnection) #Query Search
tcButton.grid(row=0, column=0, padx=5, pady=5)

qButton = Button(buttonsFrame, text="Show all logs", command=queryAll) #Query Search
qButton.grid(row=0, column=1, padx=5, pady=5)

ilButton = Button(buttonsFrame, text="Insert", command=insertScreen) #Insert Log
ilButton.grid(row=0, column=2, padx=5, pady=5)

tcButton = Button(buttonsFrame, text="Update", command=updateScreen) #Update logs
tcButton.grid(row=0, column=3, padx=5, pady=5)
#------------------------------------------------------

#Query GUI
queryFrame = LabelFrame(root, padx=10, pady=10)
#queryFrame.grid(row=1, column=0)

Label(queryFrame, text="Query Results: ", font=15).pack()

queryTextBox = Text(queryFrame, height = 25, width = 40)

scroll_bar = Scrollbar(queryFrame, orient=VERTICAL, command=queryTextBox.yview)
queryTextBox['yscroll'] = scroll_bar.set
scroll_bar.pack(side=RIGHT, fill=Y)

queryTextBox.pack(side=LEFT)
#------------------------------------------------------

#Insert GUI
insertFrame = LabelFrame(root, padx=10, pady=10)

iTitle_Label = Label(insertFrame, text="Insert Log", font=15)
iTitle_Label.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

iCharacterName_Label = Label(insertFrame, text="Name: ")
iCharacterName_Label.grid(row=1, column=0, sticky='w')
iCharacterName_Entry = Entry(insertFrame, textvariable="Joiboy Nassus", width=20)
iCharacterName_Entry.grid(row=1, column=1, sticky='w')

iCurrentAct_Label = Label(insertFrame, text="Current Act: ")
iCurrentAct_Label.grid(row=2, column=0, sticky='w')
iCurrentAct_Entry = Entry(insertFrame, textvariable="Act 2", width=20)
iCurrentAct_Entry.grid(row=2, column=1, sticky='w')

iSpecies_Label = Label(insertFrame, text="Species: ")
iSpecies_Label.grid(row=3, column=0, sticky='w')
iSpecies_Entry = Entry(insertFrame, textvariable="Troll", width=20)
iSpecies_Entry.grid(row=3, column=1, sticky='w')

iBloodColor_Label = Label(insertFrame, text="Blood Color: ")
iBloodColor_Label.grid(row=4, column=0, sticky='w')
iBloodColor_Entry = Entry(insertFrame, width=20)
iBloodColor_Entry.grid(row=4, column=1, sticky='w')

iUserName_Label = Label(insertFrame, text="Username: ")
iUserName_Label.grid(row=1, column=3, sticky='w')
iUserName_Entry = Entry(insertFrame, textvariable="aquaticDreamer", width=20)
iUserName_Entry.grid(row=1, column=4, sticky='w')

iHemotyping_Label = Label(insertFrame, text="Hemotyping: ")
iHemotyping_Label.grid(row=2, column=3, sticky='w')
iHemotyping_Entry = Entry(insertFrame, textvariable="#6a006a", width=20)
iHemotyping_Entry.grid(row=2, column=4, sticky='w')


iQuirkDesc_Label = Label(insertFrame, text="Quirk Description: ")
iQuirkDesc_Label.grid(row=3, column=3, sticky='w')
iQuirkDesc_Frame = LabelFrame(insertFrame)
iQuirkDesc_Frame.grid(row=3, column=4, sticky='w')
iQuirkDesc_Entry = Text(iQuirkDesc_Frame, height=5, width=50)
qcScroll = Scrollbar(iQuirkDesc_Frame, orient=VERTICAL, command=iQuirkDesc_Entry.yview)
iQuirkDesc_Entry['yscroll'] = qcScroll.set
qcScroll.pack(side=RIGHT, fill=Y)
iQuirkDesc_Entry.pack(side=LEFT)

iCharacterGender_Label = Label(insertFrame, text="Gender: ")
iCharacterGender_Label.grid(row=4, column=3, sticky='w')
iCharacterGender_Entry = Entry(insertFrame, textvariable="Male", width=20)
iCharacterGender_Entry.grid(row=4, column=4, sticky='w')

ttk.Separator(insertFrame, orient=VERTICAL).grid(row=1, column=2, rowspan=13, padx=10, sticky='ns')

iAge_Label = Label(insertFrame, text="Age: ")
iAge_Label.grid(row=5, column=0, sticky='w')
iAge_Entry = Entry(insertFrame, textvariable="6 Sweeps", width=20)
iAge_Entry.grid(row=5, column=1, sticky='w')

iHeight_Label = Label(insertFrame, text="Height (Meters): ")
iHeight_Label.grid(row=6, column=0, sticky='w')
iHeight_Entry = Entry(insertFrame, textvariable=1.65, width=10)
iHeight_Entry.grid(row=6, column=1, sticky='w')

iSign_Label = Label(insertFrame, text="Sign: ")
iSign_Label.grid(row=7, column=0, sticky='w')
iSign_Entry = Entry(insertFrame, textvariable="Aquapio", width=20)
iSign_Entry.grid(row=7, column=1, sticky='w')

iClass_Label = Label(insertFrame, text="Class: ")
iClass_Label.grid(row=8, column=0, sticky='w')
iClass_Entry = Entry(insertFrame, width=20)
iClass_Entry.grid(row=8, column=1, sticky='w')

iAspect_Label = Label(insertFrame, text="Aspect: ")
iAspect_Label.grid(row=9, column=0, sticky='w')
iAspect_Entry = Entry(insertFrame, width=20)
iAspect_Entry.grid(row=9, column=1, sticky='w')

iDreamself_Label = Label(insertFrame, text="Dreamself")
iDreamself_Label.grid(row=5, column=3, sticky='w')
i_Dreamself_Options =[
	"Unknown",
	"Prospit",
	"Derse",
	"Prospit (Dual)",
	"Derse (Dual)"
]
i_Dreamself_Var = StringVar()
i_Dreamself_Var.set(i_Dreamself_Options[0])
iDreamself_Dropbox = ttk.OptionMenu(insertFrame, i_Dreamself_Var, *i_Dreamself_Options)
iDreamself_Dropbox.grid(row=5, column=4, sticky='w')

iPlanet_Label = Label(insertFrame, text="Planet: ")
iPlanet_Label.grid(row=6, column=3, sticky='w')
iPlanet_Entry = Entry(insertFrame, width=40)
iPlanet_Entry.grid(row=6, column=4, sticky='w')

iConsort_Label = Label(insertFrame, text="Consort: ")
iConsort_Label.grid(row=7, column=3, sticky='w')
iConsort_Entry = Entry(insertFrame, width=20)
iConsort_Entry.grid(row=7, column=4, sticky='w')

iDenizen_Label = Label(insertFrame, text="Denizen: ")
iDenizen_Label.grid(row=8, column=3, sticky='w')
iDenizen_Entry = Entry(insertFrame, width=20)
iDenizen_Entry.grid(row=8, column=4, sticky='w')

iStrifedeck_Label = Label(insertFrame, text="Strifedeck: ")
iStrifedeck_Label.grid(row=10, column=0, sticky='w')
iStrifedeck_Entry = Entry(insertFrame, width=20)
iStrifedeck_Entry.grid(row=10, column=1, sticky='w')

iSylladexModi_Label = Label(insertFrame, text="Sylladex Modi: ")
iSylladexModi_Label.grid(row=11, column=0, sticky='w')
iSylladexModi_Entry = Entry(insertFrame, width=20)
iSylladexModi_Entry.grid(row=11, column=1, sticky='w')

iGuardian_Label = Label(insertFrame, text="Guardian: ")
iGuardian_Label.grid(row=12, column=0, sticky='w')
iGuardian_Entry = Entry(insertFrame, width=20)
iGuardian_Entry.grid(row=12, column=1, sticky='w')

iTitleColor_Label = Label(insertFrame, text="Title Color: ")
iTitleColor_Label.grid(row=13, column=0, sticky='w')
iTitleColor_Entry = Entry(insertFrame, width=20)
iTitleColor_Entry.grid(row=13, column=1, sticky='w')

iImagesURL_Label = Label(insertFrame, text="Image URL: ")
iImagesURL_Label.grid(row=14, column=0, sticky='w')
iImageURL_Entry = Entry(insertFrame, width=20)
iImageURL_Entry.grid(row=14, column=1, sticky='w')

iNotes_Label = Label(insertFrame, text="Notes: ")
iNotes_Label.grid(row=9, column=3, sticky='w')
iNotes_Frame = LabelFrame(insertFrame)
iNotes_Frame.grid(row=9, column=4, sticky='w')
iNotes_TextBox = Text(iNotes_Frame, height=5, width=50)
notesScroll = Scrollbar(iNotes_Frame, orient=VERTICAL, command=iNotes_TextBox.yview)
iNotes_TextBox['yscroll'] = notesScroll.set
notesScroll.pack(side=RIGHT, fill=Y)
iNotes_TextBox.pack(side=LEFT)

iSubmit_Button = Button(insertFrame, text="Submit", command=submitLog)
iSubmit_Button.grid(row=14, column=0, columnspan=5)
#------------------------------------------------------

#Update GUI
updateFrame = LabelFrame(root, padx=10, pady=10)

uTitle_Label = Label(updateFrame, text="Update Log", font=15)
uTitle_Label.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

uID_Frame = LabelFrame(updateFrame)
uID_Frame.grid(row=1, column=0, columnspan=2, sticky='w')
uID_Label = Label(uID_Frame, text="ID: ")
uID_Label.grid(row=0, column=0, sticky='w')
uID_Entry = Entry(uID_Frame, width=5)
uID_Entry.grid(row=0, column=1, sticky='w')
uID_Entry.insert(0, "1")
uID_Button = Button(uID_Frame, text="Load", command=lambda:loadQuery(uID_Entry.get()))
uID_Button.grid(row=0, column=2, sticky='w')

uCharacterName_Label = Label(updateFrame, text="Name: ")
uCharacterName_Label.grid(row=2, column=0, sticky='w')
uCharacterName_Entry = Entry(updateFrame, textvariable="Joiboy Nassus", width=20)
uCharacterName_Entry.grid(row=2, column=1, sticky='w')

uCurrentAct_Label = Label(updateFrame, text="Current Act: ")
uCurrentAct_Label.grid(row=3, column=0, sticky='w')
uCurrentAct_Entry = Entry(updateFrame, textvariable="Act 2", width=20)
uCurrentAct_Entry.grid(row=3, column=1, sticky='w')

uSpecies_Label = Label(updateFrame, text="Species: ")
uSpecies_Label.grid(row=4, column=0, sticky='w')
uSpecies_Entry = Entry(updateFrame, textvariable="Troll", width=20)
uSpecies_Entry.grid(row=4, column=1, sticky='w')

uBloodColor_Label = Label(updateFrame, text="Blood Color: ")
uBloodColor_Label.grid(row=5, column=0, sticky='w')
uBloodColor_Entry = Entry(updateFrame, width=20)
uBloodColor_Entry.grid(row=5, column=1, sticky='w')

uUserName_Label = Label(updateFrame, text="Username: ")
uUserName_Label.grid(row=2, column=3, sticky='w')
uUserName_Entry = Entry(updateFrame, textvariable="aquaticDreamer", width=20)
uUserName_Entry.grid(row=2, column=4, sticky='w')

uHemotyping_Label = Label(updateFrame, text="Hemotyping: ")
uHemotyping_Label.grid(row=3, column=3, sticky='w')
uHemotyping_Entry = Entry(updateFrame, textvariable="#6a006a", width=20)
uHemotyping_Entry.grid(row=3, column=4, sticky='w')


uQuirkDesc_Label = Label(updateFrame, text="Quirk Description: ")
uQuirkDesc_Label.grid(row=4, column=3, sticky='w')
uQuirkDesc_Frame = LabelFrame(updateFrame)
uQuirkDesc_Frame.grid(row=4, column=4, sticky='w')
uQuirkDesc_Entry = Text(uQuirkDesc_Frame, height=5, width=50)
uqcScroll = Scrollbar(uQuirkDesc_Frame, orient=VERTICAL, command=uQuirkDesc_Entry.yview)
uQuirkDesc_Entry['yscroll'] = uqcScroll.set
uqcScroll.pack(side=RIGHT, fill=Y)
uQuirkDesc_Entry.pack(side=LEFT)

uCharacterGender_Label = Label(updateFrame, text="Gender: ")
uCharacterGender_Label.grid(row=5, column=3, sticky='w')
uCharacterGender_Entry = Entry(updateFrame, textvariable="Male", width=20)
uCharacterGender_Entry.grid(row=5, column=4, sticky='w')

ttk.Separator(updateFrame, orient=VERTICAL).grid(row=2, column=2, rowspan=13, padx=10, sticky='ns')

uAge_Label = Label(updateFrame, text="Age: ")
uAge_Label.grid(row=6, column=0, sticky='w')
uAge_Entry = Entry(updateFrame, textvariable="6 Sweeps", width=20)
uAge_Entry.grid(row=6, column=1, sticky='w')

uHeight_Label = Label(updateFrame, text="Height (Meters): ")
uHeight_Label.grid(row=7, column=0, sticky='w')
uHeight_Entry = Entry(updateFrame, textvariable=1.65, width=10)
uHeight_Entry.grid(row=7, column=1, sticky='w')

uSign_Label = Label(updateFrame, text="Sign: ")
uSign_Label.grid(row=8, column=0, sticky='w')
uSign_Entry = Entry(updateFrame, textvariable="Aquapio", width=20)
uSign_Entry.grid(row=8, column=1, sticky='w')

uClass_Label = Label(updateFrame, text="Class: ")
uClass_Label.grid(row=9, column=0, sticky='w')
uClass_Entry = Entry(insertFrame, width=20)
uClass_Entry.grid(row=9, column=1, sticky='w')

uAspect_Label = Label(updateFrame, text="Aspect: ")
uAspect_Label.grid(row=10, column=0, sticky='w')
uAspect_Entry = Entry(updateFrame, width=20)
uAspect_Entry.grid(row=10, column=1, sticky='w')

uDreamself_Label = Label(updateFrame, text="Dreamself")
uDreamself_Label.grid(row=6, column=3, sticky='w')
u_Dreamself_Options =[
	"Unknown",
	"Prospit",
	"Derse",
	"Prospit (Dual)",
	"Derse (Dual)"
]
u_Dreamself_Var = StringVar()
u_Dreamself_Var.set(u_Dreamself_Options[0])
uDreamself_Dropbox = ttk.OptionMenu(updateFrame, u_Dreamself_Var, *u_Dreamself_Options)
uDreamself_Dropbox.grid(row=6, column=4, sticky='w')

uPlanet_Label = Label(updateFrame, text="Planet: ")
uPlanet_Label.grid(row=7, column=3, sticky='w')
uPlanet_Entry = Entry(updateFrame, width=40)
uPlanet_Entry.grid(row=7, column=4, sticky='w')

uConsort_Label = Label(updateFrame, text="Consort: ")
uConsort_Label.grid(row=8, column=3, sticky='w')
uConsort_Entry = Entry(updateFrame, width=20)
uConsort_Entry.grid(row=8, column=4, sticky='w')

uDenizen_Label = Label(updateFrame, text="Denizen: ")
uDenizen_Label.grid(row=9, column=3, sticky='w')
uDenizen_Entry = Entry(updateFrame, width=20)
uDenizen_Entry.grid(row=9, column=4, sticky='w')

uStrifedeck_Label = Label(updateFrame, text="Strifedeck: ")
uStrifedeck_Label.grid(row=11, column=0, sticky='w')
uStrifedeck_Entry = Entry(updateFrame, width=20)
uStrifedeck_Entry.grid(row=11, column=1, sticky='w')

uSylladexModi_Label = Label(updateFrame, text="Sylladex Modi: ")
uSylladexModi_Label.grid(row=12, column=0, sticky='w')
uSylladexModi_Entry = Entry(updateFrame, width=20)
uSylladexModi_Entry.grid(row=12, column=1, sticky='w')

uGuardian_Label = Label(updateFrame, text="Guardian: ")
uGuardian_Label.grid(row=13, column=0, sticky='w')
uGuardian_Entry = Entry(updateFrame, width=20)
uGuardian_Entry.grid(row=13, column=1, sticky='w')

uTitleColor_Label = Label(updateFrame, text="Title Color: ")
uTitleColor_Label.grid(row=14, column=0, sticky='w')
uTitleColor_Entry = Entry(updateFrame, width=20)
uTitleColor_Entry.grid(row=14, column=1, sticky='w')

uImagesURL_Label = Label(updateFrame, text="Image URL: ")
uImagesURL_Label.grid(row=15, column=0, sticky='w')
uImageURL_Entry = Entry(updateFrame, width=20)
uImageURL_Entry.grid(row=15, column=1, sticky='w')

uNotes_Label = Label(updateFrame, text="Notes: ")
uNotes_Label.grid(row=10, column=3, sticky='w')
uNotes_Frame = LabelFrame(updateFrame)
uNotes_Frame.grid(row=10, column=4, sticky='w')
uNotes_TextBox = Text(uNotes_Frame, height=5, width=50)
uNotesScroll = Scrollbar(uNotes_Frame, orient=VERTICAL, command=uNotes_TextBox.yview)
uNotes_TextBox['yscroll'] = uNotesScroll.set
uNotesScroll.pack(side=RIGHT, fill=Y)
uNotes_TextBox.pack(side=LEFT)

uSubmit_Button = Button(updateFrame, text="Update", command=updateQuery)
uSubmit_Button.grid(row=15, column=0, columnspan=5)
#------------------------------------------------------

root.mainloop()