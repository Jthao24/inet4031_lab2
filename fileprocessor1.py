#!/usr/bin/env python3

f = open("fileprocessor.input","r")

print("Printing out User Data:\n")

for x in f:
  y = x.split(":")
  user = y[0]
  password = y[1]
  userid = y[2]
  groupid = y[3]
  if user[0] == "#":
    print("User4 is skipped because it starts with a hashtag (is commented out)")
  else:
    print(f"The user {user} has a password of {password} and has userid {userid} and groupid {groupid}")
print("\nEnd of User Data")
