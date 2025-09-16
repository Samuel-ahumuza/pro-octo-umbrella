def get_vaccine_recommendation(infection):

    vaccine_dict = {
        "influenza": "Influenza vaccine (Flu shot)",
        "measles": "MMR (Measles, Mumps, Rubella) vaccine",
        "polio": "Polio vaccine (IPV or OPV)",
        "tetanus": "Tdap (Tetanus, Diphtheria, Pertussis) vaccine",
        "hepatitis b": "Hepatitis B vaccine",
        "varicella": "Varicella (Chickenpox) vaccine",
        "pneumonia": "Pneumococcal vaccine",
        "diphtheria": "DTP or Tdap vaccine",
        "pertussis": "DTP or Tdap vaccine",
        "meningitis": "Meningococcal conjugate vaccine",
        "covid-19": "COVID-19 vaccine (e.g., Pfizer, Moderna, AstraZeneca)",
    }

    infection_lower = infection.lower()

    if infection_lower in vaccine_dict:
        vaccine = vaccine_dict[infection_lower]
        return f"For **{infection.title()}**, the recommended vaccine is: **{vaccine}**."
    else:
        return f"Sorry, there is no vaccine recommendation for **{infection.title()}** in our database. Please consult a healthcare professional."

if __name__ == "__main__":
    print("Welcome to the Vaccine Recommender!")
    print("-----------------------------------")

    while True:
        user_input_infection = input("Please enter the name of the infection (or type 'exit' to quit): ")

        if user_input_infection.lower() == 'exit':
            print("Thank you for using the Vaccine Recommender. Goodbye!")
            break

        recommendation = get_vaccine_recommendation(user_input_infection)
        print(recommendation)
        print("-" * 45)
