﻿# Report for Assignment 1


## Project chosen

Name: Lizard

URL: https://github.com/terryyin/lizard 


Number of lines of code and the tool used to count it: 57603 counted with lizard.py (same Github link)


Programming language: Python


## Coverage measurement


### Existing tool

We used coverage.py and entered the following command in the main directory of lizard: coverage run -m pytest test
this gave the following output:

![output pytest](/Screenshots/Output_pytest.png)

Next, we constructed the report by doing 'coverage report' and we downloaded this with 'coverage html'. the test also included some Python packages that we ignored for this assignment and excluded them in the screenshots. the following two images are the result of the 'coverage report' inside the terminal:

![output coverage report 0](/Screenshots/Coverage_report0.png)
![output coverage report 1](/Screenshots/Coverage_report1.png)
![output coverage report 2](/Screenshots/Coverage_report2.png)


### Your own coverage tool

## Daniel Buis

the first function I chose was the DefaultOrderedDict class from default_ordered_dict.py in the lizard_ext directory based on its current coverage and complexity. (coverage of 65%)

this is a link to a commit made in our forked repository that shows the instrumented code to gather coverage measurements: https://github.com/terryyin/lizard/commit/e929da5bf9a278d485483d1905e6c05b8c72b877

this is the output of the instrumentation after running the tests:
![instrumentation output 1](/Screenshots/Instrumentation_output_daniel1.png)

the second function I chose was the_state_nested_end from erlangt.py in the lizard_languages directory based on its current coverage and complexity. (coverage of 91%)

this is a link to a commit made in our forked repository that shows the instrumented code to gather coverage measurements: https://github.com/Djaro08/lizard-SEP/commit/7d847957c796bfa690bd6a188ed77018fc7bfa5c

this is the output of the instrumentation after running the tests:
![instrumentation output 2](/Screenshots/Instrumentation_output_daniel2.png)


## Kristóf Földházi

For my first function, I chose next_if from code_reader.py Here is the link to the commit that shows how I measured branch coverage: 
https://github.com/terryyin/lizard/commit/ac372cf7ce1fce86053129575f32545fedf72ec9


