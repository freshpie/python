import math
import fractions
import decimal
import random

a = [4534,2663,62,5234,234,234,234,234]

print(sum(a))
print(max(a))
print(min(a))
print(pow(2,2,3))
print(divmod(5,2))


print(list(range(0,10)))
print(tuple(range(0,10)))


print(math.modf(4.9))
print(math.ceil(4.9))
print(math.floor(4.9))

print(math.sqrt(4949492))
print(math.exp(23))
print(math.log(4,2))

print(math.degrees( 2 * math.pi ))
print(math.radians( 1080 ))
print(math.radians( 1080 ) / (math.pi * 2) )

print(fractions.Fraction(4,16))
print(fractions.Fraction("0.5"))


print(decimal.Decimal(3))
print(decimal.Decimal("33.3"))
print(decimal.Decimal( (0, (5,5,3,6,7,3),-4 ) ))
print(decimal.Decimal( "NaN" ))
print(decimal.Decimal( "Infinity" ))


a=decimal.Decimal(0.44444)
b=decimal.Decimal(0.44444)

print(a*b*a)

c1=[decimal.Decimal( "Infinity" ), decimal.Decimal( "NaN" ),decimal.Decimal( "-Inf" ), decimal.Decimal( "0" ), decimal.Decimal( "354235" ),decimal.Decimal( "-33.35463" )]
c2=[decimal.Decimal( "Infinity" ), decimal.Decimal( "-Inf" ), decimal.Decimal( "0" ), decimal.Decimal( "354235" ),decimal.Decimal( "-33.35463" )]
print(c1)
print(sorted(c2))

random.seed()
print(random.random())

print(random.randint(1, 45))
print(random.choice( c2  ))

print( c2 )
print(random.shuffle( c2  ))
print( c2 )


for i in range(3):
    print(random.gauss(1, 1.0))
    
print(random.sample(range(1,46),6))