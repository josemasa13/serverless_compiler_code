class Constanttable:
    def __init__(self):
        self.table = []

    
    def insert_constant(self, constant, const_type, vAddress):
        #Check if the constant already exists
        for i in self.table:
            if i['constant'] == constant:
                return i['v_address']

        new_constant = {
            'constant' :    constant,
            'type' :        const_type,
            'v_address' :   vAddress
        }

        self.table.append(new_constant)
        return vAddress

        
    def display_table(self):

        print("Displaying constant table")
        print("Cons \t Type \t Address")
        for i in self.table:
            print(
                str(i["constant"]) + '\t' +
                i["type"] + '\t' +
                str(i["v_address"])
            )