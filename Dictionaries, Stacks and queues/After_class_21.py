import json

print("Date", " " * 10, "Buying Rate", " " * 5, "Selling Rate")
print("=" * 46)

with open("euro.json;") as file:
    
    euro = json.load(file)
    
    for rates in euro:
        
        print(rates[effectiveDate])
        
        for rates in euro:
            
            print(rates[bid])
            
            for rates in euro:
                
                print(rates[ask])
              
              