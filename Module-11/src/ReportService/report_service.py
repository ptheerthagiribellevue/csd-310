"""
This class provides functionality for retrieving data from the WilsonFinancialDB database.
"""
from ReportService.report_sql_queries import ReportSqlQueries
from DBService.db_service import DBService

class ReportService:
    def __init__(self):
        """
        Initializes the ReportService class.
        """
        # Create instances of query and database services
        self.queries = ReportSqlQueries();
        self.dbService = DBService();

    def GetAllData(self):
        """
        A method for getting all data from the database
        """
        # Connect to the wilsonFinancial database
        wilsonFinancialDB = self.dbService.connect_to_database();

        # Queries & Gets all - Client data
        print_results("Displaying Client data", self.dbService, wilsonFinancialDB, self.queries.GetAllClientData)

        # Queries & Gets all - Asset data
        print_results("Displaying Asset data", self.dbService, wilsonFinancialDB, self.queries.GetAllAssetData)
        
        # Queries & Gets all - Transaction data
        print_results("Displaying Transaction data", self.dbService, wilsonFinancialDB, self.queries.GetAllTransactionData)

        # Queries & Gets all - Department data
        print_results("Displaying Department data", self.dbService, wilsonFinancialDB, self.queries.GetAllDepartmentData)

        # Queries & Gets all - Employee data
        print_results("Displaying Employee data", self.dbService, wilsonFinancialDB, self.queries.GetAllEmployeeData)

        # Queries & Gets all - ComplianceRegulation data
        print_results("Displaying ComplianceRegulation data", self.dbService, wilsonFinancialDB, self.queries.GetAllComplianceRegulationData)

        # Queries & Gets all - ComplianceManager data
        print_results("Displaying ComplianceRegulation data", self.dbService, wilsonFinancialDB, self.queries.GetAllComplianceManagerData)
        
        # Close connection
        self.dbService.close_database(wilsonFinancialDB)
    
    def GetClientsAddedMonthlyLastSixMonths(self):
        """
        Display number of clients added for the past 6 months, show this monthly.
        """
        # Connect to the wilsonFinancial database
        wilsonFinancialDB = self.dbService.connect_to_database();
        msg = "Clients added monthly basis for the last 6 months."

        # Queries & Gets all - ComplianceManager data
        print_results(msg, self.dbService, wilsonFinancialDB, self.queries.GetClientsAddedMonthlyLastSixMonths)

        # Close connection
        self.dbService.close_database(wilsonFinancialDB)

    def GetAverageAmountOfAssetsForEntireClientList(self):
        """
        Display the number of clients added for the past 6 months, show this monthly.
        """
        # Connect to the wilsonFinancial database
        wilsonFinancialDB = self.dbService.connect_to_database();
        msg = "Average amount of assets for the entire client list."

        # Queries & Gets all - ComplianceManager data
        print_results(msg, self.dbService, wilsonFinancialDB, self.queries.GetAverageAmountOfAssetsForEntireClientList)

        # Close connection
        self.dbService.close_database(wilsonFinancialDB)

    def GetClientWithMoreThanTenTransactions(self):
        """
        Display the clients with more than 10 transactions.
        """
        # Connect to the wilsonFinancial database
        wilsonFinancialDB = self.dbService.connect_to_database();
        msg = "Client with more than 10 transactions."

        # Queries & Gets all - ComplianceManager data
        print_results(msg, self.dbService, wilsonFinancialDB, self.queries.GetClientWithMoreThanTenTransactions)

        # Close connection
        self.dbService.close_database(wilsonFinancialDB)

# Function to print query results
def print_results(heading, dbService, wilsonFinancialDB, query):
    print("--- {} ---".format(heading))
    columnHeaders, queryResults = dbService.get_query_results(wilsonFinancialDB, query);
    for result in queryResults:
        print("\n".join(["{}: {}".format(columnHeaders[i], result[i]) for i in range(len(columnHeaders))]))
        print("\n")
    input("Press Enter to continue...")

