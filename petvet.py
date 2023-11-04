#Name: Trey Gentry 
#Prog Purpose: This program finds the cost of pet vaccines & medications for dogs and cats 

# Note pet medications prescribed by licensed veterinarians are not subject to sales tax in Virginia 

#PET CARE MEDS Pricing 
#--------------------------------------
# Canine Vaccines: 
#   1. Bordatella $30.00
#   2. DARP $35.00
#   3. Influenza $48.00 
#   4. Leptospriosis $21.00
#   5. Lyme disease $41.00
#   6. Rabies $25.00
#   7. Full Vaccine Package (includes all vaccines):15% discount

# Canine Heartworm Preventative Chews (price per chew; one chew per month)
#   Small dogs, up to 35 lbs: $9.99
#   Medium-sized dogs, 26 to 50 lbs: $11.99
#   Large dogs: 51-100 lbs: $13.99

# Feline Vaccines:
#   1. Feline leukemia: $35.00
#   2. Feline Viral Rhinotracheitis: $30.00
#   3. Rabies(one year): $25.00
#   4. Full Vaccine Package (includes all vaccines): 10% off 

# Feline Heartworm Preventative Chews (one size): $8.00

import datetime

############## define global variables ###############
# define dog prices
PR_BORD=30
PR_DAPP=35
PR_FLU=48
PR_LEP=21
PR_LYME=41
PR_RAB=25
chews_cost=0
PR_ALL=PR_BORD+PR_DAPP+PR_FLU+PR_LEP+PR_LYME+PR_RAB

PR_CHEWS_SMALL=9.99
PR_CHEWS_MED=11.99
PR_CHEWS_LARGE=13.99

num_chews=0

# define cat prices 
FE_LEUK=35
FE_VIR_RHINO=30
FE_RAB=25

FE_ALL=FE_LEUK+FE_RAB+FE_VIR_RHINO

FE_CHEWS=8.00
chews_cost_f=0
num_chews_f=0


#define global variables



################ define program functions #############

def main():
    more=True
    while more:
        get_user_data()

        if pet_type.upper()=="D":
            get_dog_data()
            perform_dog_calculations()
            display_dog_results()
        else:
            get_cat_data()
            perform_cat_calculations()
            display_cat_results()

        askagain = input("\nWould you like to process anothe pet (Y/N)?:")  
        if askagain.upper() =="N":
            more=False
            print("Thank you for trusting PET CARE MEDS with your pet vaccines and medications.")

def get_user_data():
    global pet_name, pet_type, pet_weight
    pet_name= input("Pet name: ")   
    pet_type= input ("Is this pet a dog (D) or cat (c)? ")   
    pet_weight= input ("Weight of your pet (in pounds): ")   



############## Dog functions #################   
def get_dog_data():
    global pet_vax_type, num_chews
    dog1="\n** Dog Vaccines: \n\t1.Bordatella \n\t2.DAPP \n\t3.Influenza \n\t4.Leptospirosis"
    dog2="\n\t5.Lyme Disease \n\t6.Rabies \n\t7.Full Vaccine Package \n\t8.NONE"
    dogmenu= dog1+dog2
    pet_vax_type= int(input(dogmenu+ "\n** Enter Vaccine Number: "))

    print('\nMonthly heartworm prevention medication is recommendef for all dogs.')
    heart_yesno=input('Would you like to order monthly heartworm medication for'+ pet_name + "(Y/N)? ")
    if heart_yesno.upper== "Y":
        num_chews= int(input("How many heart worm chews would you like to order? "))

