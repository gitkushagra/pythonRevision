bidders = {}
amounts = []
bidding_finished = "no"


while bidding_finished == "no":
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ")
    bid_price = int(input("What is your bid?: $"))
    bidders[bid_price] = name
    amounts.append(bid_price)
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no": 
        bidding_finished = "yes"
        highest_bid = max(amounts)
        winner = bidders[highest_bid]
        print(f"The winner is {winner} with a bid of ${highest_bid}")
    elif should_continue == "yes":
        print("\n" * 100)
    else:
        print("Invalid input! Please type 'yes' or 'no'. Program Finished!")
        break

        
