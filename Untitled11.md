1.How many seconds are in an hour? Use the interactive interpreter as a calculator and multiply the number of seconds in a minute (60) by the number of minutes in an hour (also 60).
sol. 60

Ans:


```python
60*60
```




    3600


2. Assign the result from the previous task (seconds in an hour) to a variable called seconds_per_hour.

Ans:

```python
seconds_per_hour=3600
```
3. How many seconds do you think there are in a day? Make use of the variables seconds per hour and minutes per hour.

Ans

```python
seconds_per_hour=3600
minutes_per_hour=60
total_seconds=24*seconds_per_hour
print('total seconds: ',total_seconds)
```

    total seconds:  86400
    
4. Calculate seconds per day again, but this time save the result in a variable called seconds_per_day

Ans:

```python
seconds_per_hour=3600
minutes_per_hour=60
seconds_per_day=24*seconds_per_hour
```
5. Divide seconds_per_day by seconds_per_hour. Use floating-point (/) division.

```python
div=seconds_per_day/seconds_per_hour
```
6. Divide seconds_per_day by seconds_per_hour, using integer (//) division. Did this number agree with the floating-point value from the previous question, aside from the final .0?

Ans:it put aside 0 

```python
div=seconds_per_day//seconds_per_hour

```
7. Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

Ans:

```python
def genPrimes():
    primes=2
    num=3
    while True:
        is_prime=True
        for prime in Primes:
            if num % prime==0:
                is_prime=False
                break
        if is_prime:
            primes.append(num)
            yield num
        num=+1
    
```
