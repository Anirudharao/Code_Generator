class TreeNode:
    def __init__(self, data, code):
        self.data = data
        self.children = []
        self.parent = None
        self.code = code

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def getPatientCode(self, patientID, guardianship, healthHistory, insurance, hospitalReferral, hospitalBill):
        codeString = ""
        for child in self.children:
            if child.data == patientID:
                codeString = codeString + child.code + "__"
            if child.data == guardianship:
                codeString = codeString + child.code + "__"
            if child.data == healthHistory:
                codeString = codeString + child.code + "__"
            if child.data == insurance:
                codeString = codeString + child.code + "__"
            if child.data == hospitalReferral:
                codeString = codeString + child.code + "__"
            if child.data == hospitalBill:
                codeString = codeString + child.code + "__"

        codeString = codeString[:-2]
        print("Patient Code: " + codeString)


    def getDoctorCode(self, doctorID, doctorEducation, license, employment, department, backgroundVerification, patientConsent):
        codeString = ""
        for child in self.children:
            if child.data == doctorID:
                codeString = codeString + child.code + "__"
            if child.data == doctorEducation:
                codeString = codeString + child.code + "__"
            if child.data == license:
                codeString = codeString + child.code + "__"
            if child.data == employment:
                codeString = codeString + child.code + "__"
            if child.data == department:
                codeString = codeString + child.code + "__"
            if child.data == backgroundVerification:
                codeString = codeString + child.code + "__"
            if child.data == patientConsent:
                codeString = codeString + child.code + "__"

        codeString = codeString[:-2]
        print("Doctor Code: " + codeString)


    def getHSPCode(self, HSPRegistration, license, compliance, consent):
        codeString = ""
        for child in self.children:
            if child.data == HSPRegistration:
                codeString = codeString + child.code + "__"
            if child.data == license:
                codeString = codeString + child.code + "__"
            if child.data == compliance:
                codeString = codeString + child.code + "__"
            if child.data == consent:
                codeString = codeString + child.code + "__"

        codeString = codeString[:-2]
        print("Healthcare Service Provider Code: " + codeString)


    def getRICode(self, RIRegistration, license, compliance, consent):
        codeString = ""
        for child in self.children:
            if child.data == RIRegistration:
                codeString = codeString + child.code + "__"
            if child.data == license:
                codeString = codeString + child.code + "__"
            if child.data == compliance:
                codeString = codeString + child.code + "__"
            if child.data == consent:
                codeString = codeString + child.code + "__"

        codeString = codeString[:-2]
        print("Research Institute Code: " + codeString)


    def getIACode(self, IARegistration, license, compliance, consent, bill):
        codeString = ""
        for child in self.children:
            if child.data == IARegistration:
                codeString = codeString + child.code + "__"
            if child.data == license:
                    codeString = codeString + child.code + "__"
            if child.data == compliance:
                codeString = codeString + child.code + "__"
            if child.data == consent:
                codeString = codeString + child.code + "__"
            if child.data == bill:
                codeString = codeString + child.code + "__"

        codeString = codeString[:-2]
        print("Insurance Agency Code: " + codeString)


