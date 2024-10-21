class Penguin:
    
    def physicalCharacteristics(self, flipper_length, leg_length, num_eyes, has_tail, is_furry):
        self.flipper_length = flipper_length
        self.leg_length = leg.length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry
        
    def describe(self):
        description = f"Penguin Physical Characteristics:\n"
        description += f"Flipper length: {self.flipper_length}\n"
        description += f"Leg length: {self.flipper_length}\n"
        description += f"Number of eyes: {self.num_eyes}\n"
        description += f"Has a tail? {'Yes' if self.has_tail else 'No'}\n"
        description += f"Is it furry? {'Yes' if self.is_furry else 'No'}\n"
        print(description)
        
   
def main():
    # Create an instance of a penguin
    my_penguin = Penguin(flipper_length = 0.4, leg_length = 0.2, num_eyes = 2, has_tail = True, is_furry = False)
        
    # Call the describe method for my penguin
    mypenguin.describe()

# Call the main function
if __name__ == "__main__":
    main()