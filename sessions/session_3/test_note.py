from note import Note

n1 = Note("My first note")
n2 = Note("My first note", "second note tag")

print("Id: ", n1.getId(), " Memo: ", n1.memo, " Created Date: ", n1.creationDate)
print("Id: ", n2.getId(), " Memo: ", n2.memo, " Created Date: ", n2.creationDate)
