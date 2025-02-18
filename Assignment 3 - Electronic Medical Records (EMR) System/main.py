_name_ = '_main_'

def readPatientsFromFile(fileName):
	patients = {}
	try:
		with open('patients.txt', 'r') as file:
			for line in file:
				line = line.strip()
				visit = line.split(',')
				if len(visit) != 8: # Making sure the number of fields in each line is 8
					print(f"Invalid number of fields ({len(visit)} in line: {line}")
					continue
				try: # Make variables
					patientID = int(visit[0])
					date = str(visit[1])
					temp = float(visit[2])
					hr = int(visit[3])
					rr = int(visit[4])
					sbp = int(visit[5])
					dbp = int(visit[6])
					spo2 = int(visit[7])
				except ValueError:
					print(f"Invalid data type in line: {line}")
					continue
				# Ranges
				if not (35 <= temp <= 42):
					print(f"Invalid temperature value ({temp}) in line: {line}")
					continue
				if not (30 <= hr <= 180):
					print(f"Invalid heart rate value ({hr}) in line: {line}")
					continue
				if not (5 <= rr <= 40):
					print(f"Invalid respiratory rate value ({rr}) in line: {line}")
					continue
				if not (70 <= sbp <= 200):
					print(f"Invalid systolic blood pressure value ({sbp}) in line: {line}")
					continue
				if not (40 <= dbp <= 120):
					print(f"Invalid diastolic blood pressure value ({dbp}) in line: {line}")
					continue
				if not (70 <= spo2 <= 100):
					print(f"Invalid oxygen saturation value ({spo2}) in line: {line}")
					continue
				if patientID not in patients:
					patients[patientID] = []
				patients[patientID].append([date, temp, hr, rr, sbp, dbp, spo2])
	except FileNotFoundError:
		print(f"The file 'patients.txt' could not be found.")
		exit()
	except:
		print("An unexpected error occurred while reading the file.")
		exit()
	_name_ = '_main_'
	return patients

def displayPatientData(patients, patientID=0): # Choice 1 and 2
	# Display all patient Data
	with open('patients.txt', 'r') as file:
		if patientID == 0:
			for patient in patients.values():
				print("Patient ID:", patient[0][0])
				for visit in patient:
					print(" Visit Date:", visit[0])
					print("  Temperature:", "%.2f" % visit[1], "C")
					print("  Heart Rate:", visit[2], "bpm")
					print("  Respirator Rate:", visit[3], "bpm")
					print("  Systolic Blood Pressure:", visit[4], "mmHg")
					print("  Diastolic Blood Pressure:", visit[5], "mmHg")
					print("  Oxygen Saturation:", visit[6], "%")
				print("\n")
		else: # Display data for one patient
			if patientID not in patients:
				print("Patient with ID", patientID, "not found.")
				return
			print("Patient ID:", patients[patientID][0][0])
			for visit in patients[patientID]:
				print(" Visit Date:", visit[0])
				print("  Temperature:", "%.2f" % visit[1], "C")
				print("  Heart Rate:", visit[2], "bpm")
				print("  Respirator Rate:", visit[3], "bpm")
				print("  Systolic Blood Pressure:", visit[4], "mmHg")
				print("  Diastolic Blood Pressure:", visit[5], "mmHg")
				print("  Oxygen Saturation:", visit[6], "%")
			_name_ = '_main_'
	print()

