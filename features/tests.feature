Feature: Incrementor
    As a quilter
    I want to upload images
    In order to analyse them

    Scenario: I can increase the number
        Given an incrementor exists with size '5'
        When the user increments with '10'
        Then the result after incrementing is '15'

    Scenario: I can decrease the number
        Given an incrementor exists with size '-2'
        When the user increments with '20'
        Then the result after incrementing is '18'

    Scenario: I can do nothing with a number
        Given an incrementor exists with size '0'
        When the user increments with '15'
        Then the result after incrementing is '15'
