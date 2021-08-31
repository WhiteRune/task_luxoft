# Task:
# inside MyClass class, create method visible
# for everyone that takes array change every NONE with number before, all strings should be deleted
# the first appearance of None should be changed with the last appearance of number in the array
import sys  # imported for raise exceptions

my_arr = []


class MyClass:
    @staticmethod
    def visible():
        """
        Method for removing strings and replacing None values
        """
        # declare three variables, counter for iterations, temp for receive last number in list.
        # Receiving last number allows me in next cycle replace first none values with it.
        # none_counter is needed for check is None values in the list, if not we don't use second cycle
        counter = 0
        none_counter = 0
        temp = None

        # Here we check is list empty or not
        if not my_arr:
            sys.exit('List might be filled with strings, numbers, and None values.')

        # There we remove strings and check for save only None values and numbers
        while counter <= len(my_arr) - 1:
            if my_arr[counter] is None:
                counter += 1
                none_counter += 1
            elif isinstance(my_arr[counter], str):
                my_arr.pop(counter)
            elif isinstance(my_arr[counter], int or float):
                temp = my_arr[counter]
                counter += 1
            else:
                sys.exit('List may include only strings, numbers, and None values.')

        # Check is any numbers in list
        if temp is None:
            sys.exit('List may include numbers.')

        # Check is any None values in the list
        if none_counter == 0:
            pass
        else:
            # Replacing None values to numbers according to task
            for i in range(len(my_arr) - 1):
                if my_arr[i] is None:
                    my_arr[i] = temp
                else:
                    temp = my_arr[i]
        print(my_arr)


MyClass.visible()
