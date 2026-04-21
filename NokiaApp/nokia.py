print("""
1. Phone book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM services
""")

    menu = int(input("Pick an option between 1 - 13: "))

    match menu:

        case 1:
            print("Phone book")
            print("""
1. Search
2. Service Nos.
3. Add name
4. Erase
5. Edit
6. Assign tone
7. Send b’card
8. Options
9. Speed dials
10. Voice tags
""")
            phonebook = int(input("Pick an option: "))

            match phonebook:
                case 1:
                    print("Search")
                case 2:
                    print("Service nos")
                case 3:
                    print("Add name")
                case 4:
                    print("Erase")
                case 5:
                    print("Edit")
                case 6:
                    print("Assign tone")
                case 7:
                    print("Send b’card")
                case 8:
                    print("Options")
                    print("""
1. Type of view
2. Memory status
""")
                    option = int(input("Choose: "))
                    match option:
                        case 1:
                            print("Type of view")
                        case 2:
                            print("Memory status")
                        case _:
                            print("Invalid option")
                case 9:
                    print("Speed dials")
                case 10:
                    print("Voice tags")
                case _:
                    print("Invalid option")

        case 2:
            print("Messages")
            print("""
1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info service
9. Voice mailbox number
10. Service command editor
""")
            messages = int(input("Pick an option: "))

            match messages:
                case 1:
                    print("Write messages")
                case 2:
                    print("Inbox")
                case 3:
                    print("Outbox")
                case 4:
                    print("Picture messages")
                case 5:
                    print("Templates")
                case 6:
                    print("Smileys")
                case 7:
                    print("Message settings")
                    print("""
                                1. Set
                                2. Common
""")
                    message = int(input("Choose: "))

                    match message:
                        case 1:
                            print("""
1. Message centre number
2. Messages sent as
3. Message validity
""")
                            s = int(input("Choose: "))
                            match s:
                                case 1:
                                    print("Message centre number")
                                case 2:
                                    print("Messages sent as")
                                case 3:
                                    print("Message validity")
                                case _:
                                    print("Invalid option")

                        case 2:
                            print("""
1. Delivery reports
2. Reply via same centre
3. Character support
""")
                            choose = int(input("Choose: "))
                            match choose:
                                case 1:
                                    print("Delivery reports")
                                case 2:
                                    print("Reply via same centre")
                                case 3:
                                    print("Character support")
                                case _:
                                    print("Invalid option")

                        case _:
                            print("Invalid option")

                case _:
                    print("Invalid option")

        case 3:
            print("Chat")

        case 4:
            print("Call register")
            print("""
1. Missed calls
2. Received calls
3. Dialled numbers
4. Erase recent call lists
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid credit
""")
            call register = int(input("Pick an option: "))

            match cr:
                case 1:
                    print("Missed calls")
                case 2:
                    print("Received calls")
                case 3:
                    print("Dialled numbers")
                case 4:
                    print("Erase recent calls")

                case 5:
                    print("""
1. Last call duration
2. All calls duration
3. Received calls duration
4. Dialled calls duration
5. Clear timers
""")
                    call dur= int(input("Choose: "))
                    match call dur:
                        case 1:
                            print("Last call duration")
                        case 2:
                            print("All calls duration")
                        case 3:
                            print("Received calls duration")
                        case 4:
                            print("Dialled calls duration")
                        case 5:
                            print("Clear timers")
                        case _:
                            print("Invalid option")

                case 6:
                    print("""
1. Last call cost
2. All calls cost
3. Clear counters
""")
                    cc = int(input("Choose: "))
                    match cc:
                        case 1:
                            print("Last call cost")
                        case 2:
                            print("All calls cost")
                        case 3:
                            print("Clear counters")
                        case _:
                            print("Invalid option")

                case 7:
                    print("""
1. Call cost limit
2. Show costs in
""")
                    cs = int(input("Choose: "))
                    match cs:
                        case 1:
                            print("Call cost limit")
                        case 2:
                            print("Show costs in")
                        case _:
                            print("Invalid option")

                case 8:
                    print("Prepaid credit")

                case _:
                    print("Invalid option")

        case 5:
            print("Tones")

        case 6:
            print("Settings")

        case 7:
            print("Call divert")

        case 8:
            print("Games")

        case 9:
            print("Calculator")

        case 10:
            print("Reminders")

        case 11:
            print("Clock")

        case 12:
            print("Profiles")

        case 13:
            print("SIM services")

        case _:
            print("Invalid option")


# Run program
nokia_app()
