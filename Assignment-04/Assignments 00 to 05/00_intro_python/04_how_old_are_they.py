
def guess_age():

    anton = 21
    message = []
    beth = 0 #6 year than anton
    chen = 0 #20 year older than bath
    drew = 0 #older == chen + anton
    Ethan = 0 # Ethan == chen

    if anton ==21:
        beth = anton +6
        message.append(f"Beth is {beth}")
    if beth == anton +6:
        chen = beth + 20
        message.append(f"Chen is {chen}")
    if chen == beth + 20:
        drew = chen + anton
        message.append(f"Draw is {drew}")
    if drew == chen +anton:
        Ethan = chen
        message.append(f"Ethan is {Ethan}")

    return("\n".join(message))
    
print(guess_age())

