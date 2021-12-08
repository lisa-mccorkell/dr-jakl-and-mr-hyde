-- Farnsworth - MSSQL
SELECT DISTINCT client AS client_name
     , (CASE WHEN url IS NULL THEN '' ELSE url END) AS client_url
     , sfdc_account_id AS account_id
FROM Fulfillment.dbo.client



-- HG360 - MSSQL
SELECT name AS account_name
     , (CASE WHEN website IS NULL THEN '' ELSE website END) AS account_url
     , id AS account_id
     , type AS account_status
FROM HG360.dbo.Account
