from behave import Given, When, Then
from main import CountColors
from os.path import exists

@Given("an image is available for testing with {number_of_colors} colors")
def an_image_is_available_for_testing_with_colors(context, number_of_colors):
    created_filepath = "features/steps/color-recognition-examples/" + str(number_of_colors)+".png"
    context.image_to_use = created_filepath
    file_exists = exists(context.image_to_use)
    assert file_exists, "No file with name " + context.image_to_use+ " was found to test with"

@When("the user has the number of colors analyzed")
def the_user_has_the_number_of_colors_analyzed(context):
    context.result_of_analysis = CountColors(context.image_to_use)

@Then("the image contains {number_of_colors} colors")
def then_the_image_contains(context, number_of_colors: int):
    expectation = int(number_of_colors)

    assert expectation == context.result_of_analysis, "Colors found {}, colors expected {}".format(expectation, context.result_of_analysis)