class Pokemon(object):

    def __init__(self, name, type, data):

        #the name will store the Pokemon Name
        self.name = name;

        #type will store the pokemon type
        self.type = type;

        #the data array has all the stats of the Pokemon
        self.stats = data;

        #set the level to one
        #set the experience to 0
        #(optional) add other traits/data about your Pokemon

    def battle(self, enemy):
        print("Let the Battle Begin!")
        winner = None;

        #while winner is equal to None
            #Calculate the HP lose for each Pokemon
            #Make your own math operations for this!
            #if a Pokemon has 0 HP
                #Print a message saying it Fainted
                #set winner equal to the other Pokemon


###################################################################
###################################################################
###################################################################
###################################################################


#setup the Pokemon list
pokemonlist = [];

#this is the loop that will take user input
inpu = str(input("What do you want to do?"));
while(inpu.lower() != "exit"):

    segments = inpu.split(" ");
    if(segments[0].lower() == 'create'):
        #create new Pokemon
        # add it to the list
        print("Implement the create command");
        # format of Command: create pokemonName pokemonType attack defense
        # ^^check if the input from the use is correct format above



    elif (segments[0].lower() == 'battle'):
        # create new Pokemon
        # add it to the list
        print("Implement the battle command");

        #format of Command: battle pokemonName pokemonName
        #^^check if the input from the use is correct format above



    elif (segments[0].lower() == 'list'):
        # create new Pokemon
        # add it to the list
        print("Implement the list command");

        # format of Command: list
        # ^^check if the input from the use is correct format above

    inpu = input("What do you want to do?");













