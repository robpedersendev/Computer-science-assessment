def uncover_spy(n, trust):
    # The spy, if it exists:
    #     Does not trust anyone else.
    #     Is trusted by everyone else (he's good at his job).
    #     Works alone; there are no other spies in the city-state.
    
    #  Create the trusted and not trusted containers
    trusted = {}
    not_trusted = set() # Since the spy value is unique uniqe
    # Declare a -1 for spy to account for the case in which there is no spy
    spy = -1
    
    # loop over the values in trust
    for i in range(len(trust)):
        # Add every first index value to the not trusted set 
        # A set is a collection of items that is unordered and does not allow duplicates. 
        not_trusted.add(trust[i][0])
        # Check if the 1th index of the trust list at `i` index is in the trusted dictionary
        if trust[i][1] in trusted:
            # If it is, increment the 1th value in the dictionary. Increasing each time it is located in the trusted list
            # print(trusted[trust[i][1]], trust[i])
            trusted[trust[i][1]] += 1
            # print( trusted[trust[i][1]], trust[i])
        else:
            # If it is, Add the to dictionary
            trusted[trust[i][1]] = 1
    # Loop through all of the items in the trusted dictionary
    # Python dictionary method items() returns a list of dict's (key, value) tuple pairs
    for key, value in trusted.items():
        print("trusted", trusted, "key", key, "value", value, "n", n)
        if value == n-1:
            
            spy = key
            
    # Loop through the not_trusted set
    for val in not_trusted:
        # If the spy value isn't in not_trusted 
        if spy not in not_trusted:
            # Return the spy value
            return spy
    return -1



# Time complexity: O(n)
# Space complexity: O(n)

        
        
        