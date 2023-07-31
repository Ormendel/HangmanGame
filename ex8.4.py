def print_hangman(num_of_tries):
    HANGMAN_PHOTOS = {1:"""
            x-------x
            |
            |
            |
            |
            |
""", 2:"""
                    x-------x
                    |       |
                    |       0
                    |
                    |
                    |
        """, 3:"""
                        x-------x
                        |       |
                        |       0
                        |       |
                        |
                        |
            """, 4:"""
                            x-------x
                            |       |
                            |       0
                            |      /|\\
                            |
                            |
                """, 5:"""
                            x-------x
                            |       |
                            |       0
                            |      /|\\
                            |      /
                            |
                """, 6:"""
                            x-------x
                            |       |
                            |       0
                            |      /|\\
                            |      / \\
                            |
                """}

    print(HANGMAN_PHOTOS[num_of_tries])

if __name__ == "__main__":
    print_hangman(1)