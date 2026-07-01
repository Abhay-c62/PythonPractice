#Parent class
class DietPlan:
    def get_breakfast(self):
        #Base method to be overridden by subclasses
        pass
#child class 1: keto Diet
class KetoDiet(DietPlan):
    def get_breakfast(self):
        return "Keto Breakfast: Avocado and Samosa"

#child class 2: vegan Diet
class VeganDiet(DietPlan):
    def get_breakfast(self):
        return "Vegan Breakfast: Oatmeal,milk,Chia Seeds and Fruits"
    
#child class 3: high Protein Diet
class HighProteinDiet(DietPlan):
    def get_breakfast(self):
        return "High Protein Breakfast: Cereals, Sattu , Greek Yogurt and Nuts"

def print_moring_meal(diet_plan):
    print(f"Today's Breakfast: {diet_plan.get_breakfast()}")  


#Create instances of each diet plan
keto_diet = KetoDiet()
vegan_diet = VeganDiet()
high_protein_diet = HighProteinDiet()

print_moring_meal(keto_diet) 
print_moring_meal(vegan_diet)
print_moring_meal(high_protein_diet)


