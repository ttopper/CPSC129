# CPSC 129: Object-oriented Programming 2

## Week 1

### Course Information

1. Course Description
2. [Schedule](01.1_Course_Information/01_Course_schedule.md)
3. [Addendum: Marking Scheme](01.1_Course_Information/02_Marking_scheme.md)

### Algorithm Development Case Study: Life 1: Conway's Game of Life (aka CGoL)

1. [Introduction](01.2_CGoL_1_Introduction/01_Introduction.md)
2. [Algorithm Overview and Pseudocode](01.2_CGoL_1_Introduction/02_Algorithm_overview.md)
3. [Create and Initialize the Universe](01.2_CGoL_1_Introduction/03_Create_and_initialize_U.md)
4. [Display the Universe](01.2_CGoL_1_Introduction/04_Display.md)
5. [Age the Universe](01.2_CGoL_1_Introduction/05_Age.md)
6. [conway_v0.py.png](01.2_CGoL_1_Introduction/conway_v0.py.png)

### [Assignment 1](Assignments/Assignment_01.md)

## Week 2

### Searching

1. [Introduction](02.1_Searching/01_Introduction.md)
2. [Linear search, unordered list](02.1_Searching/02_Linear_Search_Unordered_List.md)
3. [Linear search, ordered list](02.1_Searching/03_Linear_Search_Ordered_List.md)
4. [Binary search](02.1_Searching/04_Binary_Search.md)
5. [Interpolative search](02.1_Searching/05_Interpolative_Search.md)

### Algorithm Analysis

1. [Introduction](02.2_Algorithm_Analysis/01_Introduction.md)
2. [Big O Notation](02.2_Algorithm_Analysis/02_Big_O_notation.md)
3. [What order is linear search?](02.2_Algorithm_Analysis/03_Linear_search.md)
4. [What order is binary search?](02.2_Algorithm_Analysis/04_Binary_search.md)
5. [O(log n) vs O(n)](02.2_Algorithm_Analysis/05_O_log_n_vs_O_n.md)
6. [Common Algorithm Orders [11:22]](02.2_Algorithm_Analysis/06_Algorithm_orders.md)
7. MISSING

### Algorithm Development Case Study: Animation (Bouncing Balls using PyGame)

