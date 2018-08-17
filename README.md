searchWord
==========

Python utility to search for a word in a text file.  If found, returns the complete paragraph the word was found in. 

It is particularly useful if used with GPG and bash as a password manager.  Just add the following to your ```.bashrc```:

### password manager
``` bash
function qpass () {
    /usr/bin/gpg -d < ~/Kevin/docs/passwords.gpg | ~/bin/searchWord.py "$@" | more
}
```

Make sure ```searchWord.py``` is located such that it can be found via your PATH setting.

Maintain your passwords in a simple txt file and encrypt it with you GPG key.  Organize your password entries almost any way you desire with whatever info you want to save, but make sure to put a new paragraph between each entry.

Example entries separated by whitespace:

```
Gmail
    URL:  http//gmail.com
    UserID:  myemail@gmail.com
    Passwd:  mySecret01

New York Times
    URL:  http://nytimes.com
    UserID:   kevin@example.com
    Passwd:   mySecret02

Amazon
    URL:  http://amazon.com
    UserID:  kevin@example.com
    Passwd:  mySecret03
```


If you happen to use vim for editing be sure to give folding a try.
