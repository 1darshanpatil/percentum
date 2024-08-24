# sand.py

"""
MIT License

Copyright (c) 2024 Darshan P.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This script calculates the percentage of the current day that has elapsed and 
displays it as a progress bar in the console.
"""


from datetime import datetime, timedelta
from time import sleep
import sys

def calculate_percentage_used():
    """
    Calculate the percentage of the current day that has elapsed.

    Returns:
        float: The percentage of the day that has been used, based on the current time.
    """
    current_time = datetime.now().time()
    start_of_day = datetime.strptime('00:00:00', '%H:%M:%S').time()
    time_used_seconds = (datetime.combine(datetime.today(), current_time) - 
                         datetime.combine(datetime.today(), start_of_day)).total_seconds()
    total_seconds_in_a_day = 24 * 60 * 60
    percentage_used = (time_used_seconds / total_seconds_in_a_day) * 100
    return percentage_used

def print_progress_bar(percentage):
    """
    Print a progress bar indicating the percentage of the day that has elapsed.

    Parameters:
        percentage (float): The percentage of the day that has elapsed.
    """
    bar_length = 50
    filled_length = int(bar_length * percentage / 100)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f'Time Used: |{bar}| {percentage:.2f}%', end='\r', flush=True)

def start():
    """
    Continuously update and display the progress bar for the day's progression
    until interrupted by the user.
    """
    try:
        while True:
            percentage_used = calculate_percentage_used()
            print_progress_bar(percentage_used)
            sleep(5)

    except KeyboardInterrupt:
        print(f'\n{percentage_used:.2f}%')
        print("Keyboard interrupt received. Saying goodbye...")
        print("Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    """
    Execute the start function to continuously display the time progression
    of the current day.
    """
    start()
