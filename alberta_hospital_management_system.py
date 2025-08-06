from typing import Final
from enum import Enum
#================================================================
# Assignment: Classes v1.1 (Updated 07/24/2025)
# Submitted by: Estaca, Marc Edison
#================================================================
# Scenario
# Alberta Hospital (AH) is a new healthcare provider in Alberta. 
# To complement the existing large-scale hospitals located in urban 
# settings, AH is building a network of smaller scale mini-hospitals 
# which target underserved rural populations. AH has hired your company 
# to create a management system which is customized to meet their unique 
# operational needs.
#==========================================================================

#==========================================================================
# Doctor Manager
#==========================================================================
class DoctorManager: 
    # filename of where the doctor data is stored
    FILENAME:Final = "doctors"

    # separator for the file
    SEPARATOR:Final = "_"

    # headers for the file
    FILE_HEADER:Final = ("id", "name", "specilist", "timing", "qualification", "roomNb")
    
    # class used as enum for the __find_doctor_index function
    class SearchCriteria:
        NAME:Final = "name"
        ID:Final = "ID"

    #==========================================================================
    # Constructor
    # - It creates an empty list of doctors.
    # - It calls read_doctors_file() to load doctors data from doctorss.txt into 
    #   this list.
    #==========================================================================
    def __init__(self):
        self.__doctors_list = []
        self.read_doctors_file()

    #==========================================================================
    # format_dr_info takes doctor object returns formatted string
    # - It receives a doctor object.
    # - It formats doctor object information similarly to the format used 
    #   in doctors TXT file (i.e., properties separated by underscore).
    #==========================================================================
    def format_dr_info(self, doctor):
        return (
            f"{doctor.get_doctor_id()}{DoctorManager.SEPARATOR}"
            f"{doctor.get_name()}{DoctorManager.SEPARATOR}"
            f"{doctor.get_specialization()}{DoctorManager.SEPARATOR}"
            f"{doctor.get_working_time()}{DoctorManager.SEPARATOR}"
            f"{doctor.get_qualification()}{DoctorManager.SEPARATOR}"
            f"{doctor.get_room_number()}"
        )

    #==========================================================================
    # enter_dr_info takes nothing returns doctor object
    # - Asks the user to enter the doctor info (id, name, etc.).
    # - Creates a doctor object using the entered information.
    # - Returns the created doctor object.
    #==========================================================================
    def enter_dr_info(self):
        id = input("\nEnter the doctor's ID: ")
        name = input("Enter the doctor's name: ")
        speciality = input("Enter the doctor's specility: ")
        working_time = input("Enter the doctor's timing (e.g., 7am-10pm): ")
        qualification = input("Enter the doctor's qualification: ")
        room = input("Enter the doctor's room number: ")

        doctor_data = {
            DoctorManager.Doctor.Keys.KEY_DOCTOR_ID: id,
            DoctorManager.Doctor.Keys.KEY_NAME: name,
            DoctorManager.Doctor.Keys.KEY_SPECIALIZATION: speciality,
            DoctorManager.Doctor.Keys.KEY_WORKING_TIME: working_time,
            DoctorManager.Doctor.Keys.KEY_QUALIFICATION: qualification,
            DoctorManager.Doctor.Keys.KEY_ROOM_NUMBER: room
        }

        return DoctorManager.Doctor(**doctor_data)

    #==========================================================================
    # read_doctors_file takes nothing returns nothing
    # - Reads doctors data from file doctors.txt.
    # - Create an object for each doctor record.
    # - Append doctor objects to the doctors list.
    #==========================================================================    
    def read_doctors_file(self):
        with open(f"{DoctorManager.FILENAME}.txt", "r") as file:

            # Omit the headers
            doctors_list = file.readlines()[1:] 

            for doctor in doctors_list:
                doctor_info = doctor.strip().split(DoctorManager.SEPARATOR)

                doctor_data = {
                    DoctorManager.Doctor.Keys.KEY_DOCTOR_ID : doctor_info[0],
                    DoctorManager.Doctor.Keys.KEY_NAME : doctor_info[1],
                    DoctorManager.Doctor.Keys.KEY_SPECIALIZATION : doctor_info[2],
                    DoctorManager.Doctor.Keys.KEY_WORKING_TIME : doctor_info[3],
                    DoctorManager.Doctor.Keys.KEY_QUALIFICATION : doctor_info[4],
                    DoctorManager.Doctor.Keys.KEY_ROOM_NUMBER : doctor_info[5]
                }
                
                self.__doctors_list.append(DoctorManager.Doctor(**doctor_data))

    #==========================================================================
    # search_doctor_by_id takes nothing returns nothing
    # - Searches for a doctor using their ID.
    # - Accepts doctor ID from the user.
    # - Iterates through the doctors list to check if a doctor with the entered 
    #   id exists or not.
    # - If the doctor exists, it displays the doctor information formatted as in 
    #   the project output file.Otherwise, it displays “Can’t find the doctor….”.
    #==========================================================================    
    def search_doctor_by_id(self):
        id = input("\nEnter the doctor Id: ")

        index=self.__find_doctor_index(DoctorManager.SearchCriteria.ID, id)

        if index!=None:
            self.__display_doctor_info_index(index)

    #==========================================================================
    # search_doctor_by_name takes nothing returns nothing
    # - Searches for a doctor using their name.
    # - Accepts doctor name from the user.
    # - Iterates through the doctors list to check if a doctor with the entered 
    #   name exists or not.
    # - If the doctor exists, it displays the doctor information formatted as in 
    #   the project output file.Otherwise, it displays “Can’t find the doctor….”.
    #==========================================================================   
    def search_doctor_by_name(self):
        name = input("\nEnter the doctor name: ")

        index=self.__find_doctor_index(DoctorManager.SearchCriteria.NAME, name)

        if index!=None:
            self.__display_doctor_info_index(index)

    #==========================================================================
    # display_doctor_info takes doctor object returns nothing
    # - It takes a doctor object and displays doctor info as in the project 
    #   output file.
    #========================================================================== 
    def display_doctor_info(self, doctor):
        print(f"\n{doctor.get_doctor_id():<5}", end="")
        print(f"{doctor.get_name():<23}", end="")
        print(f"{doctor.get_specialization():<16}", end="")
        print(f"{doctor.get_working_time():<16}", end="")
        print(f"{doctor.get_qualification():<16}", end="")
        print(f"{doctor.get_room_number()}")

    #========================================================================== 
    # edit_doctor_info takes nothing returns nothing
    # - Asks the user to enter the doctor id which the user wants to edit.
    # - Searches the doctors list to find the doctor who has the entered id.
    # - If the doctor exists, get the new values for name, speciality, timing, qualification and room number from the user.
    #   oUpdates this information in the list.
    #   oWrites the updated doctors list to doctors.txt.
    #   oConfirms that the doctor has been edited
    # - If the doctor does not exist, it displays “Cannot find the doctor …..”.
    #========================================================================== 
    def edit_doctor_info(self):
        id = input("\nPlease enter the id of the doctor that you want to edit their information: ")

        index=self.__find_doctor_index(DoctorManager.SearchCriteria.ID, id)

        if index!=None:
            name = input("Enter new Name: ")
            speciality = input("Enter new Specilist in: ")
            work_time = input("Enter new Timing: ")
            qualification = input("Enter new Qualification: ")
            room = input("Enter new Room number: ")
            
            self.__doctors_list[index].set_name(name)
            self.__doctors_list[index].set_specialization(speciality)
            self.__doctors_list[index].set_working_time(work_time)
            self.__doctors_list[index].set_qualification(qualification)
            self.__doctors_list[index].set_room_number(room)

            self.write_list_of_doctors_to_file()
            
            print(f"\nDoctor whose ID is {id} has been edited")

    #========================================================================== 
    # display_doctors_list takes nothing returns nothing
    # - Iterates through the doctors list and display doctor’s information as 
    # shown in the project output file.
    #========================================================================== 
    def display_doctors_list(self):
        DoctorManager.__display_headers()
        for doctor in self.__doctors_list:
            self.display_doctor_info(doctor)

    #========================================================================== 
    # write_list_of_doctors_to_file takes nothing returns nothing
    # - Writes a list of doctors into the doctorss.txt file.
    #   o Iterates through doctors list.
    #   o Each doctor information must be formatted using format_dr_info() 
    #     before writing it in the doctors.txt file.
    #========================================================================== 
    def write_list_of_doctors_to_file(self):
        with open(f"{DoctorManager.FILENAME}.txt", "w") as file:
            file.write(DoctorManager.SEPARATOR.join(DoctorManager.FILE_HEADER))
            file.write("\n")

            for doctor in self.__doctors_list:
                file.write(self.format_dr_info(doctor))
                file.write("\n")

    #========================================================================== 
    # add_dr_to_file takes nothing returns nothing
    # - It asks the user to enter the new doctor information such as id, name, 
    #   speciality, qualification, and room number.
    #   o Hint, use enter_dr_info() to get the doctor information from the user
    # - Appends the new doctor object to doctors list.
    # - Formats this information to match the doctors.txt format.
    # - Appends the new doctor to doctors file.
    # - Confirms that a new doctor has been added
    #========================================================================== 
    def add_dr_to_file(self):
        doctor = self.enter_dr_info()
        self.__doctors_list.append(doctor)
        self.write_list_of_doctors_to_file()
        print(f"\nDoctor whose ID is {doctor.get_doctor_id()} has been added")

    #========================================================================== 
    # Helper Methods
    #========================================================================== 

    #========================================================================== 
    # __display_headers takes nothing returns nothing
    # - Displays te header of for the doctor object
    #========================================================================== 
    @staticmethod
    def __display_headers():
        print(f"{'Id':<5}", end="")
        print(f"{'Name':<23}", end="")
        print(f"{'Speciality':<16}", end="")
        print(f"{'Timing':<16}", end="")
        print(f"{'Qualification':<16}", end="")
        print('Room Number')

    #========================================================================== 
    # __display_doctor_info_index takes index returns nothing
    # -Displays the doctor info of the given index from the list of doctors
    #========================================================================== 
    def __display_doctor_info_index(self, index):
        print()
        DoctorManager.__display_headers()
        self.display_doctor_info(self.__doctors_list[index])

    #========================================================================== 
    # __find_doctor_index takes criteria (name or id), value returns the index if found
    # - Finds and returns the doctor's index based on a given criteria
    #========================================================================== 
    def __find_doctor_index(self, criteria, value):
        for index in range(len(self.__doctors_list)):
            doctor = self.__doctors_list[index]

            if criteria == DoctorManager.SearchCriteria.ID:
                if value == doctor.get_doctor_id():
                    return index
            elif criteria == DoctorManager.SearchCriteria.NAME:
                if value.strip().upper() == doctor.get_name().strip().upper():
                    return index
                
        print(f"Can't find the doctor with the same {criteria} on the system") 

    #==========================================================================
    # Doctor Class
    # Rationale: Only the DoctorManager class interacts with the Doctor class.
    # Hence, Doctor class is an inner class of DoctorManager class
    #==========================================================================
    class Doctor:
        #==========================================================================
        # Keys
        #==========================================================================
        class Keys:
            KEY_DOCTOR_ID:Final = "ID"
            KEY_NAME:Final = "NAME"
            KEY_SPECIALIZATION:Final = "SPECIALIZATION"
            KEY_WORKING_TIME:Final = "WORKING_TIME"
            KEY_QUALIFICATION:Final = "QUALIFICATION"
            KEY_ROOM_NUMBER:Final = "ROOM_NUMBER"

        #==========================================================================
        # Constructor
        #==========================================================================
        def __init__(self, **doctor_data):
            self.__doctor_id = doctor_data[DoctorManager.Doctor.Keys.KEY_DOCTOR_ID]
            self.__name = doctor_data[DoctorManager.Doctor.Keys.KEY_NAME]
            self.__specialization = doctor_data[DoctorManager.Doctor.Keys.KEY_SPECIALIZATION]
            self.__working_time = doctor_data[DoctorManager.Doctor.Keys.KEY_WORKING_TIME]
            self.__qualification = doctor_data[DoctorManager.Doctor.Keys.KEY_QUALIFICATION]
            self.__room_number = doctor_data[DoctorManager.Doctor.Keys.KEY_ROOM_NUMBER]

        #==========================================================================
        # Getters
        #==========================================================================
        def get_doctor_id(self):
            return self.__doctor_id
        
        def get_name(self):
            return self.__name
        
        def get_specialization(self):
            return self.__specialization
        
        def get_working_time(self):
            return self.__working_time
        
        def get_qualification(self):
            return self.__qualification
        
        def get_room_number(self):
            return self.__room_number
        
        #==========================================================================
        # Setters
        #==========================================================================
        def set_doctor_id(self, value):
            self.__doctor_id = value

        def set_name(self, value):
            self.__name = value
        
        def set_specialization(self, value):
            self.__specialization = value

        def set_working_time(self, value):
            self.__working_time = value

        def set_qualification(self, value):
            self.__qualification = value

        def set_room_number(self, value):
            self.__room_number = value

        #==========================================================================
        # Magic Method
        # - It returns the string representation of a doctor object. 
        # - This representation should include all doctor properties separated by 
        #   underscore (_)
        #==========================================================================
        def __str__(self):
            return (
                f"{self.__doctor_id}{DoctorManager.SEPARATOR}"
                f"{self.__name}{DoctorManager.SEPARATOR}"
                f"{self.__specialization}{DoctorManager.SEPARATOR}" 
                f"{self.__working_time}{DoctorManager.SEPARATOR}"
                f"{self.__qualification}{DoctorManager.SEPARATOR}"
                f"{self.__room_number}"
            )
    #==========================================================================
    # End of Doctor Class
    #==========================================================================   