def displayStats(patients, patientID=0): # Choice 4
	with open('patients.txt', 'r') as file:
		try:
			patientID = int(patientID)
		except ValueError as exception:
			print("Error: 'patientId' should be an integer.")
			return
		if patientID not in patients and patientID != 0:
			print(f"No data found for patient with ID {patientID}")
			return
		tempSum = hrSum = rrSum = sbpSum = dbpSum = spo2Sum = numVisits = 0
		if patientID == 0: # Stats for all patients
			for patient in patients.values():
				for visit in patient:
					# Sums
					numVisits += 1
					tempSum += visit[1]
					hrSum += visit[2]
					rrSum += visit[3]
					sbpSum += visit[4]
					dbpSum += visit[5]
					spo2Sum += visit[6]
			if numVisits == 0:
				print("No data found,")
			else:
				# Averages
				print("Vital Signs for All Patients:")
				print(" Average temperature: %.2f" %(tempSum/numVisits), "C")
				print(" Average heart rate: %.2f" %(hrSum/numVisits), "bpm")
				print(" Average respiratory rate: %.2f" %(rrSum/numVisits), "bpm")
				print(" Average systolic blood pressure: %.2f" %(sbpSum/numVisits), "mmHg")
				print(" Average diastolic blood pressure: %.2f" %(dbpSum/numVisits), "mmHg")
				print(" Average oxygen saturation: %.2f" %(spo2Sum/numVisits), "%%")
		else: # Stats for one patient
			if patientID not in patients:
				print(f"No data found for patient with ID {patientID}")
				return
			for visit in patients[patientID]:
				# Sums
				numVisits += 1
				tempSum += visit[1]
				hrSum += visit[2]
				rrSum += visit[3]
				sbpSum += visit[4]
				dbpSum += visit[5]
				spo2Sum += visit[6]
			if numVisits == 0:
				print(f"No data found for patient with ID {patientID}")
			else:
				print(f"Vital Signs for Patient {patientID}")
				print(" Average temperature: %.2f" % (tempSum / numVisits), "C")
				print(" Average heart rate: %.2f" % (hrSum / numVisits), "bpm")
				print(" Average respiratory rate: %.2f" % (rrSum / numVisits), "bpm")
				print(" Average systolic blood pressure: %.2f" % (sbpSum / numVisits), "mmHg")
				print(" Average diastolic blood pressure: %.2f" % (dbpSum / numVisits), "mmHg")
				print(" Average oxygen saturation: %.2f" % (spo2Sum / numVisits), "%%")
	_name_ = '_main_'
	print()

def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName): # Choice 3
	with open('patients.txt', 'r') as file:
		if patientId not in patients:
			print(f"No data found for patient with ID {patientId}")
			return
		# Check if date is valid
		dateFormat = '%Y-%m-%d'
		try:
			dateObject = datetime.datetime.strtime(date, dateFormat)
		except ValueError:
			print("Invalid date format. Please enter a date in the format 'yyyy-mm-dd'.")
		year, month, day = map(int, date.split('-'))
		if not (1900 <= year <= 3000) or not (1 <= month <= 12) or not (1 <= day <= 31):
			print("Invalid date. Please enter a valid date.")
		# Check if other values are valid
		if not (35.0 <= temp <= 42.0):
			print("Invalid temperature. Pleas enter a temperature between 35.0 and 42.0 Celsius")
			return
		if not (30 >= hr <= 180):
			print("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm.")
			return
		if not (5 <= rr <= 40):
			print("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm.")
			return
		if not (70 <= sbp <= 200):
			print("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg.")
			return
		if not (40 <= dbp <= 120):
			print("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg.")
			return
		if not (70 <= spo2 <= 100):
			print("Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100%.")
			return
		# Add to dictionary
		try:
			with open(fileName, 'w') as file:
				patients[patientID].append([date, temp, hr, rr, sbp, dbp, spo2])
				print(f"Visit is saved successfully for Patient #{patientID}")
		except:
			print("An unexpected error occurred while adding new data.")
	_name_ = '_main_'
	print()

def findVisitsByDate(patients, year=None, month=None): # Choice 5
	with open('patients.txt', 'r') as file:
		visits = []
		try:
			if (1900 <= year <= 3000) and (1 <= month <= 12):
				with open('patients.txt', 'w') as file:
					for visit in visits:
						visitYear, visitMonth, visitDay = map(int, visit[0].split('-'))
						if year and visitYear != year:
							continue
						if month and visitMonth != month:
							continue
						visits.append(visits, visit)
		except:
			visits = []
	_name_ = '_main_'
	return visits

