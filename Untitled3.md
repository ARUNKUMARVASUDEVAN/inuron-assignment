1. What is the name of the feature responsible for generating Regex objects?


Ans:
 're' module is responsible for generating Regex objects.
 

2. Why do raw strings often appear in Regex objects?

Ans:
Raw strings, denoted by placing an 'r' before the string literal, are often used in Regex objects because they allow you to specify a pattern without having to worry about escaping special characters.


3. What is the return value of the search() method?

Ans:

The search() method in Python's re module returns a match object if it finds a match for the regular expression pattern in the string being searched, and None if there is no match.

4. From a Match item, how do you get the actual strings that match the pattern?

Ans:

We can use group()method, The group() method returns the string that was matched by the regular expression.

5. In the regex which created from the 'r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group zero cover?
Group 2? Group 1?

Ans:
Group 0 (or group()) covers the entire matched substring.
Group 1 (or group(1)) covers the substring matched by the first capturing group, which is the three digits before the hyphen.
Group 2 (or group(2)) covers the substring matched by the second capturing group, which is the three digits and four digits after the hyphen.

6. In standard expression syntax, parentheses and intervals have distinct meanings. How can you tell
a regex that you want it to fit real parentheses and periods?

In regular expression syntax, parentheses and intervals have special meanings. To match the actual characters "(", ")", and ".", you can use the backslash "" character to escape them

7. The findall() method returns a string list or a list of string tuples. What causes it to return one of
the two options?

The findall() method in Python's re module searches a string for all non-overlapping occurrences of a regular expression and returns the matches as a list of strings.
Whether findall() returns a list of strings or a list of string tuples depends on the regular expression pattern used in the search.
If the regular expression pattern does not contain any capturing groups (i.e., no parentheses), then findall() returns a list of strings, where each element in the list corresponds to a non-overlapping match of the pattern in the input string.


8. In standard expressions, what does the | character mean?

Ans:
 logical OR operator
 
 
9. In regular expressions, what does the character stand for?

Ans:
In regular expressions, the dot (.) character (also known as a period) is a wildcard character that matches any single character, except for a newline character.For example, the regular expression pattern a.b matches any string that starts with "a", ends with "b", and has any single character in between. So, this pattern would match "axb", "aab", "a1b", "a b", and so on, but not "a\nb".

10.In regular expressions, what is the difference between the + and * characters?

Ans:
In regular expressions, the + and * characters are both quantifiers that specify how many times a particular pattern should be repeated. However, they differ in how many repetitions they allow.

The * (asterisk) character matches zero or more occurrences of the preceding pattern. For example, the regular expression pattern ab*c matches any string that starts with "a", ends with "c", and has zero or more "b"s in between. So, this pattern would match "ac", "abc", "abbc", "abbbc", and so on.

On the other hand, the + (plus) character matches one or more occurrences of the preceding pattern. For example, the regular expression pattern ab+c matches any string that starts with "a", ends with "c", and has one or more "b"s in between. So, this pattern would match "abc", "abbc", "abbbc", and so on, but not "ac".

11. What is the difference between {4} and {4,5} in regular expression?

Ans:
{4} matches exactly four occurrences of the preceding pattern. For example, the regular expression pattern a{4} matches any string that has four consecutive "a"s. So, this pattern would match "aaaa" but not "aaa" or "aaaaa".

{4,5} matches between four and five occurrences of the preceding pattern. For example, the regular expression pattern a{4,5} matches any string that has either four or five consecutive "a"s. So, this pattern would match "aaaa" and "aaaaa", but not "aaa" or "aaaaaa".

12. What do you mean by the \d, \w, and \s shorthand character classes signify in regular
expressions?

Ans:
\d: Matches any digit character (i.e., any character from 0 to 9).
\w: Matches any word character (i.e., any alphanumeric character, including underscores).
\s: Matches any whitespace character (i.e., any space, tab, or newline character).

13. What do means by \D, \W, and \S shorthand character classes signify in regular expressions?

Ans:

