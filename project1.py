import csv

# create a list of dictionaries with top row as keys (default) from the csv file
ins_dicts = []
with open('insurance.csv') as insurance_csv:
    insurance_reader = csv.DictReader(insurance_csv)
    for row in insurance_reader:
        ins_dicts.append(dict(row)) 
print(ins_dicts)   # test print to see list of dictionaries

# test function (transfer to class method once I figure out how. DONE)
def average_age(list_of_dictionaries):
    sum_of_ages = 0
    length_of_list = len(list_of_dictionaries)
    for entry in list_of_dictionaries:
        sum_of_ages += int(entry['age'])
    average_age = sum_of_ages / length_of_list
    print(average_age)
# average_age(ins_dicts)  # test out the function

# Task: Build out analysis functions or class methods.
# Create an Insurance class with methods for the dictionary.
class Insurance:
    def __init__(self):
        self.dicts = ins_dicts
        self.total_all = len(self.dicts)
    
    # average age of all patients    
    def average_age(self):
        sum_of_ages = 0
        length_of_list = self.total_all
        for entry in self.dicts:
            sum_of_ages += int(entry['age'])
        average_age = round(sum_of_ages / length_of_list, 2)
        print('Average age of all patients: {age}'.format(age=average_age))
    
    # average age of female patients    
    def average_age_female(self):
        sum_of_ages_female = 0
        total_female = 0
        for entry in self.dicts:
            if entry['sex'] == 'female':
                sum_of_ages_female += int(entry['age'])
                total_female += 1
        average_age = round(sum_of_ages_female / total_female, 2)
        print('Average age of female patients: {age}'.format(age=average_age))
    
    # average age of male patients
    def average_age_male(self):
        sum_of_ages_male = 0
        total_male = 0
        for entry in self.dicts:
            if entry['sex'] == 'male':
                sum_of_ages_male += int(entry['age'])
                total_male += 1
        average_age = round(sum_of_ages_male / total_male, 2)
        print('Average age of male patients: {age}'.format(age=average_age))
    
    # region reported by the greatest number of patients 
    def most_common_region(self):
        northeast_count = 0
        northwest_count = 0
        southeast_count = 0
        southwest_count = 0
        region = ''
        for entry in self.dicts:
            if entry['region'] == 'northeast':
                northeast_count += 1
            elif entry['region'] == 'northwest':
                northwest_count += 1
            elif entry['region'] == 'southeast':
                southeast_count += 1
            elif entry['region'] == 'southwest':
                southwest_count += 1
        max_region = max(northeast_count, northwest_count, southeast_count, southwest_count)
        if max_region == northeast_count:
            region = 'Northeast'
        elif max_region == northwest_count:
            region = 'Northwest'
        elif max_region == southeast_count:
            region = 'Southeast'
        elif max_region == southwest_count:
            region = 'Southwest'
        print('Most commonly reported region: {region}'.format(region=region))
    
    # percentage of patients who are smokers
    def percentage_smokers(self):
        total_smokers = 0
        for entry in self.dicts:
            if entry['smoker'] == 'yes':
                total_smokers += 1
        percentage = round(total_smokers / self.total_all, 4) * 100
        print('Patients who are smokers: {percentage} %'.format(percentage=percentage))
    
    # percentage of female patients who are smokers
    def percentage_smokers_female(self):
        total_females = 0
        total_smokers_female = 0
        for entry in self.dicts:
            if entry['sex'] == 'female':
                total_females += 1
                if entry['smoker'] == 'yes':
                    total_smokers_female += 1
        percentage = round(total_smokers_female / total_females, 4) * 100
        print('Female patients who are smokers: {percentage} %'.format(percentage=percentage))
    
    # percentage of male patients who are smokers
    def percentage_smokers_male(self):
        total_males = 0
        total_smokers_male = 0
        for entry in self.dicts:
            if entry['sex'] == 'male':
                total_males += 1
                if entry['smoker'] == 'yes':
                    total_smokers_male += 1
        percentage = round(total_smokers_male / total_males, 4) * 100
        print('Male patients who are smokers: {percentage} %'.format(percentage=percentage))
        
    # average cost for all patients who smoke and have no children
    def avg_cost_smoker_nochildren(self):
        total_costs = 0
        total_smokers_nochildren = 0
        for entry in self.dicts:
            if entry['smoker'] == 'yes' and entry['children'] == '0':
                total_smokers_nochildren += 1
                total_costs += float(entry['charges'])
        average_cost = round(total_costs / total_smokers_nochildren, 2)
        print('Average cost for patients with no children who smoke: ${cost}'.format(cost=average_cost))
        
    # average cost for all patients who do not smoke and have no children
    def avg_cost_nonsmoker_nochildren(self):
        total_costs = 0
        total_nonsmokers_nochildren = 0
        for entry in self.dicts:
            if entry['smoker'] == 'no' and entry['children'] == '0':
                total_nonsmokers_nochildren += 1
                total_costs += float(entry['charges'])
        average_cost = round(total_costs / total_nonsmokers_nochildren, 2)
        print('Average cost for patients with no children who do NOT smoke: ${cost}'.format(cost=average_cost))
    
    # average bmi for male patients
    def avg_bmi_male(self):
        total_bmis = 0
        total_patients = 0
        for entry in self.dicts:
            if entry['sex'] == 'male':
                total_bmis += float(entry['bmi'])
                total_patients += 1
        average_bmi = round(total_bmis / total_patients, 2)
        print('Average BMI for male patients: {bmi}'.format(bmi=average_bmi))
        
    
    # average bmi for female patients with no children
    def avg_bmi_female_nochildren(self):
        total_bmis = 0
        total_patients = 0
        for entry in self.dicts:
            if entry['sex'] == 'female' and entry['children'] == '0':
                total_bmis += float(entry['bmi'])
                total_patients += 1
        average_bmi = round(total_bmis / total_patients, 2)
        print('Average BMI for female patients with no children: {bmi}'.format(bmi=average_bmi))
        
    # average bmi for female patients with at least one child
    def avg_bmi_female_withchildren(self):
        total_bmis = 0
        total_patients = 0
        for entry in self.dicts:
            if entry['sex'] == 'female' and int(entry['children']) > 0:
                total_bmis += float(entry['bmi'])
                total_patients += 1
        average_bmi = round(total_bmis / total_patients, 2)
        print('Average BMI for female patients with children: {bmi}'.format(bmi=average_bmi))
        

# implement all the methods
insurance_data = Insurance()
insurance_data.average_age()
insurance_data.average_age_female()
insurance_data.average_age_male()
insurance_data.most_common_region()
insurance_data.percentage_smokers()
insurance_data.percentage_smokers_female()
insurance_data.percentage_smokers_male()
insurance_data.avg_cost_smoker_nochildren()
insurance_data.avg_cost_nonsmoker_nochildren()
insurance_data.avg_bmi_male()
insurance_data.avg_bmi_female_nochildren()
insurance_data.avg_bmi_female_withchildren()