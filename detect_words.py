def retorno_Palavra(email_texto,typedef):
  #typedef=0 - conteudo
  #typedef=1 - assunto
  phishing_elements = [["Action Required", "Immediate attention required", "Urgent", "Act now", "Your account will be suspended", "Your account will be closed", "Failure to comply", "Security alert", "Warning", "Time-sensitive", "Expires soon", "Last chance", "Critical update", "Compromised account", "Unauthorized activity detected", "Your access will be terminated", "Verify your account immediately", "Official notification", "Security department", "Customer support", "Billing department", "IT support", "Admin", "Service desk", "Compliance", "Legal department", "Invoice", "Payment", "Refund", "Delivery", "Tax", "Government", "Bank", "Credit card", "PayPal", "Amazon", "Netflix", "Microsoft", "Apple", "Transaction failed", "Payment pending", "Unusual activity", "Suspicious login", "Account locked", "Password reset", "Update billing information", "Verify payment details", "Debit/Credit", "Balance", "Overdue", "Invoice attached", "Wire transfer", "Funds", "Limited access", "Frozen account", "Click here", "Verify your account", "Update your information", "Log in to your account", "Confirm your details", "Download attachment", "Review the document", "Unblock your account", "Access your secure message", "Follow this link", "Respond to this email", "Complete the form", "Social Security Number", "Date of birth", "Mother's maiden name", "Credit card number", "Bank account details", "PIN", "Security questions/answers", "Full name", "Address", "Phone number", "Username", "Password", "Dear Customer", "Dear User", "Dear Valued Client", "Sincerely", "Regards", "Thank you", "The Team", "Customer Support", "Account Services", "Security Department", "SSL certificate", "Encryption", "IP address", "Server error", "Data breach", "Firewall", "Malware", "Phishing attempt", "Two-factor authentication", "Protocol", "Domain", "Proxy"],
  ["urgent", "immediate action", "respond now", "last chance", "click here", "confidential", "verify your account", "account problem", "account locked", "password recovery", "win money", "you won", "prize", "exclusive offer", "limited time", "don't miss out", "free", "special discount", "congratulations", "pending balance", "bank transfer", "payment pending", "invoice", "refund", "expired bill", "important notice", "security alert", "confirm your information", "account update", "suspicious login", "account blocked", "bank details", "action required", "see attachment", "important message", "new message", "required response"]]
  x=0
  texto_normalizado = email_texto.lower()
  encontradas = []
  for palavra in phishing_elements[typedef]:
    if palavra.lower() in texto_normalizado:
      encontradas.append(palavra)
      x+=1
  if x>0 and x<=3:
    return 3
  elif x>3 and x<5:
    return 6.5
  elif x>=5:
    return 10
  return 0
