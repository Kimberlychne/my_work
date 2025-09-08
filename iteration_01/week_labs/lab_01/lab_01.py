all_users = []

run_program = True

while run_program == True:
    user_data = {}
    user_data['name'] = input("\nPlease enter your name: ")
    user_data['age'] = int(input("please enter your age: "))
    print(f"hello {user_data['name']}!Welcome to the program.")
    multilingual_response = input("Are you multilingual? (yes/no): ").lower()
    user_data['multilingual'] = multilingual_response in ['yes','y']

    if user_data['multilingual']:
        number_of_languages = int(input("How many languagages do you speak?"))
        languages = []
        for i in range(number_of_languages):
            language = input(f'Enter language {i+1}:')
            languages.append(language)
            user_data['languages'] = languages
    else:
        desired_language = input("Enter a language you wish to learn: ")
        user_data['desired_language'] = desired_language

    all_users.append(user_data)

    if user_data['age'] < 13:
            print("You cannot sit in the passenger seat of a car.")
    if user_data['age'] < 18:
            print("You cannot vote.")
    if user_data['age'] < 25:
            print("You cannot rent a car.")
    if user_data['age'] >35:
            print("You are getting old...")    
    if user_data['multilingual']:
            print(f"You speak {len(user_data['languages'])}language(s):{'.'.join(user_data['languages'])}.")   
    else:
            print(f"You wish to learn {user_data['desired_language']}.")

    user_response = input("Would you like to enter another user's data?").lower()
    if user_response == 'yes':
        print("program restart")
    else: 
        run_program = False

print(all_users)
