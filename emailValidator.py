def validate(input_str):
    valid = False  # Boolean to check if it is a valid email or not 
    if input_str.count("@") == 1:  # Check for exactly one "@"
        mail_recipients = input_str.split("@")

        # Recipient Name Analysis
        recipient_name = mail_recipients[0]  # Part before the "@"
        valid_special_chars = set("0123456789._")

        if 3 <= len(recipient_name) <= 24:
            # Check for invalid special characters at the beginning or end
            if recipient_name[0] not in "._" and recipient_name[-1] not in "._":
                for char in recipient_name:
                    if not (char.isalnum() or char in valid_special_chars):
                        valid = False
                        break  # Stop checking further if an invalid character is found
                else:
                    valid = True  # Only set valid to True if all characters are valid
            else:
                valid = False  # Invalid if special characters are at the beginning or end
        else:
            valid = False  # Invalid length

        # Domain Name Analysis
        if valid:
            domain_parts = mail_recipients[1].split(".")
            if len(domain_parts) > 1:
                domain_name = domain_parts[0]
                valid_special_chars_ = set("0123456789-")
                if 3 <= len(domain_name) <= 12:
                    for char in domain_name:
                        if not (char.isalnum() or char in valid_special_chars_):
                            valid = False
                            break
                    else:
                        valid = True  # Only set valid to True if all characters are valid
                else:
                    valid = False  # Invalid domain name length
            else:
                valid = False  # Invalid domain format (missing dot)

        # Top-Level Domain Name Analysis
        if valid and len(domain_parts) > 1:
            top_level_domain_name = domain_parts[-1]
            valid_names = {"com", "net", "org", "tech"}
            if top_level_domain_name not in valid_names:
                valid = False

    if valid:
        return "Email is valid"
    else:
        return "Email is invalid"

if __name__ == "__main__":
    email = input("Enter email:")
    print("\n" + validate(email))
