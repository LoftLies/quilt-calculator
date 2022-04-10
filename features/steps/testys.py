from behave import Given, When, Then
from main import incrementor

@Given("an incrementor exists with size '{stride}'")
def given_incrementor(context, stride: int):
    context.incrementor = incrementor(int(stride))

@When("the user increments with '{num}'")
def when_incrementor(context, num: str):
    context.results = context.incrementor(int(num))

@Then("the result after incrementing is '{results}'")
def then_incrementor(context, results: str):
    assert(context.results == int(results))