#==========================================================================
# End of Doctor Manager
#==========================================================================   

#==========================================================================
# Patient Manager
#==========================================================================
class PatientManager:

    FILENAME:Final = "patients"
    SEPARATOR:Final = "_"
    FILE_HEADER:Final = ("id", "Name", "Disease", "Gender", "Age")

    #==========================================================================
    # Constructor
    # - It creates an empty list of patients.
    # - It calls read_patients_file() to load patient data from patients.txt into 
    #   this list
    #==========================================================================
    def __init__(self):
        self.__patients_list = []
        self.read_patient_file()

    #==========================================================================
    # format_patient_info_for_file takes patient object returns formatted string
    # - It receives a patient object.
    # - It formats patient object information similarly to the format used in 
    #   patients file (i.e., properties separated by underscore)
    #==========================================================================
    def format_patient_info_for_file(self, patient):
        return (
            f"{patient.get_pid()}{PatientManager.SEPARATOR}"
            f"{patient.get_name()}{PatientManager.SEPARATOR}"
            f"{patient.get_disease()}{PatientManager.SEPARATOR}"
            f"{patient.get_gender()}{PatientManager.SEPARATOR}"
            f"{patient.get_age()}"
        )
    
    #==========================================================================
    # enter_patient_info takes nothing returns patient object
    # - Asks the user to enter the patient info (id, name, etc.)
    # - Creates a patient object using the entered information
    # - Returns the created patient object
    #==========================================================================
    def enter_patient_info(self):
        id = input("\nEnter Patient id: ")
        name = input("Enter Patient name: ")
        disease = input("Enter Patient disease: ")
        gender = input("Enter Patient gender: ")
        age = input("Enter Patient age: ")

        patient_data = {
            PatientManager.Patient.Keys.KEY_PID: id,
            PatientManager.Patient.Keys.KEY_NAME: name,
            PatientManager.Patient.Keys.KEY_DISEASE: disease,
            PatientManager.Patient.Keys.KEY_GENDER: gender,
            PatientManager.Patient.Keys.KEY_AGE: age
        }
        return PatientManager.Patient(**patient_data)

    #==========================================================================
    # read_patient_file takes nothing returns nothing
    # - Reads patients data from file patients.txt
    # - Create an object for each patient record
    # - Append patient objects to the patients list
    #==========================================================================
    def read_patient_file(self):
        with open(f"{PatientManager.FILENAME}.txt", "r") as file:
            patients_list = file.readlines()[1:] 
            for patient in patients_list:
                patient_info = patient.strip().split(PatientManager.SEPARATOR)
                patient_data = {
                    PatientManager.Patient.Keys.KEY_PID : patient_info[0],
                    PatientManager.Patient.Keys.KEY_NAME : patient_info[1],
                    PatientManager.Patient.Keys.KEY_DISEASE : patient_info[2],
                    PatientManager.Patient.Keys.KEY_GENDER : patient_info[3],
                    PatientManager.Patient.Keys.KEY_AGE : patient_info[4]
                }
                self.__patients_list.append(PatientManager.Patient(**patient_data))
    
    #==========================================================================
    # search_patient_by_id takes nothing returns nothing
    # - Searches for a patient using their ID
    # - It accepts patient ID from the user
    # - Iterates through the patients list to check if a patient with the 
    #   entered id exists or not
    # - If the patient exists, it displays the patient information formatted as 
    #   in the project output file.
    # - Otherwise, it displays “Can’t find the patient….”
    #==========================================================================
    def search_patient_by_id(self):
        id = input("\nEnter the Patient Id: ")
        index=self.__find_patient_index(id)
        if index!=None:
            print()
            PatientManager.__display_headers()
            self.display_patient_info(self.__patients_list[index])

    #==========================================================================
    # display_patient_info takes patient object returns nothing
    # - It takes a patient object and displays patient info as in the project 
    #   output file
    #==========================================================================
    def display_patient_info(self, patient):
        print(f"\n{patient.get_pid():<5}", end="")
        print(f"{patient.get_name():<23}", end="")
        print(f"{patient.get_disease():<16}", end="")
        print(f"{patient.get_gender():<16}", end="")
        print(f"{patient.get_age():<16}")

    #==========================================================================
    # edit_patient_info_by_id takes nothing returns nothing
    # - Asks the user to enter the patient id which the user wants to edit.
    # - Searches the patients list to find this patient.
    # - If the patient exists, get the new values for name, disease, gender, 
    #   and age from the user.
    #   o Updates this patient information in the list.
    #   o Writes the updated patients list to patients.txt.
    #   o Confirms that the patient has been edited
    # - If the patient does not exist, it displays “Cannot find the patient …..”.
    #==========================================================================
    def edit_patient_info_by_id(self):
        id = input("\nPlease enter the id of the Patient that you want to edit their information: ")
        index=self.__find_patient_index(id)
        if index!=None:
            name = input("Enter new Name: ")
            disease = input("Enter new disease: ")
            gender = input("Enter new gender: ")
            age = input("Enter new age: ")

            self.__patients_list[index].set_name(name)
            self.__patients_list[index].set_disease(disease)
            self.__patients_list[index].set_gender(gender)
            self.__patients_list[index].set_age(age)

            self.write_list_of_patients_to_file()                

            print(f"\nPatient whose ID is {id} has been edited.")

    #==========================================================================
    # display_patients_list takes nothing returns nothing
    # - Iterates through the patients list and display patients information as 
    #   shown in the project output file.
    #==========================================================================
    def display_patients_list(self):
        PatientManager.__display_headers()
        for patient in self.__patients_list:
            self.display_patient_info(patient)

    #==========================================================================
    # write_list_of_patients_to_file takes nothing returns nothing
    # - Writes a list of patients into the patients.txt file.
    # - The patient information must be formatted using 
    #   format_patient_info_for_file() before writing it in the patients.txt 
    #   file.
    #==========================================================================
    def write_list_of_patients_to_file(self):
        with open(f"{PatientManager.FILENAME}.txt", "w") as file:
            file.write(PatientManager.SEPARATOR.join(PatientManager.FILE_HEADER))
            file.write("\n")

            for patient in self.__patients_list:
                file.write(self.format_patient_info_for_file(patient))
                file.write("\n")

    #==========================================================================
    # add_patient_to_file takes nothing returns nothing
    # - It asks the user to enter the new patient information such as id, name, 
    #   disease, etc.
    #   o Hint, use enter_patient_info() to get the patient information from 
    #   the user.
    # - Appends the new patient object to patients list.
    # - Formats this information to match the patients.txt format.
    # - Appends the new patient to patients file.
    # - Confirms that a new patient has been added
    #==========================================================================
    def add_patient_to_file(self):
        patient = self.enter_patient_info()
        self.__patients_list.append(patient)
        self.write_list_of_patients_to_file()
        print(f"\nPatient whose ID is {patient.get_pid()} has been added.")

    #========================================================================== 
    # __display_headers takes nothing returns nothing
    # - Displays te header of for the patient object
    #========================================================================== 
    @staticmethod
    def __display_headers():
        print(f"{'Id':<5}", end="")
        print(f"{'Name':<23}", end="")
        print(f"{'Disease':<16}", end="")
        print(f"{'Gender':<16}", end="")
        print(f"{'Age':<16}")

    #========================================================================== 
    # __find_patient_index takes id returns the index if found
    # - Finds and returns the patient's index based on a given criteria
    #========================================================================== 
    def __find_patient_index(self, id):
        for index in range(len(self.__patients_list)):
            patient = self.__patients_list[index]
            if (id== patient.get_pid()):
                return index
        print("Can't find the Patient with the same id on the system")

    #==========================================================================
    # Patient Class
    # Same rationale as the Doctor class. Only the PatientManager uses this class
    # Hence, its an inner class
    #==========================================================================
    class Patient:
        #==========================================================================
        # Keys
        #==========================================================================
        class Keys:
            KEY_PID:Final = "PID"
            KEY_NAME:Final = "NAME"
            KEY_DISEASE:Final = "DISEASE"
            KEY_GENDER:Final = "GENDER"
            KEY_AGE:Final = "AGE"

        #==========================================================================
        # Constructor
        #==========================================================================
        def __init__(self, **patient_data):
            self.__pid =  patient_data[PatientManager.Patient.Keys.KEY_PID]
            self.__name = patient_data[PatientManager.Patient.Keys.KEY_NAME]
            self.__disease = patient_data[PatientManager.Patient.Keys.KEY_DISEASE]
            self.__gender = patient_data[PatientManager.Patient.Keys.KEY_GENDER]
            self.__age = patient_data[PatientManager.Patient.Keys.KEY_AGE]

        #==========================================================================
        # Getters
        #==========================================================================
        def get_pid(self):
            return self.__pid
        
        def get_name(self):
            return self.__name
        
        def get_disease(self):
            return self.__disease
        
        def get_gender(self):
            return self.__gender
        
        def get_age(self):
            return self.__age
        
        #==========================================================================
        # Setters
        #==========================================================================
        def set_pid(self, value):
            self.__pid = value

        def set_name(self, value):
            self.__name = value

        def set_disease(self, value):
            self.__disease = value

        def set_gender(self, value):
            self.__gender = value

        def set_age(self, value):
            self.__age = value

        #==========================================================================
        # Magic Method
        #==========================================================================
        def __str__(self):
            return (
                f"{self.__pid}{PatientManager.SEPARATOR}"
                f"{self.__name}{PatientManager.SEPARATOR}"
                f"{self.__disease}{PatientManager.SEPARATOR}" 
                f"{self.__gender}{PatientManager.SEPARATOR}"
                f"{self.__age}"
            )
    #==========================================================================
    # End of Patient Class
    #==========================================================================
