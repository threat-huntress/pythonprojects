email = input("Enter your email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"Your user name is '{username}' and you rdomain is '{domain_name}'")
print(format_)