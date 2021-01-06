# Byte encoding 


A client we are working with encoded data in bytes.  

Use this code to extract information about sensors measurements  
encoded in repeated sequences of 8 bytes.  

`[timestamp [8bytes] , measurement [8bytes] ]*`

## References 

Convert float to datetime:  
https://stackoverflow.com/questions/6706231/fetching-datetime-from-float-in-python

Convert bytes to Double:  
https://stackoverflow.com/questions/20530678/how-can-i-convert-a-byte-array-to-a-double-in-python

Read file from archive without extracting first  
https://stackoverflow.com/questions/19371860/python-open-file-in-zip-without-temporarily-extracting-it