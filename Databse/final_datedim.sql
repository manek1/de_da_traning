use company
WITH DateSeries AS (
    -- Generate a date series from '2022-01-01' to '2022-12-31'
    SELECT CAST('2000-01-01' AS DATETIME) AS date_key
    UNION ALL
    SELECT DATEADD(DAY, 1, date_key)
    FROM DateSeries
    WHERE date_key < '2050-12-31' -- Adjust the end date as needed
)
SELECT 
    date_key,
    
    -- Bank Holidays (for simplicity, set as 0, adjust based on a holiday table if needed)
    0 AS Bank_Holiday_CY,
    0 AS Bank_Holiday_UK,
    
    -- CIGNA Month End (End of the month flag)
    CASE 
        WHEN date_key = EOMONTH(date_key, 0) THEN 1
        ELSE 0 
    END AS CIGNA_Month_End,
    
    -- Quarter and Year
    CONCAT('Q', DATEPART(QUARTER, date_key), ' ', YEAR(date_key)) AS cq_and_cy_name,
    'Q' + CAST(DATEPART(QUARTER, date_key) AS VARCHAR) AS cq_name,
    YEAR(date_key) AS cy_name,
    
    date_key AS date_key_REAL,

    -- Day Flags for the Start and End of the Fiscal/Calendar Quarters and Year
    CASE WHEN DATEPART(DAY, date_key) = 1 THEN 1 ELSE 0 END AS day_cq_begin, 
    CASE WHEN date_key = EOMONTH(date_key, 0) THEN 1 ELSE 0 END AS day_cq_end, -- End of Quarter
    CASE WHEN DATEPART(DAYOFYEAR, date_key) = 1 THEN 1 ELSE 0 END AS day_cy_begin, -- Start of Calendar Year
    CASE WHEN date_key = '2050-12-31' THEN 1 ELSE 0 END AS day_cy_end, -- End of Calendar Year
    
    -- Week Information (Calculating Start and End of Week)
    DATEADD(DAY, -DATEPART(WEEKDAY, date_key) + 1, date_key) AS week_monday, -- Monday of the week
    DATEADD(DAY, -DATEPART(WEEKDAY, date_key) + 7, date_key) AS week_sunday, -- Sunday of the week
    DATEPART(WEEK, date_key) AS week_number, -- Week number in the year
    YEAR(date_key) AS week_number_cy, -- Week number in Calendar Year
    DATEPART(QUARTER, date_key) AS week_number_fq, -- Week number in Fiscal Quarter (assumed to be same as Calendar Quarter here)
    YEAR(date_key) AS week_number_fy, -- Week number in Fiscal Year
    
    -- Month and Fiscal Year Information
    FORMAT(date_key, 'MMM-yy') AS month_and_cy_name, -- Month and Calendar Year (e.g., Jan-22)
    FORMAT(date_key, 'MMM-yy') AS month_and_fy_name, -- Month and Fiscal Year (e.g., Jan-22)
    DATENAME(MONTH, date_key) AS month_name, -- Name of the Month
    MONTH(date_key) AS month_number, -- Month Number (e.g., 1 for January)
    
    -- Weekday Information (e.g., Saturday, Sunday)
    DATENAME(WEEKDAY, date_key) AS weekday,
    
    -- Weekend and Working Day Flags
    CASE WHEN DATENAME(WEEKDAY, date_key) IN ('Saturday', 'Sunday') THEN 1 ELSE 0 END AS Weekend_Working_Day_CY, -- Weekend flag
    CASE WHEN DATENAME(WEEKDAY, date_key) IN ('Saturday', 'Sunday') THEN 0 ELSE 1 END AS Working_Day_CY, -- Working Day flag
    
    -- Julian Counter (Days since a base date, e.g., '1900-01-01')
    DATEDIFF(DAY, '1900-01-01', date_key) AS julian_counter
    
FROM DateSeries
OPTION (MAXRECURSION 20000);