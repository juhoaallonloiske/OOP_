from task4class import CellPhone

def main():
    my_phone = CellPhone()

    my_phone.set_manufact()
    my_phone.set_model()
    my_phone.set_retail_price()
    my_phone.set_ID()


    print("Manufacturer:", my_phone.get_manufact(),
          "\nModel number:", my_phone.get_model(),
          "\nRetail price:", my_phone.get_retail_price(),
          "\nID:", my_phone.get_ID())

    print(my_phone)


main()