here is the output of the coverage measurement: 
![nextif_coverage](https://github.com/terryyin/lizard/assets/121450186/a5457074-ae30-4557-b34c-4214efe0552f)

As for my second function, I choose get_method from lizardnd.py. Here is the link to the commit that shows how I measured branch coverage: 
https://github.com/terryyin/lizard/commit/265349a6d9356796f8cbecca023e1d0d794d7bf8

here is the output of the coverage measurement: 
![lizad_nd_branch_coverage](https://github.com/terryyin/lizard/assets/121450186/f4d6e975-55b5-4ee1-86ac-3d6f6ca8bcd2)

## Darian de Graaf

I chose to measure the coverage from 2 functions in fortran.py in the lizard languages directory.
The first function I chose to measure the coverage on is _state_global and the second function is _ignore_if_paren. Neither of these functions were fully covered by the original tests.

In this commit you can see the code i added to measure the coverage of these functions. https://github.com/terryyin/lizard/commit/1c4e0a83567b86584c5368737235e8bd6cf90a59

In this screenshot you can see the coverage results of these changes resulting in a coverage of 44% over these 2 functions and a total coverage of 87% on this file as shown in the screenshots in the existing tool section.
![output own coverage tool Darian](/Screenshots/Coverage_personal_tool_Darian.png)

## Coverage improvement

### Individual tests

## Daniel Buis

Test 1:
this is a link to a commit made in our forked repository that shows the new/enhanced test:
https://github.com/Djaro08/lizard-SEP/commit/c7bd8ddc761acec37844bf5c466a407796dbad7b

The old coverage results:
![Old coverage 1](Screenshots/Old_coverage_Daniel1.png)

The new coverage results:
![improved coverage 1](/Screenshots/Improved_Coverage_Daniel1.png)


test_default_ordered_dict_with_default_factory:
This test creates an instance of DefaultOrderedDict with int as the default_factory.
It then tries to access a missing key, which should trigger the __missing__ method and use the default_factory to set the default value.

test_default_ordered_dict_without_default_factory:
This test creates an instance of DefaultOrderedDict without a default_factory.
It then tries to access a missing key, which should trigger the __missing__ method and raise a KeyError.

test_reduce_with_default_factory:
This test creates an instance of DefaultOrderedDict with int as the default_factory.
It calls the __reduce__ method, which should return a tuple representing the instance.

test_reduce_without_default_factory
This test creates an instance of DefaultOrderedDict without a default_factory.
It calls the __reduce__ method, which should return a tuple representing the instance.

Test 2:
this is a link to a commit made in our forked repository that shows the new/enhanced test: https://github.com/terryyin/lizard/commit/a58cae72cf51eb2ba055c82d7257a8bd9ea67614 

The old coverage results:
![Old coverage 2](Screenshots/Old_coverage_Daniel2.png)

The new coverage results:
![improved coverage 2](/Screenshots/Improved_Coverage_Daniel2.png)

test_state_nested_end_with_dot:
This test sets up the state machine to be in _state_nested_end. It pushes a function named 'fun' onto the stack. It then feeds the '.' token to the state machine.
The presence of 'fun' in the stack should trigger the nested end condition, calling self.statemachine_return() and then transitioning to _state_global.
This covers the condition if token == '.' or token == ',' and checks the inner condition if len(self.context.stacked_functions) > 1 and self.context.stacked_functions[-1].name == 'fun'.


## Kristóf Földházi

<Test 1>

Here is the link for the first improved test: https://github.com/terryyin/lizard/commit/1e9ad5d8fae75b5300cd4adefafd95508a2ca1af

Before improving, the coverage was at 97% and I improved it to 99%. This could be done because I covered two more branches than the original coverage. This was achieved with the test functions test_next_if_token_equal and test_next_if_token_not_equal

Old coverage result: 

![nexif_original](https://github.com/terryyin/lizard/assets/121450186/801ad305-66eb-4a5e-a945-5f502cf8e51f)

New coverage result: 

![nextif_after](https://github.com/terryyin/lizard/assets/121450186/98aedc2e-34ab-4c2f-b133-60cb5c6eac7a)


<Test 2>
Here is the link for the second improved test: https://github.com/terryyin/lizard/commit/85d5001cb3c5457f7da97b3cc24f146e0df2f81f

The old coverage was at 93% and I managed to improve it to 95% by covering two more branches compared to the original tests. These branches were covered with the tests test_with_func_attribute and test_without_func_attribute

Old coverage result:

![Screenshot 2024-06-16 194931](https://github.com/terryyin/lizard/assets/121450186/112cf0fe-13a7-4547-9c2b-cb753002d672)

New coverage result:

![Screenshot 2024-06-16 200304](https://github.com/terryyin/lizard/assets/121450186/5cf02840-5cb4-4880-a2c9-73182c1d8b04)

## Darian de Graaf

<Test 1>
The first test i made is called test_new_block. In the following commit you can see the test from line 62-82.
https://github.com/terryyin/lizard/commit/762b627af59d9cf2ae9b288f29c4d05f8bae8172

The old coverage results
![output own coverage tool Darian](/Screenshots/Coverage_fortran_before.png)

The new coverage results
![output own coverage tool Darian](/Screenshots/Coverage_fortran_after1.png)

Before the coverage was 87% on the fortran.py file and after the first new test the coverage is improved to 89%.
This happened because the 2 functions mentioned earlier in the personal tool measurement _state_global and _ignore_if_paren had a total of 3 extra branches covered.
One branch in _state_global for the BLOCK token and both branches in the _ignore_if_paren function are covered by this test.

<Test 2>
The second test i made is called test_program. In the following commit you can see the new test from line 69-86
https://github.com/terryyin/lizard/commit/18f006521925030094da6b0c6d30bfcf9976146d

The old coverage results

![output own coverage tool Darian](/Screenshots/Coverage_fortran_before.png)

The new coverage results

![output own coverage tool Darian](/Screenshots/Coverage_fortran_after2.png)

Before the second new test, the coverage was 89% as stated above and after the second new test, the coverage improved to 91%.
The new test covers one branch in the _state_global function, namely the PROGRAM branch, and tests if this branch is properly executed.


### Overall


This is a screenshot of the old coverage results. We retrieved by running an existing tool (the same as we already showed above)

![output coverage report 0](/Screenshots/Coverage_report0.png)
![output coverage report 1](/Screenshots/Coverage_report1.png)
![output coverage report 2](/Screenshots/Coverage_report2.png)

The following screenshots show the improved coverage for all functions we improved. Sidenote: on the laptop of Daniel were some Python files that were included in the coverage report. We left them out of our results as they are not relevant for the coverage of the lizard files. besides this, we managed to improve the overall coverage by 1%.


This is the prove that all the test pass on one computer. we have put a red line after the altered and created tests:
![new coverage](/Screenshots/new_coverage0.png)

These screenshots show that the coverage is improved after we merged the files and tested everything:
![new coverage](/Screenshots/new_coverage1.png)
![new coverage](/Screenshots/new_coverage2.png)

As you can see, the coverage has been improved from 49% to 50%. This could have been more without the python files that are tested. (we decided to exclude this from the results as they are irrelevant).

## Statement of individual contributions

Daniel Buis:
Daniel made the improvements for the default_ordered_dict.py file and function and the erlang.py file regarding the _state_nested_end function. the test_own.py and test_own2.py files were created for this to test the improved coverage. He also created the overall results and statement of individual contribution

Darian de Graaf:
Darian improved two functions in the Fortran.py: _state_global and _ignore_if_paren. He also updated the Fortran_test file with additional tests to improve coverage. 

Kristóf Földházi:
Kristof improved the next_if from code_reader.py and the get_method from lizardnd.py files. He created the test_next_if.py and the test_lizardnd.py for these files to improve coverage.

These 3 team members have communicated clearly with each other and everyone met the internal deadlines.
We did have a fourth team member, but he decided to drop out of the assignment. This has been communicated with the professor and he has been removed from the group in Canvas. 
