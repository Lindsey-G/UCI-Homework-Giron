Sub TestingTicker():
    
    For Each ws In Worksheets
    
    'Insert Headers
    ws.Cells(1, 9).Value = "Ticker"
    ws.Cells(1, 10).Value = "Yearly Change"
    ws.Cells(1, 11).Value = "Yearly Percent Change"
    ws.Cells(1, 12).Value = "Yearly Stock Volume Total"
    
 '-----------------------------------------------------------------
    'Variables
    
        'Set Ticker_Total as String
        Dim Ticker_Total As String
        
        Dim Open_Year_Amount As Double
        Open_Year_Amount = 0
        
        Dim Close_Year_Amount As Double
        Close_Year_Amount = 0
        
        'Set Closining Change Total variable as Double
        Dim Yearly_Change_Total As Double
        Yearly_Change_Total = 0
        
        Dim Yearly_Percent_Change As Double
        Yearly_Percent_Change = 0
        
        Dim Stock_Volume_Total As Double
        Stock_Volume_Total = 0
    
        'Set integer for table
        Dim Summary_Table_Row As Integer
        Summary_Table_Row = 2
        
'-----------------------------------------------------------------------
        
        LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row

        For i = 2 To LastRow
            
            'Check to see if we are in the same Ticker
            If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
            
            'Set Ticker
            Ticker = ws.Cells(i, 1).Value
            
            'Collect Ticker Total
            Ticker_Total = Ticker_Total + ws.Cells(i, 1).Value
            
            Open_Year_Amount = ws.Cells(i, 3).Value
                        
            Open_Year_Total = Open_Year_Total + Open_Year_Amount
            
            Close_Year_Amount = ws.Cells(i, 6).Value
            
            Close_Year_Total = Close_Year_Total + Close_Year_Amount
            
            'Set Yearly Change
            Yearly_Change_Total = (Open_Year_Total - Close_Year_Total)
            
            Yearly_Percent_Change = ((Close_Year_Total - Open_Year_Total) / Open_Year_Total)
            
            Stock_Volume = ws.Cells(i, 7).Value
            
            Stock_Volume_Total = Stock_Volume_Total + Stock_Volume
            
            '--------------------------------------------------------------
            
            'Print Ticker on summary table
            ws.Range("I" & Summary_Table_Row).Value = Ticker
            
            'Print Yearly change on summary table
            ws.Range("J" & Summary_Table_Row).Value = Yearly_Change_Total
            
            ws.Range("K" & Summary_Table_Row).Value = Yearly_Percent_Change
            
            ws.Range("L" & Summary_Table_Row).Value = Stock_Volume_Total
            
            Summary_Table_Row = Summary_Table_Row + 1
            
            '----------------------------------------------------------------
            
            'Reset Ticker Total
            Ticker_Total = " "
            Yearly_Change_Total = 0
            Yearly_Percent_Change = 0
            Stock_Volume_Total = 0
            
            Else
            
            Ticker = Ticker + ws.Cells(i, 1).Value
            Yearly_Change_Total = Yearly_Change_Total + (Open_Year_Total - Close_Year_Total)
            Yearly_Percent_Change = Yearly_Percent_Change + ((Close_Year_Total - Open_Year_Total) / Open_Year_Total)
            Stock_Volume_Total = Stock_Volume_Total + ws.Cells(i, 7).Value
            End If
            
        Next i
        
    Next ws
    
End Sub
















































