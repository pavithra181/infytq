def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    count1=count2=count3=0
    i=1
    a=len(patient_medical_speciality_list)
    for j in range(i,a,i+1):
        if(patient_medical_speciality_list[j]=="p"):
            count1=count1+1
        elif(patient_medical_speciality_list[j]=="o"):
            count2=count2+1
        else:
            count3=count3+1
        if((count1>count2) and (count1>count3)):
            speciality="Pediatrics"
        elif(count2>count3):
            speciality="Orthopedics"
        else:
            speciality="ENT"

    return speciality


patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
