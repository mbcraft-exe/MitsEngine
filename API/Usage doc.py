"""
© MB INC

[OPTIONS]
- install; {module_name, version=Default} : Installing Python external modules from PyPi (automatically recognized).
- say; {text} : Say something.
- calc; {numbers} *Computer syntaxe*.

[Context actions]
--Vars--
varname: "Something"
othervar: calc; 2 * 2

--say--
tosay: "Something"
say; {tosay}
say; "Something"
say; "Calculate : " & calc; 1 + 1

--Type of text--
LET/let : Only letters
NUM/num : Only Numbers
ALL/all : All kind of symbols
"""