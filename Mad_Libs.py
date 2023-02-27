import random

def story_1():
        print("Now you have to enter several objects' names. Let's start.")
         
        story1 = 'It was about <number> <measure_of_time> ago when I arrived at the hospital in a <mode_of_transportation>. The hospital is a/an <adjective> place, there are a lot of <adjective2> <noun> here. There are nurses here who have <color> <part_of_the_body>. If someone wants to come into my room I told them that they have to <verb> first. I have decorated my room with <number2> <noun2>. Today I talked to a doctor and they were wearing a <noun3> on their <part_of_the_body2>. I heard that all doctors <verb> <noun4> every day for breakfast. The most <adjective3> thing about being in the hospital is the <silly_word> <noun4> !'
    
        objects = ["<number>", "<measure_of_time>", "<mode_of_transportation>", "<adjective>","<adjective2>", "<noun>", "<color>", "<part_of_the_body>", "<verb>", "<number2>", "<noun2>", "<noun3>", "<part_of_the_body2>", "<adjective3>", "<silly_word>", "<noun4>"]
        user_inputs = {}
            
        for x in objects:
            user_inputs[x] = input("Enter a " + x + ": ")
            
        for x, value in user_inputs.items():
            story1 = story1.replace(x, value)
                
        print(story1)
                 
    
def story_2():
        print("Now you have to enter several objects' names. Let's start.")
         
        story2 = 'This weekend I am going camping with <persons_name>. I packed my lantern, sleeping bag, and <noun>. I am so <adjective_feeling> to <verb> in a tent. I am <adjective_feeling2> we might see a(n) <animal>, I hear they are kind of dangerous. While we are camping, we are going to hike, fish, and <verb2>. I have heard that the <color> lake is great for <verb_ending_in_ing>. Then we will <adverb_ending_in_ly> hike through the forest for <number> <measure_of_time>. If I see a <color> <animal2> while hiking, I am going to bring it home as a pet! At night we will tell <number2> <silly_word> stories and roast <noun2> around the campfire!!'
    
        objects = ["<persons_name>", "<noun>", "<adjective_feeling>", "<verb>", "<adjective_feeling2>","<animal>", "<verb2>", "<color>", "<verb_ending_in_ing>", "<adverb_ending_in_ly>", "<number>", "<measure_of_time>", "<color>", "<animal2>", "<number2>", "<silly_word>", "<noun2>"]
        user_inputs = {}
            
        for x in objects:
            user_inputs[x] = input("Enter a " + x + ": ")
            
        for objects, value in user_inputs.items():
            story2 = story2.replace(objects, value)
                
        print(story2)

print("Hello, we are going to play a game.")
a = input("Are you ready? (yes/no): ")

if  a.lower() == "yes" :
    b = input("Now you have to choose a template(1, 2 or type r(for random choice)): " )
    if b == "1":
        story_1()
       
    elif b == "2":
        story_2()

    elif b == "r":
       b = random.randint(1,2)
       if b == 1:
            story_1()
       else:
            story_2()
           
    else:
        print("Template doesn't exist.")
        
         
elif a.lower() == "no" :
    print("Game ended.")
else:
    print("Wrong answer.")

