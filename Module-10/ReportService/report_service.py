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
        pass

    def GetAllData(self):
        """
        A method for getting all data from the database
        """
        # Create instances of query and database services
        queries = ReportSqlQueries();
        dbService = DBService();

        # Connect to the wilsonFinancial database
        wilsonFinancialDB = dbService.connect_to_database();

        # Queries & Gets all - Client data
        print_results("Displaying Client data", dbService, wilsonFinancialDB, queries.GetAllClientData)

        # Queries & Gets all - Asset data
        print_results("Displaying Asset data", dbService, wilsonFinancialDB, queries.GetAllAssetData)
        
        # Queries & Gets all - Transaction data
        print_results("Displaying Transaction data", dbService, wilsonFinancialDB, queries.GetAllTransactionData)

        # Queries & Gets all - Department data
        print_results("Displaying Department data", dbService, wilsonFinancialDB, queries.GetAllDepartmentData)

        # Queries & Gets all - Employee data
        print_results("Displaying Employee data", dbService, wilsonFinancialDB, queries.GetAllEmployeeData)

        # Queries & Gets all - ComplianceRegulation data
        print_results("Displaying ComplianceRegulation data", dbService, wilsonFinancialDB, queries.GetAllComplianceRegulationData)

        # Queries & Gets all - ComplianceManager data
        print_results("Displaying ComplianceRegulation data", dbService, wilsonFinancialDB, queries.GetAllComplianceManagerData)
        
        # Close connection
        dbService.close_database(wilsonFinancialDB)

# Function to print query results
def print_results(heading, dbService, wilsonFinancialDB, query):
    print("--- {} ---".format(heading))
    columnHeaders, queryResults = dbService.get_query_results(wilsonFinancialDB, query);
    for result in queryResults:
        print("\n".join(["{}: {}".format(columnHeaders[i], result[i]) for i in range(len(columnHeaders))]))
        print("\n")
    input("Press Enter to continue...")

