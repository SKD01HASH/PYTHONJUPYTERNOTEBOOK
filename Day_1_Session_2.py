{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"Day_1_Session_2.ipynb","provenance":[],"collapsed_sections":["63iHONtXmyYj","sDy7Ik8AsJyQ","NlWRCyOVaOvY","imIPBN1g-XPm"]},"kernelspec":{"name":"python3","display_name":"Python 3.8.3 32-bit"},"interpreter":{"hash":"c44c4cfe05a0f2d911ad786c073734f5a2836356abef7b6ad679499f520cf0ac"},"language_info":{"name":"python","version":"3.8.3"}},"cells":[{"cell_type":"code","metadata":{"id":"KE4Nz75CubNh"},"source":[""],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"U2LImq3YbyVo","outputId":"a6fb30ee-27dc-4bbc-dc4f-994173d64b17"},"source":["age = input('How old are you? ')\n","print ('You are ', age, ' years old.')"],"execution_count":null,"outputs":[{"output_type":"stream","text":["You are  10  years old.\n"],"name":"stdout"}]},{"cell_type":"code","metadata":{"id":"ZH8nPxYd7HM-","outputId":"fc36d838-3876-470e-f3fc-2f5eea1d8bf5"},"source":["\n","name = 'Atul' \n","print('Hey, {}, You are {} years old.'.format(name, age))\n","print('Hey,', name, ', You are', age, 'years old.')"],"execution_count":null,"outputs":[{"output_type":"stream","text":["Hey, AMEY, You are 10 years old.\n","Hey, AMEY , You are 10 years old.\n"],"name":"stdout"}]},{"cell_type":"code","metadata":{"id":"haGC7G2C7oJl","outputId":"4f9d62dc-3979-4611-adfa-e48335ff6beb"},"source":["print('The double of your age ({}) is {}.'.format(age, 2*age))"],"execution_count":null,"outputs":[{"output_type":"stream","text":["The double of your age (10) is 1010.\n"],"name":"stdout"}]},{"cell_type":"code","metadata":{"id":"Vt1F2me6NaV5"},"source":["print( 'In age years, you will be {} years old'.format(age + age))"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"ygKG4iAbqIMI"},"source":["print( 'In 5 years, you will be {} years old'.format(age + 5))"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"HHLRrChGuy4B"},"source":["type(age)"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"DOdg3fd1cgVO"},"source":["name = \"Amey Karkare\"\n","age  = 42\n","print('Hey', name, '. You are', age, 'years old')"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"v0A2S0jJ7XoE"},"source":["print('Hey {}. You are {} years old'.format(name, age))"],"execution_count":null,"outputs":[]},{"cell_type":"markdown","metadata":{"id":"oHtfbayyt6RB"},"source":["##Variables"]},{"cell_type":"code","metadata":{"id":"zSmPNy4FqRpo"},"source":["# declaring and initializing the variables\n","m = 64\n","c = 'Nrti'\n","f = 3.1416"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"6XZdoxbiqiW9"},"source":["# print the value held by f and c\n","print(f)\n","print(c)"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"Hw3vzh3qqmc9"},"source":["# assign new value to the existing variable\n","\n","f = 2.7183\n","print(f)\n","type(f)"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"Zs0_JwS29XZh"},"source":["# You can even change the type \n","f = \"Day 2 of the class day\"\n","print(f)\n","type(f)"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"26R2pCIm_uFl"},"source":["# format works for strings, even outside print\n","day = 2 \n","f = \"The next day is {}\".format(day+1)\n","print(f)"],"execution_count":null,"outputs":[]},{"cell_type":"markdown","metadata":{"id":"qHQjiCHR_94N"},"source":["## Identifiers"]},{"cell_type":"code","metadata":{"id":"JObnwHooquw9"},"source":["# valid variable names\n","i          = 5\n","count      = 0\n","Lab5       = 'python data types'\n","max_profit = 100\n","_left      = False\n","fUnNy      = 5.7\n","mcomment   = \"\"\"This is a doc string.\n","      It can span multiple lines.\n","Like I am spanning 3 lines\"\"\"\n","comment = \"this is not really a comment\"\n","\"\"\" this is not\n","   executed\"\"\"\n","   \n","print(\"i =\", i)\n","print(\"count =\", count)\n","print(\"Lab5 = \", Lab5)\n","print(\"max_profit =\", max_profit)\n","print(\"_left =\", _left)\n","print(\"fUnNy =\", fUnNy)\n","print(\"mcomment = \", mcomment)"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"LRm4cw-tryXp"},"source":["# invalid variable names\n","\n","# 5j = 50\n","# min profit = 10.4\n","# lab.7 = 'data science'"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"D6Kf9XDFsb5v"},"source":["# get a list of keywords in python\n","import keyword #import the package 'keyword'\n","print(keyword.kwlist)"],"execution_count":null,"outputs":[]},{"cell_type":"markdown","metadata":{"id":"HQqRhCNxCm8B"},"source":["### A program that tries to assign to a keyword"]},{"cell_type":"code","metadata":{"id":"Ryf1x1fAs0dy"},"source":["# keywords cannot be used as a variable name. \n","# Note that 'class' is a keyword in python.\n","# class = 6.4\n","clasS = 6.4  # CLASS is NOT a keyword.\n","print(clasS) "],"execution_count":null,"outputs":[]},{"cell_type":"markdown","metadata":{"id":"bEHHKEcmC638"},"source":["### A program that tries to assign to a library function"]},{"cell_type":"code","metadata":{"id":"kRGbpj7qDBvQ"},"source":["print('Hello')\n","saved = print\n","print = 1"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"BlI94DjADPMO"},"source":["print('Bye')"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"dIvcqMzDDd2d"},"source":["print = saved\n","print('Bye')\n","saved('hello' , 'amey')"],"execution_count":null,"outputs":[]},{"cell_type":"markdown","metadata":{"id":"iGETDVD0tu5J"},"source":["##Assignment Statement"]},{"cell_type":"code","metadata":{"id":"QFaZCP1FnyF_"},"source":["# to assign a value to a variable, '=' operator (assignment operator) \n","# can be used.\n","x = 10\n","print(x)"],"execution_count":null,"outputs":[]},{"cell_type":"markdown","metadata":{"id":"1zhRIl229nsS"},"source":["## Multiple Assignment"]},{"cell_type":"code","metadata":{"id":"v0Scbbmwhb7x"},"source":["x, y = 10, 20\n","print(x,y)"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"dOWrP6WghjUa"},"source":["x, y = y+1, x+1\n","print(x, y)"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"7rqlXLf_TmVY"},"source":["print(x,y)\n","x,y = y,x\n","print(x,y)"],"execution_count":null,"outputs":[]},{"cell_type":"markdown","metadata":{"id":"tRU371C6hzfQ"},"source":["##Activity\n","\n","---\n","\n","\n","Swap the contents of two Variables in Python\n"]},{"cell_type":"code","metadata":{"id":"R26RcixRiMhf"},"source":["# Replace '__YOUR_CODE__' so that the below program prints 506, 401. \n","# Do not change any other line.\n","var1 = 401\n","var2 = 506\n","\n","'__YOUR__CODE__'\n","\n","print(var1, var2)"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"4PtZ3_3pUAKu"},"source":["x, y, z, w = 100, 200, 400, 600\n","print(x,y,z,w)\n","x, y, w, y, w = 10, 11, 12, 13\n"],"execution_count":null,"outputs":[]},{"cell_type":"markdown","metadata":{"id":"i66f8xbqE6Kd"},"source":["##Types\n","type() method can be used to see the type of an object passed to it"]},{"cell_type":"code","metadata":{"id":"5ajC_XY9p4QN"},"source":["type(500)"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"nU8Hum87FN4B"},"source":["type(-200)"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"tC_hZjc-FYw3"},"source":["type(2.71832)"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"RWD9wze6FbKZ"},"source":["type(\"Hello\")"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"MqFeMs-lFdn0"},"source":["type('World')"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"Jtq0rHUiFgA-"},"source":["type(3+2+5)"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"PVCoMDb2FkCC"},"source":["type(3>2)"],"execution_count":null,"outputs":[]},{"cell_type":"markdown","metadata":{"id":"3s8TdN8e8I16"},"source":["##Type Cast"]},{"cell_type":"code","metadata":{"id":"rp3nwgjpftQ0","outputId":"9feea9a5-0933-47ff-c06c-bb2322d2fec3"},"source":["age = input('age? ')\n","print('The double of your age is {}'.format(2*age))\n","print(type(age))"],"execution_count":null,"outputs":[{"output_type":"stream","text":["The double of your age is 1010\n","<class 'str'>\n"],"name":"stdout"}]},{"cell_type":"code","metadata":{"id":"2INlV72K9Ehq","outputId":"094cc65a-6180-4486-92d8-0a3d32a4cc00"},"source":["age = input('age? ')\n","print('The double of your age is {}'.format(2*int(age)))\n","type(age)"],"execution_count":null,"outputs":[{"output_type":"stream","text":["The double of your age is 20\n"],"name":"stdout"},{"output_type":"execute_result","data":{"text/plain":["str"]},"metadata":{"tags":[]},"execution_count":9}]},{"cell_type":"code","metadata":{"id":"gEDxd96Y83h3","outputId":"b065edab-e266-4db4-b542-6ad1521dffec"},"source":["age = input('age? ')\n","age = int(age)\n","print('The double of your age is {}'.format(2*age))\n","print(type(age))"],"execution_count":null,"outputs":[{"output_type":"stream","text":["The double of your age is 20\n","<class 'int'>\n"],"name":"stdout"}]},{"cell_type":"code","metadata":{"id":"ku8fGhtu9Sl6","outputId":"a6b32935-2f52-421a-cb26-338dbd4f946d"},"source":["age = int(input('age? '))\n","print('The double of your age is {}'.format(2*age))\n","print(type(age))"],"execution_count":null,"outputs":[{"output_type":"stream","text":["The double of your age is 20\n","<class 'int'>\n"],"name":"stdout"}]},{"cell_type":"markdown","metadata":{"id":"zPLSQZBrGrIv"},"source":["## Bad programming"]},{"cell_type":"code","metadata":{"id":"T9OW7W6qGquQ"},"source":["# This will change the roles of type and str\n","str, type = type, str"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"voYQwWVtFrhQ"},"source":["val = 3.1416\n","print('The type of val is', type(val))\n","print('Converting val to string', str(val))"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"tGyUUzfyHD2f"},"source":["# Restore it before more damage is done.\n","str, type = type, str"],"execution_count":null,"outputs":[]},{"cell_type":"markdown","metadata":{"id":"mjFISlyHEwyg"},"source":["## Operators and Expressions"]},{"cell_type":"code","metadata":{"id":"xcks5y4XcfsA"},"source":["x = 2**3\n","y = 2 + 6\n","print(2**x == 2**y)"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"avEW5w8zxhDz"},"source":["# binary operators +, -, *, /, //, %\n","print('9 + 2 =', 9 + 2)\n","print('9.1 + 2.0 =', 9.1 + 2.0)\n","\n","print('9 - 2 =', 9 - 2)\n","print('9.1 - 2.0 =', 9.1 - 2.0)\n","\n","print('9 * 2 =', 9 * 2)\n","print('9.1 * 2.0 =', 9.1 * 2.0)\n","\n","print('9 / 2 =', 9 / 2)\n","print('9.1 / 2.0 =', 9.1 / 2.0)\n","\n","print('9 // 2.0 =', 9 // 2.0)\n","print('9 % 2 =', 9 % 2)\n"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"iIO-CNcddskR"},"source":["(-1)%(-2)"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"SVXqJ-2miy_8"},"source":["print('9//4 is', 9//4)\n","print('(-1)//2 is', (-1)//2)\n","print('(-1)//(-2) is', (-1)//(-2))\n","print('1//2 is', 1//2)\n","print('1//(-2) is', 1//(-2))\n","print('9//4.5 is', 9//4.5 )"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"BwxrIEKxkESW"},"source":["print('9%4 is', 9//4)\n","print('(-1)%2 is', (-1)%2)\n","print('(-1)%(-2) is', (-1)%(-2))\n","print('1%2 is', 1%2)\n","print('1%(-2) is', 1%(-2))\n","print('9%4.5 is', 9%4.5 )"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"0ApK6mpqLTAU"},"source":["print('The value and type of 9 // 4.5 are {} and {}'.format(\n","    9//4.5, type(9//4.5)))"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"le_Amj9V7TPI"},"source":["'''\n","Guess result of the expression below:\n","'''\n","x = -5 * 4 // 2 * 3 + -1 * 2\n","print(x)"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"QdSJYl2ANagw"},"source":["x = 5 * 4 + +3 / 2\n","print(x)\n","y = 5 * 4 - 3 // 2\n","print(y)"],"execution_count":null,"outputs":[]}]}