myJob = "Janitor"
print(f"I work as a {myJob}")
globals()["myJob"] = "CEO"
print(f"I got a promotion! I now work as a {myJob}")