def perform_dog_calculations():
    global vax_cost, chews_cost, total, num_chews

    ##### vaccines
    if pet_vax_type== 1:
        vax_cost=PR_BORD

    elif pet_vax_type==2:
        vax_cost=PR_DAPP

    elif pet_vax_type==3:
        vax_cost=PR_FLU

    elif pet_vax_type==4:
        vax_cost=PR_LEP

    elif pet_vax_type==5:
        vax_cost=PR_LYME

    elif pet_vax_type==6:
        vax_cost=PR_RAB

    else:
        PR_ALL=PR_BORD + PR_FLU + PR_DAPP + PR_LEP + PR_LYME + PR_RAB
        vax_cost=.85* PR_ALL

    ##### heart worm chews 
    if num_chews!= 0:    
        if pet_weight < 25:
            chews_cost= num_chews*PR_CHEWS_SMALL

        elif pet_weight >= 26 and pet_weight < 50:
            chews_cost= num_chews*PR_CHEWS_MED    

        else:
            chews_cost=num_chews*PR_CHEWS_LARGE

    ###### find total
    total = vax_cost + chews_cost                   

def display_dog_results ():
    moneyf="8,.2f"
    line= '---------------------------'
    print (line)
    print ('***** PET CARE MEDS *******')
    print (line)
    print ('Bordatella ammount $)' + format(PR_BORD,moneyf))
    print('DAPP Amount         $)' + format(PR_DAPP,moneyf))
    print('Influenza ammount   $)' + format(PR_FLU,moneyf))
    print('Lepto ammount       $)' + format(PR_LEP,moneyf))
    print('Lyme disease ammount$)' + format(PR_LYME,moneyf))
    print('Rabies ammount      $)' + format(PR_RAB,moneyf))
    print('Full vax pkg amt    $)' + format(.85*PR_ALL,moneyf))
    print('Large Chews ammount $)' + format(PR_CHEWS_LARGE,moneyf))
    print('Med Chews ammount   $)' + format(PR_CHEWS_MED,moneyf))
    print('Total ammount       $)' + format(total,moneyf))

############## Cat Functions ##################def get_dog_data():
def get_cat_data():  
    global pet_vax_type_f, num_chews_f
    cat1="\n** Cat Vaccines: \n\t1.Feline Leukemia \n\t2.Feline Viral Rhinotracheitis \n\t3.Rabies  \n\t4.Full Vaccine Package"
    catmenu= cat1
    pet_vax_type_f= int(input(catmenu+ "\n** Enter Vaccine Number: "))

    print('\nMonthly heartworm prevention medication is recommended for all cats.')
    heart_yesno=input('Would you like to order monthly heartworm medication for' + pet_name + "(Y/N)? ")
    if heart_yesno.upper== "Y":
        num_chews_f=int(input("How many heart worm chews would you like to order?"))

def perform_cat_calculations():
    global vax_cost_f, chews_cost_f, total_cost

    ##### vaccines
    if pet_vax_type_f== 1:
        vax_cost_f=FE_LEUK

    elif pet_vax_type_f==2:
        vax_cost_f=FE_VIR_RHINO

    elif pet_vax_type_f==3:
        vax_cost_f=FE_RAB

    else:
        FE_ALL= FE_LEUK+ FE_VIR_RHINO+ FE_RAB
        vax_cost_f= .90 * FE_ALL

    ##### chews
    if num_chews_f != 0:
        chews_cost_f=num_chews_f*FE_CHEWS

    ##### find total cost

    total_cost= vax_cost_f+ chews_cost_f
             
def display_cat_results ():
    moneyf="8,.2f"
    line= '---------------------------'
    print (line)
    print ('***** PET CARE MEDS *******')
    print (line)
    print ('Feline Leukemia amt           $)' + format(FE_LEUK,moneyf))
    print ('Feline Viral Rhino amt        $)' + format(FE_VIR_RHINO,moneyf))
    print ('Rabies amount                 $)' + format(FE_RAB,moneyf))
    print ('Feline chews ammount          $)' + format(FE_CHEWS,moneyf))
    print ('Full vax package ammount      $)' + format(.9*FE_ALL,moneyf))
    print ('Total ammount                 $)' + format(total_cost,moneyf))


main()