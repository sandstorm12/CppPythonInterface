from module import Person


if __name__ == "__main__":
    person = Person("Andy", 16)

    print("Initial name: ", person.get_name())
    print("Initial age : ", person.get_age())

    person.set_name("Moral")
    person.set_age(25)

    print("Modified name: ", person.get_name())
    print("Modified age : ", person.get_age())
