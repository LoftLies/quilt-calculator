Feature: Recognizing colors
    As a quilter
    I want to get information about the colors in an image
    In order to create a pattern from these colors

    Scenario Outline: Recognize the amount of colors in an image
        #Test images created with https://www.pixilart.com/draw
        Given an image is available for testing with <number_of_colors> colors
        When the user has the number of colors analyzed
        Then the image contains <number_of_colors> colors

        Examples:
            | number_of_colors |
            | 2                |
            | 3                |
            | 4                |
            | 8                |