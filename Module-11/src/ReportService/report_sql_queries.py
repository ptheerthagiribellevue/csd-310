
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

    # SQL query to get the number of clients added for the past 6 months, show this monthly.
    GetClientsAddedMonthlyLastSixMonths = """
    Select 
        YEAR(c.account_open_date) Year, 
        DATE_FORMAT(c.account_open_date, '%M') Month, 
        count(c.client_id) as 'New client count'  
    from Clients c
    where c.account_open_date > DATE_SUB(now(), INTERVAL 6 MONTH)
    GROUP BY DATE_FORMAT(c.account_open_date, '%M'), MONTH(c.account_open_date), YEAR(c.account_open_date)
    order by YEAR(c.account_open_date), MONTH(c.account_open_date) asc
    """
    #Get average amount of assets (in currency) for the entire client list
    GetAverageAmountOfAssetsForEntireClientList = """
    Select 
        count(*) as 'Total Clients', 
        CONCAT('$', FORMAT(avg(temp.clientTotal), 2)) as 'Average Assets',
        CONCAT('$', FORMAT(sum(temp.clientTotal), 2)) as 'Total Assets'
    from
    (Select a.client_id, sum(a.asset_value) as clientTotal from assets a group by a.client_id) as temp
    """

    #Get clients who has a high number (more than 10 a month) of transactions
    GetClientWithMoreThanTenTransactions = """
    Select 
        YEAR(t.transaction_date) as Year, 
        DATE_FORMAT(t.transaction_date, '%M') as Month,
        c.client_id as 'Client Id',
        c.client_first_name as 'First Name',
        c.client_last_name as 'Last Name',
        count(t.transaction_id) as 'Transaction Count'
    from Transactions t
    inner join assets a on a.asset_id = t.asset_id
    inner join clients c on c.client_id = a.client_id
    GROUP BY DATE_FORMAT(t.transaction_date, '%M'), Month(t.transaction_date), YEAR(t.transaction_date), (c.client_id)
    having count(t.transaction_id) > 10 
    order by Year, Month(t.transaction_date) desc
    """
