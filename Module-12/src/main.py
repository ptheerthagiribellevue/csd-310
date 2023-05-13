
"""
Group: Group3
Members: Loren Alwarez-Mejias & Praveen Theerthagiri 
Assignment: Wilson Financial case study - Assignment 9, 10 
Date: 05/02/2023

This script showcases how the ReportService classes can be utilized to 
create a report that contains all the sample data available in the database for Wilson Financial case study.
"""
import os
from ReportService.report_service import ReportService

def main():
    """
    The main entry point of the script.
    """
    # Clear the terminal screen
    os.system('cls' if os.name =='nt' else 'clear')

    try:
        # Generate a report of all the data
        report_service = ReportService()
        report_service.GetClientsAddedMonthlyLastSixMonths()
        report_service.GetAverageAmountOfAssetsForEntireClientList()
        report_service.GetClientWithMoreThanTenTransactions()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()