#==========================================================================
# End of Patient Manager
#==========================================================================

#==========================================================================
# Management
#==========================================================================
class Management:

    #==========================================================================
    # Keys
    #==========================================================================
    class Keys:
        KEY_MAIN_MENU:Final = "MAIN"
        KEY_DOCTORS_MENU:Final = "DOCTORS"
        KEY_PATIENTS_MENU:Final = "PATIENTS"
        KEY_PROMPT:Final = "PROMPT"
        KEY_OPTIONS:Final = "OPTIONS"

    #==========================================================================
    # Main Menu Actions
    #==========================================================================
    class MainMenu:
        class MenuActions(Enum):
            DOCTORS:Final = 1
            PATIENTS:Final = 2
            EXIT:Final = 3
    
    #==========================================================================
    # Doctors Menu Actions
    #==========================================================================
    class DoctorsMenu:
        class MenuActions(Enum):
            DISPLAY_DOCTORS_LIST:Final = 1
            SEARCH_FOR_DOCTOR_BY_ID:Final = 2
            SEARCH_FOR_DOCTOR_BY_NAME:Final = 3
            ADD_DOCTOR:Final = 4
            EDIT_DOCTOR_INFO:Final = 5 
            BACK_TO_MAIN:Final = 6
    
    #==========================================================================
    # Patients Menu Actions
    #==========================================================================
    class PatientsMenu:
        class MenuActions(Enum):
            DISPLAY_PATIENTS_LIST:Final = 1
            SEARCH_FOR_PATIENT_BY_ID:Final = 2
            ADD_PATIENT:Final = 3
            EDIT_PATIENT_INFO:Final = 4
            BACK_TO_MAIN:Final = 5

    #==========================================================================
    # Menu Structure
    # Menu  -> Prompt
    #       -> Actions
    #==========================================================================
    MENU_DATA:Final = {
        Keys.KEY_MAIN_MENU : {
            Keys.KEY_PROMPT : ("Welcome to Alberta Hospital (AH) Managment system\n"
                "Select from the following options, or select 3 to stop:"),
            Keys.KEY_OPTIONS : {
                1: f"{' ':3} Doctors",
                2: f"{' ':3} Patients",
                3: f"Exit Program"
            },
        },
        Keys.KEY_DOCTORS_MENU : {
            Keys.KEY_PROMPT : "\nDoctors Menu:",
            Keys.KEY_OPTIONS : {
                1: "Display Doctors list",
                2: "Search for doctor by ID",
                3: "Search for doctor by name",
                4: "Add doctor",
                5: "Edit doctor info",
                6: "Back to the Main Menu"
            },
        },
        Keys.KEY_PATIENTS_MENU : {
            Keys.KEY_PROMPT: "\nPatients Menu:",
            Keys.KEY_OPTIONS : {
                1: "Display patients list",
                2: "Search for patient by ID",
                3: "Add patient",
                4: "Edit patient info",
                5: "Back to the Main Menu"    
            },
        }
    }

    def __init__(self):
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    #==========================================================================
    # display_menu takes nothing returns nothing
    # - It displays the main menu which has 3 options (1 for Doctors submenu, 
    #   2 for Patients submenu, and 3 for exiting the program.
    #   o The program should continue displaying the main menu until the user 
    #       enters 3.
    # - When the user selects option 1, Doctors submenu will be displayed to 
    #   allow user working with doctors.
    #   o Doctors menu has 6 options.
    #   o The first 5 options allow a variety of manipulation (displaying 
    #       doctors list, searching by id or name, adding a new doctor, and 
    #       editing existing doctor information) of doctors. 
    #   o Option 6 allows returning to the main menu.
    # - The program should continue displaying the doctors menu until the user 
    #   enters 6.
    # - When the user selects option 2, Patients submenu will be displayed to 
    #   allow user working with patients.
    #   o Patients menu has 5 options.
    #   o The first 4 options allow a variety of manipulation (displaying 
    #       patients list, searching by id, adding a new patient, and editing 
    #       existing patient information) of patients. 
    #   o Option 5 allows returning to the main menu.
    # - The program should continue displaying patients menu until the user enters 5.
    #==========================================================================
    def display_menu(self):
        selection = None
        current_menu = Management.Keys.KEY_MAIN_MENU
        
        # Loop for the main menu
        while selection != Management.MainMenu.MenuActions.EXIT.value:

            #==========================================================================
            # selection is going to be one of the following actions
            # (1 - Doctor Menu, 2 - Patient Menu, 3 - Exit)
            #==========================================================================
            selection = self.__menu_controller(Management.Keys.KEY_MAIN_MENU)

            if selection == Management.MainMenu.MenuActions.DOCTORS.value:
                current_menu = Management.Keys.KEY_DOCTORS_MENU

                # loop for the doctor menu
                while current_menu == Management.Keys.KEY_DOCTORS_MENU:

                    #==========================================================================
                    # selection is going to be one of the following actions
                    # 1 - "Display Doctors list",
                    # 2 - "Search for doctor by ID",
                    # 3 - "Search for doctor by name",
                    # 4 - "Add doctor",
                    # 5 - "Edit doctor info",
                    # 6 - "Back to the Main Menu"
                    #==========================================================================
                    selection = self.__menu_controller(Management.Keys.KEY_DOCTORS_MENU)
                    
                    # Performs the selected action
                    if selection == Management.DoctorsMenu.MenuActions.DISPLAY_DOCTORS_LIST.value:
                        self.doctor_manager.display_doctors_list()
                    elif selection == Management.DoctorsMenu.MenuActions.SEARCH_FOR_DOCTOR_BY_ID.value:
                        self.doctor_manager.search_doctor_by_id()
                    elif selection == Management.DoctorsMenu.MenuActions.SEARCH_FOR_DOCTOR_BY_NAME.value:
                        self.doctor_manager.search_doctor_by_name()
                    elif selection == Management.DoctorsMenu.MenuActions.ADD_DOCTOR.value:
                        self.doctor_manager.add_dr_to_file()
                    elif selection == Management.DoctorsMenu.MenuActions.EDIT_DOCTOR_INFO.value:
                        self.doctor_manager.edit_doctor_info()
                    elif selection == Management.DoctorsMenu.MenuActions.BACK_TO_MAIN.value:
                        current_menu = Management.Keys.KEY_MAIN_MENU
                        print()
            elif selection == Management.MainMenu.MenuActions.PATIENTS.value:
                current_menu = Management.Keys.KEY_PATIENTS_MENU

                # loop for the patient menu
                while current_menu == Management.Keys.KEY_PATIENTS_MENU:

                    #==========================================================================
                    # selection is going to be one of the following actions
                    # 1 - "Display patients list",
                    # 2 - "Search for patient by ID",
                    # 3 - "Add patient",
                    # 4 - "Edit patient info",
                    # 5 - "Back to the Main Menu"    
                    #==========================================================================
                    selection = self.__menu_controller(Management.Keys.KEY_PATIENTS_MENU)

                    # Performs the selected action
                    if selection == Management.PatientsMenu.MenuActions.DISPLAY_PATIENTS_LIST.value:
                        self.patient_manager.display_patients_list()
                    elif selection == Management.PatientsMenu.MenuActions.SEARCH_FOR_PATIENT_BY_ID.value:
                        self.patient_manager.search_patient_by_id()
                    elif selection == Management.PatientsMenu.MenuActions.ADD_PATIENT.value:
                        self.patient_manager.add_patient_to_file()
                    elif selection == Management.PatientsMenu.MenuActions.EDIT_PATIENT_INFO.value:
                        self.patient_manager.edit_patient_info_by_id()
                    elif selection == Management.PatientsMenu.MenuActions.BACK_TO_MAIN.value:
                        current_menu = Management.Keys.KEY_MAIN_MENU
                        print()

        print("Thanks for using the program. Bye!")

    #==========================================================================
    # Helper Method
    # __menu_controller takes current_menu returns selection
    # - Elegantly displays the menu prompt followed by menu actions
    # - Checks if the menu action is valid
    # - returns the selected value for the selection
    #==========================================================================
    def __menu_controller(self, current_menu):
        # prints the prompt of the menu data
        print(Management.MENU_DATA[current_menu][Management.Keys.KEY_PROMPT])

        # prints the selection
        for number, description in Management.MENU_DATA[current_menu][Management.Keys.KEY_OPTIONS].items():
            print(f"{number} - {description}")

        # validates the input
        selection = int(input(">>> "))
        while selection not in  Management.MENU_DATA[current_menu][Management.Keys.KEY_OPTIONS].keys():
            print("Invalid input. Try again.")
            selection = int(input(">>> "))

        return selection

# Driver
def main():
    management = Management()
    management.display_menu()

if __name__ == "__main__":
    main()
