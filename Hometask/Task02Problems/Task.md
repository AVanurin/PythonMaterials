## Задание 01

Написать программу для поиска дубликата

Программа получает на вводе список строк.

### Пример ввода:

Ниже приводятся примеры ввода в такую программу. Все слова разделяются пробелом и могут содержать все символы, кроме пробельных. В таком наборе слов
гарантировано будет один дубликат

```bash
fredo 12redo sd	kjf 12redo
banana banana orange apple
b ft h g koip se qwert b
```

Программа должна найти среди слов дубликат и распечатать его на экран

### Пример вывода программы

Примеры ответов на ввод выше

```bash
12redo
banana
b
```

## Задание 02

Написать программу, которая будет считать количество человек в аудитории

Программа принимает на ввод число от 0 до 1000. Это число - количество человек в аудитории

### Примеры ввода:

Ниже приводятся примеры того, что может быть введено в программу

```bash
0
1
3
135
```

Программа должна сказать, сколько человек в аудитории

### Примеры вывода

```bash
0 человек
1 человек
3 человека
135 человек
```

## Задание 03

Написать программу для проверки email

Программа получает на вводе одну строку в виде адреса электронной почты

### Примеры ввода:

Ниже приводится два разных варианта ввода

```bash
akula@gmail.com
akula.gmail_com
```

Программа должна определять, является ли введенная строка корректным email'ом

### Примеры вывода

Ниже приводится два ответа на варианты ввода выше

```bash
True
False
```

Корректным email'ом считается такая строчка, которая состоит из двух частей - имени и названии домена, разделенные символом `@` 

## Задание 04

Программа цензурирует текст

Программа принимает на вход список запрещенных слов, в виде списка слов разделенные пробелами, и текст в виде строки

### Пример ввода:

```bash
math java sad
I had to choose between math or java. I have to admit it was pretty sadistic.
```

Программа должна заменить в тексте все слова, указанные в списке запрещенных слов и заменить их на строки `$#%@`

### Пример вывода:

```bash
I had to choose between $\#%@ or $\#%@. I have to admit it was pretty sadistic.
```

## Задание 05

Программа должна посчитать количество букв в некотором тексте. Программа должна игнорировать пробельные символы

Программа принимает на вход текст в виде строки

### Пример ввода:

```bash
Hello my dear friend
```

### Пример вывода:

```bash
h - 1
e - 3
l - 2
o - 1
m - 1
y - 1
d - 2
a - 1
r - 2
f - 1
i - 1
n - 1
```




