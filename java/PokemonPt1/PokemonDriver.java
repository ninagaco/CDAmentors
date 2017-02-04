import java.util.ArrayList;
import java.util.Scanner;

/**
 * Created by GbearTheGenius on 2/4/17.
 */
public class PokemonDriver {

    public static void main(String[] args) {

        ///list of all the Pokemon
        ArrayList<Pokemon> pokemon = new ArrayList<>();

        Scanner in = new Scanner(System.in);
        String input = in.nextLine();


        //if user types in exit, the program exits.
        while(!input.equalsIgnoreCase("exit")) {

            String[] ins = input.split(" ");
            if(ins[0].equals("create")) {
                //create a new Pokemon
                //add it to the ArrayList with pokemon.add();
                System.out.println("create is not implemented");
                //format of Command: create pokemonName pokemonType attack defense

            }
            else if(ins[0].equals("battle")) {
                //check that the Pokemon Exist
                //Have them battle
                System.out.println("battle is not implemented");
                //format of Command: battle pokemonName pokemonName

            }
            else if(ins[0].equals("list")) {
                //print out all the Pokemon and their data from ArrayList
                System.out.println("list is not implemented");
                //format of Command: list
            }


            System.out.print("What do you want to do?: ");
            input = in.nextLine();

        }
    }

}
