name=["joel","aswathy","ganga","radhakrishnan"]
longest_length=0
for ne in name:
    current_length=len(ne)
    if current_length>longest_length:
        longest_length=current_length
print(longest_length)
