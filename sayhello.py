def sayhello(name, school = "CSNHS"):
    print("Hello, {} from {}." .format(name, school))

sayhello("Glenn")
sayhello("Dave", "CSNHS")
sayhello(name="Dave" , school="CSNHS")