1. [Introduction](02.3_PyGame_1_Drawing/01_Introduction.md)
2. [Getting started with Pygame](02.3_PyGame_1_Drawing/02_pygame_test_0.md)
3. [It's installed, but is Pygame actually working?](02.3_PyGame_1_Drawing/03_pygame_test_1.md)
4. [Exiting Pygame more gracefully](02.3_PyGame_1_Drawing/04_pygame_test_2.md)
5. [Drawing something](02.3_PyGame_1_Drawing/05_pygame_test_3.md)
6. [Drawing lots of a thing](02.3_PyGame_1_Drawing/06_pygame_test_4.md)
7. [Drawing lots of things](02.3_PyGame_1_Drawing/07_pygame_test_5.md)
8. [Resource: The ball image](02.3_PyGame_1_Drawing/Aqua-Ball-icon.png)

### [Assignment 2](Assignments/Assignment_02.md)

## Week 3

### Recursion

1. [Recursion by example](03.1_Recursion/01_Recursion_by_example.md)
2. [Recursion Through a List](03.1_Recursion/02_Recursion_through_a_list.md)
3. [Calculating Factorials](03.1_Recursion/03_Calculating_factorials.md)
4. [Recursve Binary Search](03.1_Recursion/04_Recursive_binary_search.md)
5. [Recursive Data Structure](03.1_Recursion/05_Recursive_data_structures.md)
6. [recursion.py: Recursion examples](03.1_Recursion/06_recursion.md)
7. [Summary Notes](03.1_Recursion/07_Notes.md)

### Working with Text Files

1. [Context: Persistence](03.2_File_Processing/01_Persistence.md)
2. [Text versus binary files](03.2_File_Processing/02_Text_vs_binary_files.md)
3. [Reading from text files](03.2_File_Processing/03_Reading_from_text_files.md)
4. [Example: Searching log files](03.2_File_Processing/04_Example_searching_log_files.md)
5. [N.B. Files are sequential](03.2_File_Processing/05_Files_are_sequential.md)
6. [Is there more?](03.2_File_Processing/06_Is_there_more.md)
7. [Writing to text files](03.2_File_Processing/07_Writing_to_text_files.md)
8. [Appending to files](03.2_File_Processing/08_Appending_to_files.md)
9. [Reading numeric data](03.2_File_Processing/09_Reading_numeric_data.md)

### Life 2: Persistence

1. [Introduction](03.3_CGoL_2_Persistence/01_Introduction.md)
2. [The Goal](03.3_CGoL_2_Persistence/02_Goal.md)
3. [Option 1: Store a screenshot of the universe](03.3_CGoL_2_Persistence/03_Option_1_Screenshot.md)
4. [Option 2: Store the universe array using str(u)](03.3_CGoL_2_Persistence/04_Option_2_Python_list.md)
5. [Option 3: Store only the coordinates of live cells](03.3_CGoL_2_Persistence/05_Option_3_Coordinate_list.md)
6. [Option 4: Use only 1 bit per cell](03.3_CGoL_2_Persistence/06_Option_4_Bits.md)
7. [Python helps out: Pickling](03.3_CGoL_2_Persistence/07_Pickling.md)

### [Assignment 3](Assignments/Assignment_03.md)

## Week 4

### Review: From Pickles on Shelves to CRUD

1. [Context: Persistence](04.1_CRUD/01_Persistence.md)
2. [Python helps out: Pickling](04.1_CRUD/02_Pickling.md)
3. [Python helps out more: Shelves](04.1_CRUD/03_Shelves.md)
4. [Gotcha! Shelves update on assignment not mutation (?!)](04.1_CRUD/04_Shelve_gotcha.md)
5. [CRUD = A controller for our database](04.1_CRUD/05_Controller.md)
6. [The Main Event Loop](04.1_CRUD/06_The_main_event_loop.md)

### MVC Architecture (Model, View, Controller)

1. [Introduction](04.2_MVC_1/01_Introduction.md)
2. [Step 1: Separating the Model from the Controller](04.2_MVC_1/02_Step_1_Identify_model.md)
3. [Step 2: The Model](04.2_MVC_1/03_Step_2_Start_the_model.md)
4. [Step 3: The Quote Class](04.2_MVC_1/04_Step_3_The_quote_class.md)
5. [UIDs](04.2_MVC_1/05_UIDs.md)
6. [Step 4: The Model Revisited (for testing)](04.2_MVC_1/06_Step_4_Model_revisited_for_testing.md)
7. [Step 5: Controller revisited](04.2_MVC_1/07_Step_5_Controller_revisited.md)
8.  Support file: [Quote_0.py](04.2_MVC_1/04_Quote_0.py)
9.  Support file: [MVC_Model_0.py](04.2_MVC_1/06_MVC_Model_0.py)
10. Support file: [MVC_Controller_0.py](04.2_MVC_1/07_MVC_Controller_0.py)


###PyGame 2: Animation

1. [Introduction](04.3_PyGame_2_Animation/01_Introduction.md)
2. [Making something move 1](04.3_PyGame_2_Animation/02_pygame_test_6.md)
3. [Making something move 2](04.3_PyGame_2_Animation/03_pygame_test_7.md)
4. [Making something move 3](04.3_PyGame_2_Animation/04_pygame_test_8.md)
5. [Making something move 4](04.3_PyGame_2_Animation/05_pygame_test_9.md)
6. [Making something move 5](04.3_PyGame_2_Animation/06_pygame_test_10.md)
7. [Resource: The ball image](04.3_PyGame_2_Animation/Aqua-Ball-icon.png)

###[Assignment 4](Assignments/Assignment_04.md)

## Week 5

###Sorting 1

1. [Video(s): Sorting out sorting](05.1_Sorting_1/01_Sorting_out_sorting.md)
2. [Straight insertion sort](05.1_Sorting_1/02_Straight_insertion_sort.md)
3. [Straight selection sort](05.1_Sorting_1/03_Straight_selection_sort.md)
4. [Straight exchange sort](05.1_Sorting_1/04_Straight_exchange_sort.md)
5. [Shell sort](05.1_Sorting_1/05_Shell_sort.md)

###Life 3: More speed!

1. [Where to begin?](05.2_CGoL_3_Speed/01_Where_to_begin.md)
2. [Measure, don't guess](05.2_CGoL_3_Speed/02_Measure_dont_guess.md)
3. [Reworking Aging](05.2_CGoL_3_Speed/03_Reworking_aging.md)
4. [The new aging scheme](05.2_CGoL_3_Speed/04_The_new_aging_scheme.md)
5. [Is it better? Measure again](05.2_CGoL_3_Speed/05_Measure_again.md)

###[Assignment 5](Assignments/Assignment_05.md)

## Week 6

###MVC 2: Even more separation

1. [The Issue](06.1_MVC_2/01_The_issue.md)
2. [The Payoff](06.1_MVC_2/02_The_payoff.md)
3. [Separating Controller and Quote](06.1_MVC_2/03_Separating_controller_and_quote.md)
4. [A Quote Factory](06.1_MVC_2/04_Quote_factory.md)
5. [Adding More Object Types](06.1_MVC_2/05_Adding_more_object_types.md)
6. [Your Turn](06.1_MVC_2/06_Your_turn.md)
7. [MVC_controller.py](06.1_MVC_2/MVC_controller.py)
8. [MVC_model.py](06.1_MVC_2/MVC_model.py)
9. [quote.py](06.1_MVC_2/quote.py)

###Creating Mazes: A case study in OOP and algorithm development

1. [The Problem](06.2_Mazes_1/01_The_problem.md)
2. [Approaches](06.2_Mazes_1/02_Approaches.md)
3. [From English to Pseudocode](06.2_Mazes_1/03_Step_1_From_english_to_pseudcode.md)
4. [Testing our Pseudocode](06.2_Mazes_1/04_Step_2_Testing_our_pseudocode.md)
5. [Revising our pseudocode](06.2_Mazes_1/05_Step_3_Revise_pseudocode.md)
6. [Data Structures (OOP)](06.2_Mazes_1/06_Step_4_OOP.md)
7. [Initializing the Maze](06.2_Mazes_1/07_Step_5_Initializing_maze.md)
8. [Add some debugging output](06.2_Mazes_1/08_Step_6_Debugging_output.md)
9. [Sharing walls](06.2_Mazes_1/09_Step_7_Sharing_walls.md)
10. [Put the pieces together](06.2_Mazes_1/10_Step_8_Put_the_pieces_together.md)
11. [A starting point: maze_3.py](06.2_Mazes_1/maze_3.py)

###[Assignment 6](Assignments/Assignment_06.md)

## Week 7

###Sorting and Algorithm Analysis 2

1. [Introduction](07.1_Sorting_2/01_Introduction.md)
2. [Quicksort](07.1_Sorting_2/02_Quicksort_1.md)
3. [A more Pythonic Quicksort](07.1_Sorting_2/03_Quicksort_2.md)
4. [Representing a tree using a list](07.1_Sorting_2/04_Tree_in_a_list.md)
5. [Heapsort](07.1_Sorting_2/05_Heapsort.md)

###Life 4: Renovations

1. [A graphical interface to go with our graphical display](07.2_CGoL_4_GUI/01_The_goal.md)
2. [Step 1: Make a plan](07.2_CGoL_4_GUI/02_Step_1_Make_a_plan.md)
3. [Step 2: Review existing code](07.2_CGoL_4_GUI/03_Step_2_Review_existing_code.md)
4. [Step 3: Test existing code](07.2_CGoL_4_GUI/04_Step_3_Test_existing_code.md)
5. [Step 4: Make room for the menu](07.2_CGoL_4_GUI/05_Step_4_Make_room_for_the_menu.md)
6. [Step 5: Refactoring interlude](07.2_CGoL_4_GUI/06_Step_5_Refactoring_interlude.md)
7. [Step 6: Display the menu icons](07.2_CGoL_4_GUI/07_Step_6_Display_menu_icons.md)
8. [Step 7: Map mouse clicks to actions](07.2_CGoL_4_GUI/08_Step_7_Map_clicks_to_actions.md)
9. [Step 8: Merge the UI and the simulation](07.2_CGoL_4_GUI/09_Step_8_Merge_ui_and_simulation.md)
10. [life_gui_6.py: Ending point of the presentation; starting point for the assignment](07.2_CGoL_4_GUI/life_gui_6.py)

###[Assignment 7](Assignments/Assignment_07.md)

## Week 8

###CGI: Give your Python application a web interface

1. [Introduction](08.1_CGI/01_Introduction.md)
2. [Software Distribution](08.1_CGI/02_Software_distribution.md)
3. [Web-based Computing](08.1_CGI/03_Web_computing.md)
4. [Introduction to CGI](08.1_CGI/04_Introduction_to_CGI.md)
5. [Your first web server](08.1_CGI/05_Your_first_web_server.md)
6. [Testing static serving](08.1_CGI/06_Testing_static_serving.md)
7. [Testing CGI serving](08.1_CGI/07_Testing_CGI_serving.md)
8. [Toward a real CGI program](08.1_CGI/08_Toward_a_real_CGI_program.md)
9. [The input form](08.1_CGI/09_The_input_form.md)
10. [The processing script](08.1_CGI/10_The_processing_script.md)
11. [Unifying the form input file and the script file](08.1_CGI/11_Unifying_input_form_and_processing_script.md)
12. Support file:[mi2km_input_v3/](08.1_CGI/mi2km_input_v3.md)
13. Support file:[mi2km_output_v3/](08.1_CGI/mi2km_output_v3.md)
14. [Fancier input](08.1_CGI/12_Fancier_input.md)
15. [HTML form controls](08.1_CGI/13_HTML_form_controls.html)
16. [demoform.py](08.1_CGI/demoform.py)
17. [Fancier output](08.1_CGI/14_Fancier_output.md)

###Interactive Maze

1. [Interactive Maze](08.2_Mazes_2/01_Interactive_Maze.md)

###[Assignment 8](Assignments/Assignment_08.md)

## Week 9

###Two Approaches to Median Finding: An Algorithm Development Case Study

1. [Introduction](09.1_Median/01_Introduction.md)
2. [Median by Partitioning v0](09.1_Median/02_median_by_partn_0.md)
3. [Median by Partitioning v1](09.1_Median/03_median_by_partn_1.md)
4. [Median by Partitioning v2](09.1_Median/04_median_by_partn_2.md)
5. [Median by Partitioning v3](09.1_Median/05_median_by_partn_3.md)
6. [Median by Bounding v0 [5:35]](09.1_Median/06_median_by_bounding_0.md)
7. [Median by Bounding v1 [5:00]](09.1_Median/07_median_by_bounding_1.md)
8. [Median by Bounding v2 [3:50]](09.1_Median/08_median_by_bounding_2.md)
9. [Median by Bounding v3 [6:25]](09.1_Median/09_median_by_bounding_3.md)

###Data Processing

1. [Introduction](09.2_Data_Processing/01_Introduction.md)
2. [Case Study: Spelling Bee Administration](09.2_Data_Processing/02_Spelling_bee_The_problem.md)
3. [Data Processing View](09.2_Data_Processing/03_Spelling_bee_Data_processing_view.md)
4. [Potential Problems](09.2_Data_Processing/04_Spelling_bee_Potential_problems.md)
5. [Python Exceptions](09.2_Data_Processing/05_Python_exceptions.md)
6. [EasyGUI](09.2_Data_Processing/06_EasyGUI.md)

###[Assignment 09](Assignments/Assignment_09.md)

## Week 10

###HTTP + OOP: Building an Object Server

1. [Introduction](10.1_HTTP_REST/01_Introduction.md)
2. [The problem with CGI](10.1_HTTP_REST/02_The_problem_with_CGI.md)
3. How the web works:
4. [The World Wide Web](10.1_HTTP_REST/03_The_world_wide_web.md)
5. [The inner nature of HTTP](10.1_HTTP_REST/04_The_inner_nature_of_HTTP.md)
6. [HTTP "on the wire"](10.1_HTTP_REST/05_HTTP_on_the_wire.md)
7. [Browsing without a browser](10.1_HTTP_REST/06_Browsing_without_a_browser.md)
8. [CRUD = HTTP?](10.1_HTTP_REST/07_CRUD_vs_HTTP.md)
9. Creating a specialized webserver:
10. [A minimal HTTP server in Python](10.1_HTTP_REST/08_A_minimal_HTTP_server_in_python.md)
11. [An ugly truth about browsers](10.1_HTTP_REST/10_The_ugly_truth_about_browsers.md)
12. [Translating MVC + CRUD to HTTP](10.1_HTTP_REST/11_Translating_MVC_CRUD_to_HTTP.md)
13. [Our HTTP request-response cycles](10.1_HTTP_REST/12_Our_HTTP_request_response_cycles.md)
14. [Interaction storyboard](10.1_HTTP_REST/13_Interaction_storyboard.md)
15. [Code reuse](10.1_HTTP_REST/14_Code_reuse.md)
16. [Mapping to HTTP + URL pairs](10.1_HTTP_REST/15_Mapping_actions_to_HTTP_method_URL_pairs.md)
17. [Actual Code (](10.1_HTTP_REST/16_Actual_code.md)Source files:[quote_server.py](10.1_HTTP_REST/quote_server_5.py),[quote.py](10.1_HTTP_REST/quote_3.py))
18. Towards an Object Server:
19. [1. Identify couplings to quote.py](10.1_HTTP_REST/17_To_object_server_1.md)
20. [2. Object creation menu requirements](10.1_HTTP_REST/18_To_object_server_2.md)
21. [3. Object creation menu Python code](10.1_HTTP_REST/19_To_object_server_3.md)
22. [4. Final steps](10.1_HTTP_REST/20_To_object_server_4.md)
23. [(A thing we're not doing.)](10.1_HTTP_REST/21_Something_we_re_not_doing.md)
24. [Summary](10.1_HTTP_REST/22_Summary.md)

###Image Processing 1

1. [Introduction](10.2_IP_1/01_Introduction.md)
2. [PIL: The Python Imaging Library](10.2_IP_1/02_PIL.md)
3. [Test Images](10.2_IP_1/03_Test_images.md)
4. [IPO Programming](10.2_IP_1/04_IPO.md)
5. [Point vs Neighbourhood Processes](10.2_IP_1/05_Point_vs_neighbourhood.md)
6. [Edge Detection](10.2_IP_1/06_Edge_detection.md)

###[Assignment 10](Assignments/Assignment_10.md)

## Week 11

###Pitcher Problems: A Case Study in Using Search Trees

1. [The problem](11.1_Pitcher_Problems/01_The_problem.md)
2. [First: Do it by hand](11.1_Pitcher_Problems/02_By_hand.md)
3. [Second: Notice what you did](11.1_Pitcher_Problems/03_Notice_what_you_did.md)
4. [Third: Identify the problem type](11.1_Pitcher_Problems/04_Identify_the_problem_type.md)
5. [Formalize the Algorithm](11.1_Pitcher_Problems/05_Formalize_the_algorithm.md)
6. [Pseudocode](11.1_Pitcher_Problems/06_Pseudocode.md)
7. [An edge case leads to a refinement](11.1_Pitcher_Problems/07_Refinement.md)
8. [Towards Python: A little OOP](11.1_Pitcher_Problems/08_OOP.md)
9. [Further towards Python: Pseudocode translation](11.1_Pitcher_Problems/09_Pseudocode_translation.md)
10. [Debugging `is_goal()`](11.1_Pitcher_Problems/10_Debugging_is_goal.md)
11. [Interlude: Bitwise operations (really just `&`)](11.1_Pitcher_Problems/11_Bitwise_operations.md)
12. [Back to our program: `is_goal()`](11.1_Pitcher_Problems/12_is_goal.md)
13. [Final program](11.1_Pitcher_Problems/13_Final_program.md)

###Data Processing: Reporting

1. [A report generation problem](11.2_Reporting/01_The_Problem.md)

###[Assignment 11](Assignments/Assignment_11.md)

## Week 12

###Image Enhancement Lab

1. [Introduction](12.1_IP_2/01_Introduction.md)
2. [Dynamic Range](12.1_IP_2/02_Dynamic_range.md)
3. [Noise Filtering](12.1_IP_2/03_Noise_filtering.md)
4. [Sharpening](12.1_IP_2/04_Sharpening.md)

###DP: Names and Addresses

1. [Algorithms and Heuristics](12.2_YG_Emails/01_Algorithms_and_heuristics.md)
2. [Introduction](12.2_YG_Emails/02_YG_Introduction.md)
3. [The Goal](12.2_YG_Emails/03_YG_Goal.md)
4. [Complications](12.2_YG_Emails/04_YG_Complications.md)
5. [activedirectory.txt](12.2_YG_Emails/activedirectory.txt)
6. [peoplesoft.txt](12.2_YG_Emails/peoplesoft.txt)

###[Assignment 12](Assignments/Assignment_12.md)

## Week 13

###Exam Preparation

1. [Examinable topics](13.1_Exam_Preparation/01_Examinable_topics.md)
2. [Exam Study Guide](13.1_Exam_Preparation/02_Exam_study_guide.md)
3. [Redacted final exam + Q&A](13.1_Exam_Preparation/03_Redacted_final_exam.md)
