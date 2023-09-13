
def userRegistered(post_data_dict, connection) -> bool:
    
    cursor = connection.cursor()
    
    try:
        cursor.execute("INSERT INTO username VALUES ('%s', '%s', '%s');" % (post_data_dict["login"], post_data_dict["password"], post_data_dict["email"]))
        connection.commit()
    except:
        return False

    return True