\D: Matches any non-digit character (i.e., any character that is not from 0 to 9).
\W: Matches any non-word character (i.e., any character that is not alphanumeric, including underscores).
\S: Matches any non-whitespace character (i.e., any character that is not a space, tab, or newline character


14. What is the difference between .*? and .*?

Ans:

.*? and .* are the same except for the presence of the ? quantifier, which makes the .* expression non-greedy. The .* expression matches any character zero or more times, except for a newline character, whereas the .*? expression matches any character zero or more times, but matches as few characters as possible.

15. What is the syntax for matching both numbers and lowercase letters with a character class?
Ans:
to match both numbers and lowercase letters using a character class in a regular expression, you can use the shorthand character classes \d and \w, which match digits and word characters (letters, digits, and underscores), respectively

16. What is the procedure for making a normal expression in regax case insensitive?

ans:

re.IGNORECASE or re.I flag as the second argument to the re.compile() function or as the third argument to the re.search() or re.match() functions.

17. What does the . character normally match? What does it match if re.DOTALL is passed as 2nd argument in re.compile()?

Ans:
In a regular expression, the . character (period) matches any single character except for a newline character \n.

However, if the re.DOTALL or re.S flag is passed as the second argument to the re.compile() function or as the third argument to the re.search() or re.match() functions, then the . character will match any character, including newline characters.

18. If numReg = re.compile(r&#39;\d+&#39;), what will numRegex.sub(&#39;X&#39;, &#39;11 drummers, 10 pipers, five rings, 4
hen&#39;) return?
Ans:
If numRegex = re.compile(r'\d+'), then calling numRegex.sub('X', '11 drummers, 10 pipers, five rings, 4 hen') will replace all occurrences of one or more digits with the string 'X'.

19. What does passing re.VERBOSE as the 2nd argument to re.compile() allow to do?
Ans:

When re.VERBOSE is passed as the second argument to re.compile(), it allows you to write more readable and organized regular expressions by ignoring whitespace and comments within the regular expression pattern string.

Using re.VERBOSE, you can add comments to the regular expression pattern by enclosing them in (?#...) parentheses, and you can also add whitespace to separate parts of the pattern, without affecting the actual pattern matching.

20. How would you write a regex that match a number with comma for every three digits? It must
match the given following:
&#39;42&#39;
&#39;1,234&#39;
&#39;6,368,745&#39;

but not the following:
&#39;12,34,567&#39; (which has only two digits between the commas)
&#39;1234&#39; (which lacks commas)

Ans:

^\d{1,3}: one to three digits at the beginning of the string
(,\d{3})*: zero or more occurrences of a comma followed by three digits
$: end of the string

21. How would you write a regex that matches the full name of someone whose last name is
Watanabe? You can assume that the first name that comes before it will always be one word that
begins with a capital letter. The regex must match the following:
&#39;Haruto Watanabe&#39;
&#39;Alice Watanabe&#39;
&#39;RoboCop Watanabe&#39;
but not the following:
&#39;haruto Watanabe&#39; (where the first name is not capitalized)
&#39;Mr. Watanabe&#39; (where the preceding word has a nonletter character)
&#39;Watanabe&#39; (which has no first name)
&#39;Haruto watanabe&#39; (where Watanabe is not capitalized)

Ans:
^[A-Z][a-z]*: a word at the beginning of the string that starts with a capital letter
\s: a whitespace character
Watanabe$: the string "Watanabe" at the end of the string

22. How would you write a regex that matches a sentence where the first word is either Alice, Bob,
or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs;
and the sentence ends with a period? This regex should be case-insensitive. It must match the
following:
&#39;Alice eats apples.&#39;
&#39;Bob pets cats.&#39;
&#39;Carol throws baseballs.&#39;
&#39;Alice throws Apples.&#39;
&#39;BOB EATS CATS.&#39;
but not the following:
&#39;RoboCop eats apples.&#39;
&#39;ALICE THROWS FOOTBALLS.&#39;
&#39;Carol eats 7 cats.&#39;

Ans:
^ matches the start of the string.
(Alice|Bob|Carol) matches any of the specified names.
\s+ matches one or more whitespace characters.
(eats|pets|throws) matches any of the specified verbs.
\s+ matches one or more whitespace characters.
(apples|cats|baseballs) matches any of the specified nouns.
\. matches a period character.
$ matches the end of the string.
The regular expression is case-insensitive by default, so it will match any combination of uppercase and lowercase letters for the specified names, verbs, and nouns.

```python

```
