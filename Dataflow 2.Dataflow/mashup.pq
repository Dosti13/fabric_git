[StagingDefinition = [Kind = "FastCopy"]]
section Section1;
shared city_safety_seattle = let
  Source = Lakehouse.Contents(null),
  Navigation = Source{[workspaceId = "0c6ed14a-ad74-4f7d-b82e-b1451582e8f6"]}[Data],
  #"Navigation 1" = Navigation{[lakehouseId = "8c0c9121-64e1-4920-bac7-f032092f74f4"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[Id = "city_safety_seattle", ItemKind = "Table"]}[Data]
in
  #"Navigation 2";
[DataDestinations = {[Definition = [Kind = "Reference", QueryName = "public_holidays_DataDestination", IsNewTarget = true], Settings = [Kind = "Manual", AllowCreation = true, ColumnSettings = [Mappings = {[SourceColumnName = "countryOrRegion", DestinationColumnName = "countryOrRegion"], [SourceColumnName = "holidayName", DestinationColumnName = "holidayName"], [SourceColumnName = "normalizeHolidayName", DestinationColumnName = "normalizeHolidayName"], [SourceColumnName = "isPaidTimeOff", DestinationColumnName = "isPaidTimeOff"], [SourceColumnName = "countryRegionCode", DestinationColumnName = "countryRegionCode"], [SourceColumnName = "date", DestinationColumnName = "date"]}], DynamicSchema = false, UpdateMethod = [Kind = "Replace"], TypeSettings = [Kind = "Table"]]]}]
shared public_holidays = let
  Source = Lakehouse.Contents(null),
  Navigation = Source{[workspaceId = "0c6ed14a-ad74-4f7d-b82e-b1451582e8f6"]}[Data],
  #"Navigation 1" = Navigation{[lakehouseId = "8c0c9121-64e1-4920-bac7-f032092f74f4"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[Id = "public_holidays", ItemKind = "Table"]}[Data]
in
  #"Navigation 2";
shared public_holidays_DataDestination = let
  Pattern = Fabric.Warehouse([CreateNavigationProperties = false, HierarchicalNavigation = true]),
  Navigation_1 = Pattern{[workspaceId = "0c6ed14a-ad74-4f7d-b82e-b1451582e8f6"]}[Data],
  Navigation_2 = Navigation_1{[warehouseId = "5f63d8b8-23d4-47f7-995a-cef6fc7c739d"]}[Data],
  Navigation_3 = Navigation_2{[Schema = "dbo"]}[Data],
  TableNavigation = Navigation_3{[Name = "public_holidays"]}?[Data]?
in
  TableNavigation;
