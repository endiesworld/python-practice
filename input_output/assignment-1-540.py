
"""
SSW 540-A Fundamentals of Software Engineering
Assignment 1
Author: Emmanuel Okoro
Date: 09/17/2024
Description: Sets up Environment – ...prints out your name in response to a query
"""

"""
    Function: welcome_message
    Parameters: None
    Returns: None
    
"""
def welcome_message():
    print("Welcome to SSW 540-A Fundamentals of Software Engineering solution to Assignment 1")
    print("****************************************************************")
    
    

"""
    Function: query_response
    Parameters: None
    Returns: None
    
"""
def query_response():
    user_input = input("Please enter your query: ")
    print("My name: Emmanuel Okoro")
    
    
if __name__ == "__main__":
    welcome_message()
    query_response()