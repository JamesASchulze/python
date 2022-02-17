import re
def arithmetic_arranger(problems, needsAnswers=False):
  
  # Make sure there are not too many problems.
  problems_count = len(problems)
  if problems_count > 5:
    return "Error: Too many problems."
  else:
    f_nums = ''
    operators = ''
    s_nums = ''
    
    top_row = ''
    bottom_row = ''
    dash_row = ''
    answer_row = ''
    arranged_problems = ''

    # Loop through the list of math problems
    i = 0
    while i < problems_count:

      problem_elements = re.split("\s",problems[i])

      f_num     = problem_elements[0]
      operator  = problem_elements[1]
      s_num     = problem_elements[2]

      f_num_len = len(f_num)
      s_num_len = len(s_num)

      f_num_res   = ''
      s_num_res   = ''
      dash_res    = ''
      answer_res  = ''

      # Error Checking
      if re.search("\D",f_num) or re.search("\D",s_num): 
        return "Error: Numbers must only contain digits."

      if not re.search("[+,-]",operator):
        return "Error: Operator must be '+' or '-'."

      if f_num_len > 4 or s_num_len > 4:
        return "Error: Numbers cannot be more than four digits."
      
      # Get the length of spaces needed before each problem
      if f_num_len > s_num_len:
        problem_length = f_num_len + 2
      else:                
        problem_length = s_num_len + 2

      # Formatting - Add spaces to the beginning of 1st number.
      f_num_len_i = f_num_len
      while f_num_len_i < problem_length:
        f_num_res = " " + f_num_res
        f_num_len_i += 1

      # Formatting - Add spaces to the beginning of 2nd number.
      s_num_len_i = s_num_len + 1
      while s_num_len_i < problem_length:
        s_num_res = " " + s_num_res
        s_num_len_i += 1

      # Formatting - Add the dashes underneath each equation.
      dash_len_i = 0
      while dash_len_i < problem_length:
        dash_res = "-" + dash_res
        dash_len_i += 1

      # Formatting - Add four spaces between each equation.
      if i > 0:
        top_row    = top_row    + '    '
        bottom_row = bottom_row + '    '
        dash_row   = dash_row   + '    '
      
      # Build each row
      top_row = top_row + f_num_res + f_num
      bottom_row = bottom_row + operator + s_num_res + s_num
      dash_row = dash_row + dash_res
      
      # Do yous guys want the answers, er no?
      if needsAnswers is False :
        # Get it together
        arranged_problems = '{}\n{}\n{}'.format(top_row,bottom_row,dash_row)
      else:
        # Check your math
        if operator == '+':
          answer = int(f_num) + int(s_num)
        else:
          answer = int(f_num) - int(s_num)
        
        # #LearningFunctionalProgramming
        answer_str = str(answer)

        # Formatting - Add four spaces between each equation.
        if i > 0:
          answer_res = answer_res + '    '

        # Formatting - Add spaces to the beginning of answer.
        answer_len_i = len(answer_str)
        while answer_len_i < problem_length:
          answer_res = ' ' + answer_res
          answer_len_i += 1

        # Build answer row
        answer_row = answer_row + answer_res + answer_str

        # Get it together
        arranged_problems = '{}\n{}\n{}\n{}'.format(top_row,bottom_row,dash_row,answer_row)

      # Add 1 and try the loop again!
      i += 1 

  return arranged_problems