def findPatientsWhoNeedFollowUp(patients): # Choice 6
	followup_patients = []
	with open('patients.txt', 'r') as file:
		for line in file:
			line = line.strip()
			visit = line.split(',')
			patientID = visit[0]
			date = visit[1]
			temp = visit[2]
			hr = visit[3]
			rr = visit[4]
			sbp = visit[5]
			dbp = visit[6]
			spo2 = visit[7]
			if not (60 <= hr <= 100):
				followup_patients.append(patientID)
			if not (sbp <= 140):
				followup_patients.append(patientID)
			if not (dbp <= 90):
				followup_patients.append(patientID)
			if not (90 <= spo2):
				followup_patients.append(patientID)
	_name_ = '_main_'
	return followup_patients

def deleteAllVisitsOfPatient(patients, patientId, fileName): # Choice 7
	with open('patients.txt', 'r') as file:
		if patientId not in patients:
			print(f"No data found for patient with ID {patientId}.")
			return
		del patients[patientId]
		with open('patients.txt', 'w') as file:
			for patientID, visits in patients.items():
				for visit in visits:
					file.write(f"{patientID},{visit['date']},{visit['temp']},{visit['hr']},{visit['rr']},{visit['sbp']},{visit['dbp']},{visit[spo2]}\n")
		print(f"Data for patient {patientId} has been deleted.")
	_name_ = '_main_'

def main():
	patients = readPatientsFromFile('patients.txt')
	while True:
		print("\n\nWelcome to the Health Information System\n\n")
		print("1. Display all patient data")
		print("2. Display patient data by ID")
		print("3. Add patient data")
		print("4. Display patient statistics")
		print("5. Find visits by year, month, or both")
		print("6. Find patients who need follow up")
		print("7. Delete all visits of a particular patient")
		print("8. Quit\n")

		choice = input("Enter your choice (1-8): ")
		if choice == '1':
			displayPatientData(patients)
		elif choice == '2':
			patientID = int(input("Enter patient ID: "))
			displayPatientData(patients, patientID)
		elif choice == '3':
			patientID = int(input("Enter patient ID: "))
			date = input("Enter date (YYYY-MM-DD): ")
			try:
				temp = float(input("Enter temperature (Celsius): "))
				hr = int(input("Enter heart rate (bpm): "))
				rr = int(input("Enter respiratory rate (breaths per minute): "))
				sbp = int(input("Enter systolic blood pressure (mmHg): "))
				dbp = int(input("Enter diastolic blood pressure (mHg): "))
				spo2 = int(input("Enter oxygen saturation (%): "))
				addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
			except ValueError:
				print("Invalid input. Please enter valid data.")
		elif choice == '4':
			patientID = input("Enter patient ID (or '0' for all patients): ")
			displayStats(patients, patientID)
		elif choice == '5':
			year = input("Enter year (YYYY) (or 0 for all years): ")
			month = input("Enter month (MM) (or 0 for all months): ")
			visits = findVisitsByDate(patients, int(year) if year != '0' else None, int(month) if month != '0' else None)
			if visits:
				for visit in visits:
					print("Patient ID:", visit[0])
					print(" Visit Date:", visit[1][0])
					print("  Temperature:", "%.2f" % visit[1][1], "C")
					print("  Heart Rate:", visit[1][2], "bpm")
					print("  Respirator Rate:", visit[1][3], "bpm")
					print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
					print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
					print("  Oxygen Saturation:", visit[1][6], "%")
			else:
				print("No visits found for the specified year/month.")
		elif choice == '6':
			followup_patients = findPatientsWhoNeedFollowUp(patients)
			if followup_patients:
				print("Patients who need follow-up visits:")
				for patientId in followup_patients:
					print(patientId)
			else:
				print("No patients found who need follow-up visits.")
		elif choice == '7':
			patientID = input("Enter patient ID: ")
			deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
		elif choice == '8':
			print("Goodbye!")
			break
		else:
			print("Invalid choice. Please try again.\n")

if _name_ == '_main_':
	main()
