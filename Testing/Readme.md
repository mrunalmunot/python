#sample_tests.txt
===============================
Demonstrating usage of doctest
===============================

1. This doctest checks functionality of  python's plus operator.

\>>> 2 + 4

6

\>>> -10.5 + 8

-2.5


#command
python3 ‑m doctest sample_tests.txt

#command
python3 ‑m doctest -v sample_tests.txt

#output

Trying:

    2 + 4

Expecting:

    6

ok

Trying:

    -10.5 + 8

Expecting:

    -2.5

ok

1 items passed all tests:

   2 tests in sample_tests.txt

2 tests in 1 items.

2 passed and 0 failed.

Test passed.