Sub Multiple_Year_Stock_Data():

	'Set Worksheet variable as Long
	Dim Worksheet As Long 

	'Set i variable as Long
	Dim i As Long

	'Set Ticker variable as String
	Dim Ticker As String

	'Set Ticker Total variable as String
	Dim Ticker_Total As String

	'Set Open Year Amount variable as Double
	Dim Open_Year_Amount As Double
	Open_Year_Amount = 0

	'Set Open Year Amount Total variable as Double
	Dim Open_Year_Total As Double
	Open_Year_Total = 0

	'Set Close Year Amount variable as Double
	Dim Close_Year_Amount As Double
	Close_Year_Amount = 0 

	'Set Close Year Total variable as Double
	Dim Close_Year_Total As Double
	Close_Year_Total = 0

	'Set Ticker's Yearly Change variable as Double
	Dim Yearly_Change_Total As Double
	Yearly_Change_Total = 0 

	'Set Ticker's Yearly Percent Change variable as Double
	Dim Yearly_Percent_Change As Double
	Yearly_Percent_Change = 0

	'Set Ticker's Yearly Percent Change Total variable as Double
	Dim Yearly_Percent_Change_Total As Double
	Yearly_Percent_Change_Total = 0 

	'Set Stock Volune variable As Double
	Dim Stock_Volume As Double
	Stock_Volume = 0

	'Set Stock Volume Total variable As Double
	Dim Stock_Volume_Total As Double
	Stock_Volume_Total = 0 

	'Set Summary Table Row Variable as Integer
	Dim Summary_Table_Row As Integer
	Summary_Table_Row = 2

	'Set LastRow variable as Long
	Dim LastRow As Long

	LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row

'-----------------------------------------------------'
		for i = 2 To LastRow

			'Check to see if we are in the same Ticker
			If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then

			'Identiy what Ticker we in
			Ticker = ws.Cells(i, 1).Value

			'Set the total for Ticker for the next Step
			Ticker_Total = Ticker_Total + ws.Cells(i, 1).Value

			'Identify Open Year Amounts
			Open_Year_Amount = ws.Cells(i, 3).Value

			'Calculate Open Year Total for set Ticker above
			Open_Year_Total = Open_Year_Total + ws.Cells(i, 3).Value

			'Identify Close Year Amounts for set Ticker above
			Close_Year_Amount = ws.Cells(i, 6).Value

			'Calculate Close Year Total for set Ticker above
			Close_Year_Total = Close_Year_Total + ws.Cells(i, 6).Value

			'Calculate Yearly Change for set Ticker above
			Yearly_Change_Total = Yearly_Change_Total + (Open_Year_Total - Close_Year_Total)

			'Calculate Yearly Percent Change for set Ticker above
			Yearly_Percent_Change = ((ws.Cells(i, 6).Value - ws.Cells(i, 3).Value) / ws.Cells(i, 3).Value)

			'Identify Stock Volume amounts for set Ticker above
			Stock_Volume = ws.Cells(i, 7).Value

			'Collect Stock Volume Ticker for set Ticker above
			Stock_Volume_Total = Stock_Volume_Total + ws.Cells(i, 7).Value

			'--------------------------------------------------------------------'
			
			'Print data that has been collected

			'Print Ticker
			ws.Range("I" & Summary_Table_Row).Value = Ticker

			'Print yearly change total from open to close amounts for set Ticker above
			ws.Range("J" & Summary_Table_Row).Value = Yearly_Change_Total

			'Print yearly percent change from open to close amounts for set Ticker above
			ws.Range("K" & Summary_Table_Row).Value = Yearly_Percent_Change_Total

			'Print stock volume total for set Ticker above
			ws.Range("L" & Summary_Table_Row).Value = Stock_Volume_Total

			Summary_Table_Row = Summary_Table_Row + 1

			'-------------------------------------------------------------------------------------------'

			'Reset 
			Ticker_Total = 0
			Yearly_Change_Total = 0
			Yearly_Percent_Change_Total = 0
			Stock_Volume_Total = 0

			Else

			Ticker_Total = Ticker_Total + ws.Cells(i, 1).Value
			Yearly_Change_Total = Yearly_Change_Total + (ws.Cells(i, 3).Value - ws.Cells(i, 6).Value )
			Yearly_Percent_Change_Total = Yearly_Percent_Change_Total + ((ws.Cells(i, 6).Value - ws.Cells(i, 3).Value) / ws.Cells(i, 3).Value)
			Stock_Volume_Total = Stock_Volume_Total + ws.Cells(i, 7).Value

			End If
		Next i
	End Sub