def build_tree():

    root = TreeNode("Root", "000")

    patient = TreeNode("Patient", "001")
    patient.add_child(TreeNode("Patient_ID: 202201", "001_001"))
    patient.add_child(TreeNode("Guardianship: Parent", "001_010"))
    patient.add_child(TreeNode("Health_History: Cough, Cold", "001_011"))
    patient.add_child(TreeNode("Insurance: HDFC Life", "001_100"))
    patient.add_child(TreeNode("Hospital_Referral: KMC Manipal", "001_101"))
    patient.add_child(TreeNode("Hospital_Bill: 3500", "001_110"))

    education = TreeNode("Education", "010_010")
    education.add_child(TreeNode("MBBS: KMC Manipal", "010_010_001"))
    education.add_child(TreeNode("MD: BMC Bangalore", "010_010_010"))
    education.add_child(TreeNode("DM: Oxford Medical School London", "010_010_011"))

    employment = TreeNode("Employment", "010_100")
    employment.add_child(TreeNode("Current_Employer: KMC Manipal", "010_100_001"))
    employment.add_child(TreeNode("Previous_Employer: TATA Memorial", "010_100_010"))

    department = TreeNode("Department", "010_101")
    department.add_child(TreeNode("Department: General Medicine", "010_101_001"))
    department.add_child(TreeNode("Designation: HOD", "010_101_010"))

    doctor = TreeNode("Doctor", "010")
    doctor.add_child(TreeNode("Doctor_ID: 2003521", "010_001"))
    doctor.add_child(education)
    doctor.add_child(TreeNode("License: L001", "010_011"))
    doctor.add_child(employment)
    doctor.add_child(department)
    doctor.add_child(TreeNode("Background_Verification: Done", "010_110"))
    doctor.add_child(TreeNode("Patient_Consent: Yes", "010_111"))

    healthcareServiceProvider = TreeNode("Healthcare_Service_Provider", "011")
    healthcareServiceProvider.add_child(TreeNode("Registration: Done", "011_001"))
    healthcareServiceProvider.add_child(TreeNode("License: HSP201", "011_010"))
    healthcareServiceProvider.add_child(TreeNode("Quality_Compliance: Complies", "011_011"))
    healthcareServiceProvider.add_child(TreeNode("Patient_Consent: Yes", "011_100"))

    researchInstitute = TreeNode("Research_Institution", "100")
    researchInstitute.add_child(TreeNode("Registration: Done", "100_001"))
    researchInstitute.add_child(TreeNode("License: RI201", "100_010"))
    researchInstitute.add_child(TreeNode("Quality_Compliance: Complies", "100_011"))
    researchInstitute.add_child(TreeNode("Patient_Consent: Yes", "100_100"))

    insuranceAgency = TreeNode("Insurance_Agency", "101")
    insuranceAgency.add_child(TreeNode("Registration: Done", "101_001"))
    insuranceAgency.add_child(TreeNode("License: IA201", "101_010"))
    insuranceAgency.add_child(TreeNode("Quality_Compliance: Complies", "101_011"))
    insuranceAgency.add_child(TreeNode("Patient_Consent: Yes", "101_100"))
    insuranceAgency.add_child(TreeNode("Bill: 4500", "101_101"))

    root.add_child(patient)
    root.add_child(doctor)
    root.add_child(healthcareServiceProvider)
    root.add_child(researchInstitute)
    root.add_child(insuranceAgency)


    choice = input("Enter the entity Press 1 for Patient, 2 for Doctor, 3 for Healthcare service provider, 4 for Research Institue, 5 for Insurance Agency: ")

    if choice == "1":
        patientID = input("Enter patient ID: ")
        guardianship = input("Guardian: ")
        healthHistory = input("Health History: ")
        insurance = input("Insurance: ")
        hospitalReferral = input("Hospiral referrals: ")
        hospitalBill = input("Hospital/Clinic Bills: ")

        patient.getPatientCode(patientID, guardianship, healthHistory, insurance, hospitalReferral, hospitalBill)


    elif choice == "2":
        doctorID = input("Enter Doctor ID: ")
        doctorEducation = input("Enter Doctor's education: ")
        license = input("Enter License Number: ")
        employment = input("Current employer: ")
        department = input("Enter Department: ")
        backgroundVerification = input("Type done if background verification is done: ")
        patientConsent = input("Type yes if patient consent is obtained: ")

        doctor.getDoctorCode(doctorID, doctorEducation, license, employment, department, backgroundVerification, patientConsent)


    elif choice == "3":
        HSPRegistration = input("Type done if Registration is complete: ")
        HSPLicense = input("Enter license number: ")
        HSPQualityCompliance = input("Type Complies if it complies: ")
        HSPConsent = input("Type yes if consent is obtained: ")

        healthcareServiceProvider.getHSPCode(HSPRegistration, HSPLicense, HSPQualityCompliance, HSPConsent)


    elif choice == "4":
        RIRegistration = input("Type done if registration is done: ")
        RILicense = input("Enter the license number: ")
        RICompliance = input("Type complies if quality complies: ")
        RIConsent = input("Type yes if patient consent is obtained: ")

        researchInstitute.getRICode(RIRegistration, RILicense, RICompliance, RIConsent)


    elif choice == "5":
        IARegistration = input("Type done if registration is done: ")
        IALicense = input("Enter the license number: ")
        IACompliance = input("Type Complies if quality complies: ")
        IAConsent = input("Type yes if patient consent is obtained: ")
        bill = input("Enter the bill amount: ")

        insuranceAgency.getIACode(IARegistration, IALicense, IACompliance, IAConsent, bill)

    else:
        print("Enter a valid input")


if __name__ == '__main__':
    build_tree()