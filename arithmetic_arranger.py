def arithmetic_arranger(problems):
  #limit number of problems to 5
  if len(problems) > 5:
    return "Error: Too many problems"

  #create empty variables to fill later
  line1 = line2 = line3 = line4 = ""
  
  #split up the problem
  for problem in problems:
      try:
          [operand1, operator, operand2] = problem.split()
      except ValueError:
        return "Error: Malformed problem"

      #check that operator is add or subtract
      if operator not in "+-":
        return "Error: Operator must be '+' or '-'."

      #check submission for digits
      if not operand1.isdigit() or not operand2.isdigit(): 
        return "Error: Numbers must only contain digits."

      #check that digits submitted are 4 or less
      if len(operand1) > 4 or len(operand2) > 4:
        return "Error: Numbers cannot be more than four digits."

      #calculate the answer
      if operator in "+":
        answer = str(int(operand1) + int(operand2))
      elif operator in "-":
        answer = str(int(operand1) - int(operand2))
      else:
        return "Error: unknown operator"

      #create the lines for the formatting
      width = max(len(operand1), len(operand2))
      line1 += "  " + " " * (width - len(operand1)) + operand1 + "    "
      line2 += operator + " " + " " * (width - len(operand2)) + operand2 + "    "
      line3 += "-" * (width + 2) + "    "
      line4 += " " * ((width + 2) - len(answer)) + answer + "    "

  arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()

  return arranged_problems