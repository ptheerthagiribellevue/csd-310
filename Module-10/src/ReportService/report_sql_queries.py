
"""
This class contains SQL queries for retrieving data from the tables in the WilsonFinancialDB database.
"""
class ReportSqlQueries:

    # SQL query to get all data from the Client table
    GetAllClientData = 'SELECT * FROM Clients'

    # SQL query to get all data from the Asset table
    GetAllAssetData = 'SELECT * FROM Assets'

    # SQL query to get all data from the Transaction table
    GetAllTransactionData = 'SELECT * FROM Transactions'

    # SQL query to get all data from the Department table
    GetAllDepartmentData = 'SELECT * FROM Department'

    # SQL query to get all data from the Employee table
    GetAllEmployeeData = 'SELECT * FROM Employees'

    # SQL query to get all data from the ComplianceRegulation table
    GetAllComplianceRegulationData = 'SELECT * FROM ComplianceRegulation'

    # SQL query to get all data from the ComplianceManager table
    GetAllComplianceManagerData = 'SELECT * FROM ComplianceManager'