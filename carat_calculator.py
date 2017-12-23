# Used source: https://owlcation.com/misc/Understanding-Gold-Purity

# Used naming convention for variables:
# Suffix:
#   _g := calculated in gram
#   _c := calculated in carat
#   _p := calculated in percentage

def c2p(k):
    """Converts carat to percentage"""
    return 4.45 + 4.15 * (k-1)

def p2c(p):
    """Converts percentage to carat"""
    return (p - 4.45) / 4.15 + 1

def is_correct(answer):
    """Check if input is a correct answer"""
    return answer == "yes" or \
           answer == "no" or \
           answer == "y" or \
           answer == "n"


if __name__ == "__main__":
    n_decimals = 4
    # Forging all the alloys together
    gold_in_alloy_g = 0
    alloy_g = 0
    answer = "yes"
    while answer != "no" and answer != "n":

        gold_alloy_g = float(raw_input("How many gram gold do you have? "))
        gold_alloy_c = float(raw_input("What carat does it have? "))

        gold_in_alloy_g += (c2p(gold_alloy_c) / 100) * gold_alloy_g
        alloy_g += gold_alloy_g

        answer = "not_correct"
        while is_correct(answer) == False:
            answer = raw_input("Do you still have gold that you want to forge? [y,n] ")

        print("")

    # Calculating the percentage of gold in the alloy
    gold_in_alloy_p = (gold_in_alloy_g / alloy_g) * 100
    gold_in_alloy_c = p2c(gold_in_alloy_p)

    print("You have " + str(gold_in_alloy_g) + "g gold in " + str(alloy_g) \
          + "g alloy.\n" + "The current forged alloy is " \
          + str(gold_in_alloy_c) + " carat.\n")
    output_alloy_c = float(raw_input("What carat do you want to have for the resulting alloy? "))

    # Calculate gram of new alloy for given carat
    output_alloy_p = c2p(output_alloy_c)
    output_alloy_g = gold_in_alloy_g / (output_alloy_p/100)

    # Rounding to desired decimal precision
    output_alloy_g = round(output_alloy_g, n_decimals)
    gold_in_alloy_g = round(gold_in_alloy_g, n_decimals)

    # Print final alloy
    print("\nFinal alloy (gold/total): " \
          + str(gold_in_alloy_g) + '/' + str(output_alloy_g) + ' gram, ' +
          str(output_alloy_c) + " carat.")

